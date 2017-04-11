#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyserial',
    'ipython',
    'ipykernel',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='circuitpython_kernel',
    version='0.2.0',
    description="CircuitPython Kernel enables CircuitPython to be used in Jupyter Notebooks for learning Python coding with microcontrollers.",
    long_description=readme + '\n\n' + history,
    author="Carol Willing",
    author_email='carolcode@willingconsulting.com',
    url='https://github.com/willingc/circuitpython_kernel',
    packages=[
        'circuitpython_kernel',
    ],
    package_dir={'circuitpython_kernel':
                 'circuitpython_kernel'},
    entry_points={},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='circuitpython_kernel jupyter notebook',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
