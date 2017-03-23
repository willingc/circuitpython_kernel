#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='circuitpython_kernel',
    version='0.1.0',
    description="CircuitPython Kernel enables CircuitPython to be used in Jupyterr Notebooks.",
    long_description=readme + '\n\n' + history,
    author="Carol Willing",
    author_email='carolcode@willingconsulting.com',
    url='https://github.com/willingc/circuitpython_kernel',
    packages=[
        'circuitpython_kernel',
    ],
    package_dir={'circuitpython_kernel':
                 'circuitpython_kernel'},
    entry_points={
        'console_scripts': [
            'circuitpython_kernel=circuitpython_kernel.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='circuitpython_kernel',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
