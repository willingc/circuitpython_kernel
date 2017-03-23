.. highlight:: shell

=====
Usage
=====

To use CircuitPython Kernel in a Jupyter Notebook, you must install
and activate the kernel specification (kernelspec) for Jupyter:

.. code-block:: console

    $ python3 circuitpython_kernel.install

You can check that CircuitPython has been activated for Jupyter:

.. code-block:: console

    $ jupyter kernelspec list

Removing CircuitPython from Jupyter's kernel specification list:

.. code-block:: console

    $ jupyter kernelspec remove circuitpython_kernel
