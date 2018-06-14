.. highlight:: shell

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


.. _GitHub repo: https://github.com/adafruit/circuitpython_kernel
.. _tarball: https://github.com/adafruit/circuitpython_kernel/tarball/master
