CircuitPython Kernel
====================

.. image:: https://readthedocs.org/projects/circuitpython-kernel/badge/?version=latest
        :target: https://circuitpython-kernel.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://img.shields.io/travis/adafruit/circuitpython_kernel.svg
    :target: https://travis-ci.org/adafruit/circuitpython_kernel

The CircuitPython Kernel is a `Jupyter Kernel <https://jupyter.org/>`_ designed to interact withAdafruit boards running `CircuitPython <https://github.com/adafruit/circuitpython>`_ from a Jupyter Notebook

Demo GIF
------
.. image:: https://cdn-learn.adafruit.com/assets/assets/000/055/304/original/circuitpython_2018-06-11_18-00-35.gif?1528754563


Status
------

This project is in a pre-alpha phase. It has been tested with CircuitPython (SAMD) boards and the Feather HUZZAH (esp8266) using CircuitPython 2.x Stable.

Supported Boards
----------------

Designed for CircuitPython
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `Adafruit CircuitPlayground Express <https://www.adafruit.com/product/3333>`__
-  `Adafruit Feather M0 Express <https://www.adafruit.com/product/3403>`__
-  `Adafruit Metro M0 Express <https://www.adafruit.com/product/3505>`_
-  `Adafruit Gemma M0 <https://www.adafruit.com/product/3501>`__
-  `Adafruit ItsyBitsy M0 Express <https://www.adafruit.com/product/3727>`_
-  `Adafruit Trinket M0 <https://www.adafruit.com/product/3500>`__


Other
~~~~~

-  `Adafruit Feather HUZZAH ESP8266 <https://www.adafruit.com/products/2821>`__


Download
--------

Official .zip files are available through the `latest GitHub
releases <https://github.com/adafruit/circuitpython_kernel/releases>`__.


Documentation
-------------

This kernel is fully documented on the Adafruit Learning System (*Guide Coming Soon!*)

Installing Jupyter
------------------

Option 1. Installing Jupyter with Anaconda

**Don't have a Python installation on your computer?** If you're new to all this, the Jupyter Project recommends installing `Anaconda <https://www.continuum.io/downloads>`_
, which installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science.

Option 2. Installing Jupyter with PIP

If you have a Python installation already on your computer, you may want to use the Python package manager (pip) instead of Anaconda. You'll need Python 3.3+.

First, ensure that you have the latest version of pip:

.. code:: shell

 $ pip3 install --upgrade pip


Install the Jupyter Notebook using:

.. code:: shell

 $ pip3 install jupyter

Ok, now that we have Jupyter installed, let's start the notebook server.

We can launch the server from a command line (either Terminal on macOS/Linux or Command Prompt on Windows) by running:

.. code:: shell

 $ jupyter notebook

If your installation went well, you'll see information about the notebook server in your command line. Also, your web browser will open to the URL displayed in your command line (http://localhost:8888), displaying the Notebook Dashboard.

Installing the CircuitPython Kernel
-----------------------------------
First, clone this repository.

.. code:: shell

 $ git clone https://github.com/adafruit/circuitpython_kernel.git

Navigate into the cloned repository directory. Install this kernel into Jupyter by running:

.. code:: shell

 $ pip3 install circuitpython_kernel

Then, run

.. code:: shell

 $ python3 -m circuitpython_kernel.install

* if you encounter errors running this command on macOS/Linux, you'll need to prefix this command with *sudo*

Finally, let's verify the kernel was installed correctly in Jupyter. To do this, run:


.. code:: shell

 $ jupyter kernelspec list

Your output should show circuitpython as an available kernel:

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/055/226/original/circuitpython_jupyter-kernelspec-list.png?1528483983


Launching a CircuitPython Notebook
----------------------------------
Launch jupyter by running:

.. code:: shell

 $ jupyter notebook

Make sure your board is plugged into USB and running CircuitPython by opening a file explorer. It should show up as a removable drive named **CIRCUITPY**.

Then click **new -> circuitpython** to open a new CircuitPython Notebook

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/055/305/original/circuitpython_newnotebook.gif?1528755209

A new CircuitPython Notebook should open and you should be able to execute code from within cells.
