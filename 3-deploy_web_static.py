
#!/usr/bin/python3
"""Distribute an archive to web servers."""

import imp
from fabric.api import env

# Replace these placeholders with your actual server IP addresses.
env.hosts = ['<IP web-01>', '<IP web-02>']

# Load the existing packing and deployment functions.
deployment = imp.load_source(
    'deployment',
    '2-do_deploy_web_static.py'
)

do_pack = deployment.do_pack
do_deploy = deployment.do_deploy


def deploy():
    """Create and distribute an archive to both web servers."""
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)

