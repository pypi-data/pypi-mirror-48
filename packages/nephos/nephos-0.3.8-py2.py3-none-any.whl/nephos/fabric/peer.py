#   Copyright [2018] [Alejandro Vicente Grabovetsky via AID:Tech]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at#
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import random
from time import sleep

from nephos.fabric.ord import check_ord_tls
from nephos.fabric.settings import get_namespace, get_version
from nephos.fabric.utils import get_helm_pod
from nephos.helpers.helm import (
    HelmPreserve,
    helm_check,
    helm_extra_vars,
    helm_install,
    helm_upgrade,
)


def check_peer(namespace, release):
    """Check if Peer is running.

    Args:
        namespace: Namespace where Peer is located.
        release: Name of Peer Helm release.
        

    Returns:
        bool: True once Peer is correctly running.
    """
    pod_exec = get_helm_pod(
        namespace=namespace, release=release, app="hlf-peer"
    )
    res = pod_exec.logs(1000)
    if "Received block" in res:
        return True
    while True:
        if "Starting peer" in res or "Sleeping" in res:
            return True
        else:
            sleep(15)
            res = pod_exec.logs(1000)


# TODO: Split CouchDB creation from Peer creation
def setup_peer(opts, upgrade=False):
    """Setup Peer on K8S.

    Args:
        opts (dict): Nephos options dict.
        upgrade (bool): Do we upgrade the deployment? False by default.
        
    """
    peer_namespace = get_namespace(opts, opts["peers"]["msp"])
    for release in opts["peers"]["names"]:
        # Deploy the CouchDB instances
        version = get_version(opts, "hlf-couchdb")
        config_yaml = f'{opts["core"]["dir_values"]}/hlf-couchdb/cdb-{release}.yaml'
        if not upgrade:
            extra_vars = helm_extra_vars(version=version, config_yaml=config_yaml)
            helm_install(
                opts["core"]["chart_repo"],
                "hlf-couchdb",
                f"cdb-{release}",
                peer_namespace,
                extra_vars=extra_vars,
                
            )
        else:
            preserve = (
                HelmPreserve(
                    peer_namespace,
                    f"cdb-{release}-hlf-couchdb",
                    "COUCHDB_USERNAME",
                    "couchdbUsername",
                ),
                HelmPreserve(
                    peer_namespace,
                    f"cdb-{release}-hlf-couchdb",
                    "COUCHDB_PASSWORD",
                    "couchdbPassword",
                ),
            )
            extra_vars = helm_extra_vars(
                version=version, config_yaml=config_yaml, preserve=preserve
            )
            helm_upgrade(
                opts["core"]["chart_repo"],
                "hlf-couchdb",
                f"cdb-{release}",
                extra_vars=extra_vars,
                
            )
        helm_check("hlf-couchdb", f"cdb-{release}", peer_namespace)

        # Deploy the HL-Peer charts
        version = get_version(opts, "hlf-peer")
        config_yaml = f"{opts['core']['dir_values']}/hlf-peer/{release}.yaml"
        extra_vars = helm_extra_vars(version=version, config_yaml=config_yaml)
        if not upgrade:
            helm_install(
                opts["core"]["chart_repo"],
                "hlf-peer",
                release,
                peer_namespace,
                extra_vars=extra_vars,
                
            )
        else:
            helm_upgrade(
                opts["core"]["chart_repo"],
                "hlf-peer",
                release,
                extra_vars=extra_vars,
                
            )
        helm_check("hlf-peer", release, peer_namespace)
        # Check that peer is running
        check_peer(peer_namespace, release)


def peer_channel_suffix(opts, ord_name):
    """Get command suffix for "peer channel" commands, as they involve speaking with Orderer.

    Args:
        opts (dict): Nephos options dict.
        ord_name (str): Orderer we wish to speak to.
        

    Returns:
        str: Command suffix we need to use in "peer channel" commands.
    """
    ord_tls = check_ord_tls(opts)
    if ord_tls:
        cmd_suffix = (
            "--tls "
            + f"--ordererTLSHostnameOverride {ord_name}-hlf-ord "
            + f"--cafile $(ls ${{ORD_TLS_PATH}}/*.pem)"
        )
    else:
        cmd_suffix = ""
    return cmd_suffix


def get_channel_block(peer_ex, ord_name, ord_namespace, channel, cmd_suffix):
    """Get channel block from Peer.

    Args:
        peer_ex (Executor): A Pod Executor representing a Peer.
        ord_name (str): Name of the orderer we wish to communicate with.
        ord_namespace (str): Namespace where the orderer resides.
        channel (str): Name of the channel we with to retrieve.
        cmd_suffix (str): Suffix to the "peer channel fetch" command.

    Returns:
        bool: Were we able to fetch the channel?
    """
    channel_file = f"/var/hyperledger/{channel}.block"
    channel_block, _ = peer_ex.execute(f"ls {channel_file}")
    if not channel_block:
        res, err = peer_ex.execute(
            (
                f"bash -c 'peer channel fetch 0 {channel_file} "
                + f"-c {channel} "
                + f"-o {ord_name}-hlf-ord.{ord_namespace}.svc.cluster.local:7050 {cmd_suffix}'"
            )
        )
        if err:
            return False
    return True


# TODO: Split channel creation from channel joining
def create_channel(opts):
    """Create Channel for Peer.

    Args:
        opts (dict): Nephos options dict.
        
    """
    peer_namespace = get_namespace(opts, opts["peers"]["msp"])
    ord_namespace = get_namespace(opts, opts["orderers"]["msp"])
    channel = opts["peers"]["channel_name"]
    # Get orderer TLS status
    ord_name = random.choice(opts["orderers"]["names"])
    # TODO: This should be a function
    cmd_suffix = peer_channel_suffix(opts, ord_name)

    for index, release in enumerate(opts["peers"]["names"]):
        # Get peer pod
        pod_ex = get_helm_pod(peer_namespace, release, "hlf-peer")

        # Check if the file exists
        has_channel = False
        while not has_channel:
            has_channel = get_channel_block(
                pod_ex, ord_name, ord_namespace, channel, cmd_suffix
            )
            if not has_channel:
                pod_ex.execute(
                    (
                        "bash -c 'peer channel create "
                        + f"-o {ord_name}-hlf-ord.{ord_namespace}.svc.cluster.local:7050 "
                        + f"-c {opts['peers']['channel_name']} -f /hl_config/channel/{channel}.tx {cmd_suffix}'"
                    )
                )
        res, _ = pod_ex.execute("peer channel list")
        channels = (res.split("Channels peers has joined: ")[1]).split()
        if opts["peers"]["channel_name"] not in channels:
            pod_ex.execute(
                (
                    "bash -c "
                    + "'CORE_PEER_MSPCONFIGPATH=$ADMIN_MSP_PATH "
                    + f"peer channel join -b /var/hyperledger/{opts['peers']['channel_name']}.block {cmd_suffix}'"
                )
            )
