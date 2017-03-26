# -*- coding: utf-8 -*-
"""Kernelspec installation."""

import json
import os
import sys
import getopt

from jupyter_client.kernelspec import install_kernel_spec
from IPython.utils.tempdir import TemporaryDirectory

kernel_json = {
    "argv": [sys.executable, "-m", "circuitpython_kernel", "-f", "{connection_file}"],
    "display_name": "CircuitPython",
    "mimetype": "text/x-python",
    "language": "python",
    "name": "circuitpython",
}


def install_my_kernel_spec(user=True, prefix=None):
    """Install circuitpython kernel to list of kernels."""
    user = '--user' in sys.argv or not _is_root()
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        kernel_name = kernel_json['name']
        print('Installing CircuitPython kernelspec')
        try:
            install_kernel_spec(td, kernel_name, user=user, replace=True,
                prefix=prefix)
        except:
            install_kernel_spec(td, kernel_name, user=not user, replace=True,
                prefix=prefix)


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def main(argv=[]):
    prefix = None
    user = not _is_root()

    opts, _ = getopt.getopt(argv[1:], '', ['user', 'prefix='])
    for k, v in opts:
        if k == '--user':
            user = True
        elif k == '--prefix':
            prefix = v
            user = False

    install_my_kernel_spec(user=user, prefix=prefix)

if __name__ == '__main__':
    main(argv=sys.argv)
