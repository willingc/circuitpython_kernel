# -*- coding: utf-8 -*-
"""Kernelspec installation."""

import json
import os
import sys

from jupyter_client.kernelspec import install_kernel_spec
from IPython.utils.tempdir import TemporaryDirectory

kernel_json = {
 "argv": [sys.executable, "-m", "circuitpython_kernel", "-f", "{connection_file}"],
 "display_name": "CircuitPython",
 "language": "python",
}


def install_kernelspec(user=True):
    """Install circuitpython kernel to list of kernels."""
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        # TODO: Copy resources once they're specified

        print('Installing CircuitPython kernel spec')
        install_kernel_spec(td, 'CircuitPyKernel', user=user, replace=True)


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def main(argv=[]):
    user = '--user' in argv or not _is_root()
    install_kernelspec(user=user)

if __name__ == '__main__':
    main(argv=sys.argv)
