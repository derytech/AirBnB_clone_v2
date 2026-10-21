#!/usr/bin/python3
"""Fabric script to create a .tgz archive of web_static."""

from datetime import datetime
from fabric import task
from invoke import Context
from os import path


@task
def do_pack(c):
    """Pack the web_static folder into a timestamped .tgz archive."""
    try:
        c.run("mkdir -p versions")

        filename = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )

        print("Packing web_static to {}".format(filename))

        c.run("tar -cvzf {} web_static".format(filename))

        if not path.isfile(filename):
            return None

        print(
            "web_static packed: {} -> {}Bytes".format(
                filename, path.getsize(filename)
            )
        )

        return filename

    except Exception:
        return None
