#!/usr/bin/python3
"""Create and distribute an archive to web servers."""

import imp

from fabric.api import env

env.hosts = ['<IP web-01>', '<IP web-02>']

packing = imp.load_source(
    'packing',
    '1-pack_web_static.py'
)
deployment = imp.load_source(
    'deployment',
    '2-do_deploy_web_static.py'
)

do_pack = packing.do_pack
do_deploy = deployment.do_deploy


def deploy():
    """Create an archive and deploy it to the web servers."""
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
