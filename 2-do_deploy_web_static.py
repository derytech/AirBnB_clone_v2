#!/usr/bin/python3
"""Fabric script to deploy a web_static archive to web servers."""

import os
from fabric.api import env, put, run

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Distribute an archive to web servers and activate the release."""
    if not os.path.isfile(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        release_name = filename.replace(".tgz", "")
        release_path = "/data/web_static/releases/{}".format(release_name)
        remote_archive = "/tmp/{}".format(filename)

        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(remote_archive, release_path))
        run("rm {}".format(remote_archive))

        run(
            "mv {}/web_static/* {}/".format(
                release_path, release_path
            )
        )
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True

    except Exception:
        return False
