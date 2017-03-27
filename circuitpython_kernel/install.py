# -*- coding: utf-8 -*-
"""Kernelspec installation."""

import getopt
import json
import os
import sys

from IPython.utils.tempdir import TemporaryDirectory
from jupyter_client.kernelspec import KernelSpecManager

kernel_json = {
    "argv": ["python", "-m", "circuitpython_kernel", "-f", "{connection_file}"],
    "display_name": "CircuitPython",
    "mimetype": "text/x-python",
    "language": "python",
    "name": "circuitpython",
}


def install_my_kernel_spec(user=True, prefix=None):
    """Install circuitpython kernel to list of kernels."""
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        print('Installing CircuitPython kernelspec')
        KernelSpecManager().install_kernel_spec(td, 'circuitpython',
            user=user, replace=True, prefix=prefix)
        print('Completed kernel installation.')


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def main(argv=None):
    if argv is None:
        argv = []
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
