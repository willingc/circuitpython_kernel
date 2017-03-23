from ipykernel.kernelapp import IPKernelApp
from .circuitpython_kernel import CircuitPyKernel

IPKernelApp.launch_instance(kernel_class=CircuitPyKernel)
