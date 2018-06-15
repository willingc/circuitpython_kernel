"""Kernel Launcher"""
import logging

from ipykernel.kernelapp import IPKernelApp
from .kernel import CircuitPyKernel

logging.basicConfig(level=logging.DEBUG)

IPKernelApp.launch_instance(kernel_class=CircuitPyKernel)
