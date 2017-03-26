# -*- coding: utf-8 -*-
"""Basic functionality of CircuitPython kernel."""
import ast
import re
import sys
import time

from ipykernel.kernelbase import Kernel
from .board import connect
from .version import __version__


class CircuitPyKernel(Kernel):
    """CircuitPython kernel implementation."""
    protocol_version = '5.0.0'
    implementation = 'circuitpython_kernel'
    implementation_version = __version__
    language_info = {'name': 'python',
                     'version': '3',
                     'mimetype': 'text/x-python',
                     'file_extension': '.py',
                     'pygments_lexer': 'python3',
                     'codemirror_mode': {'name': 'python', 'version': 3},
                    }
    banner = "Jupyter and CircuitPython create fablab-ulous things."
    help_links = [
        {'text': 'CircuitPython kernel',
         'url': 'https://circuitpython_kernel.readthedocs.io',
        },
    ]


    def __init__(self, **kwargs):
        """Set up connection to board"""
        super().__init__(**kwargs)
        self.serial = connect()


    def run_code(self, code):
        """Run a code snippet.

        Parameters
        ----------
        code : str
            Code to be executed.

        Returns
        -------
        out
            Decoded result from code run.
        err
            Decoded error from code run.

        """
        self.serial.write(code.encode('utf-8') + b'\x04')

        result = bytearray()
        while not result.endswith(b'\x04>'):
            time.sleep(0.1)
            result.extend(self.serial.read_all())

        assert result.startswith(b'OK')
        out, err = result[2:-2].split(b'\x04', 1)

        return out.decode('utf-8', 'replace'), err.decode('utf-8', 'replace')


    def do_execute(self, code, silent=False, store_history=True,
                   user_expressions=None, allow_stdin=False):
        """Execute a user's code cell.

        Parameters
        ----------
        code : str
            Code, one or more lines, to be executed.
        silent : bool
            True, signals kernel to execute code quietly, and output is not
            displayed. The default is False.
        store_history : bool
            Whether to record code in history and increase execution count. If
            silent is True, this is implicitly false.
        user_expressions : dict, optional
            Mapping of names to expressions to evaluate after code is run.
        allow_stdin : bool
            Whether the frontend can provide input on request (e.g. for
            Python’s raw_input()).

        Returns
        -------
        dict
            Execution results.

        """
        out, err = self.run_code(code)

        if not silent:
            if out:
                self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text': out})
            if err:
                self.send_response(self.iopub_socket, 'stream', {'name': 'stderr', 'text': err})

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {}
                }


    def _eval(self, expr):
        """Evaluate the expression"""
        out, err = self.run_code('print({})'.format(expr))
        return ast.literal_eval(out)


    def do_complete(self, code, cursor_pos):
        """Support code completion."""
        code = code[:cursor_pos]
        m = re.search(r'(\w+\.)*(\w+)?$', code)
        if m:
            prefix = m.group()
            if '.' in prefix:
                obj, prefix = prefix.rsplit('.')
                names = self._eval('dir({})'.format(obj))
            else:
                names = self._eval('dir()')
            matches = [n for n in names if n.startswith(prefix)]
            return {'matches': matches,
                    'cursor_start': cursor_pos - len(prefix), 'cursor_end': cursor_pos,
                    'metadata': {}, 'status': 'ok'}
        else:
            return {'matches': [],
                    'cursor_start': cursor_pos, 'cursor_end': cursor_pos,
                    'metadata': {}, 'status': 'ok'}
