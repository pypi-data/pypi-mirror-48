#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists, dirname, realpath
from setuptools import setup, Extension, find_packages
import sys

# numpy and cython are installed via pyproject.toml [build-system]
import numpy as np

author = u"Paul Müller"
authors = [author]
description = 'Library for real-time deformability cytometry (RT-DC)'
name = 'dclab'
year = "2015"


sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
try:
    from _version import version  # @UnresolvedImport
except:
    version = "unknown"


setup(
    name=name,
    author=author,
    author_email='dev@craban.de',
    url='https://github.com/ZELLMECHANIK-DRESDEN/dclab',
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license="GPL v2",
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    install_requires=["fcswrite>=0.4.1",  # required by: fcs export
                      "h5py>=2.8.0",      # required by: rtdc format
                      "imageio>=2.3.0,<2.5.0",   # required by: tdms format, avi export
                      "nptdms",           # required by: tdms format
                      "numpy>=1.10.0",
                      "pathlib;python_version<='3.4'",
                      "scipy>=0.14.0",
                      ],
    ext_modules = [Extension("dclab.external.skimage._find_contours_cy",
                        sources=["dclab/external/skimage/_find_contours_cy.pyx"],
                        include_dirs=[np.get_include()]
                        )
                   ],
    # not to be confused with definitions in pyproject.toml [build-system]
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "urllib3"],
    entry_points={
       "console_scripts": [
           "dclab-verify-dataset = dclab.cli:verify_dataset",
           "dclab-tdms2rtdc = dclab.cli:tdms2rtdc",
            ],
       },
    keywords=["RT-DC", "deformation", "cytometry", "zellmechanik"],
    classifiers= ['Operating System :: OS Independent',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3.6',
                  'Topic :: Scientific/Engineering :: Visualization',
                  'Intended Audience :: Science/Research',
                  ],
    platforms=['ALL'],
    )
