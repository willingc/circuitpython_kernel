from ipykernel.kernelapp import IPKernelApp
from .kernel import CircuitPyKernel

IPKernelApp.launch_instance(kernel_class=CircuitPyKernel)
