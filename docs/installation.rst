.. highlight:: shell

============
Installation
============


Stable release
--------------

To install CircuitPython Kernel, run this command in your terminal:

.. code-block:: console

    $ pip3 install circuitpython_kernel
    $ python3 -m circuitpython_kernel.install

This is the preferred method to install CircuitPython Kernel, as it will
always install the most recent stable release.

If you don't have `pip3`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for CircuitPython Kernel can be downloaded from the `GitHub repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/willingc/circuitpython_kernel

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/willingc/circuitpython_kernel/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python3 setup.py install
    $ python3 -m circuitpython_kernel.install


.. _GitHub repo: https://github.com/willingc/circuitpython_kernel
.. _tarball: https://github.com/willingc/circuitpython_kernel/tarball/master
