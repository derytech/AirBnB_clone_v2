#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static."""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a .tgz archive of the web_static folder."""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        filename = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )

        print("Packing web_static to {}".format(filename))
        result = local("tar -cvzf {} web_static".format(filename))

        if result.failed:
            return None

        print(
            "web_static packed: {} -> {}Bytes".format(
                filename, os.path.getsize(filename)
            )
        )
        return filename

    except Exception:
        return None
