#!/usr/bin/env python

import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    orig_content = open(os.path.join(os.path.dirname(__file__), fname)).readlines()
    content = ""
    in_raw_directive = 0
    for line in orig_content:
        if in_raw_directive:
            if not line.strip():
                in_raw_directive = in_raw_directive - 1
            continue
        elif line.strip() == '.. raw:: latex':
            in_raw_directive = 2
            continue
        content += line
    return content


# wui_requires = ['bokeh']
wui_requires = []

setup(
    name="fpvgcc",
    use_scm_version={"root": ".", "relative_to": __file__},
    author="Chintalagiri Shashank",
    author_email="shashank@chintal.in",
    description="Analysing code footprint on embedded microcontrollers "
                "using GCC generated Map files",
    long_description=read('README.rst'),
    license="GPLv3+",
    keywords="utilities",
    url="https://github.com/chintal/fpv-gcc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Embedded Systems",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Environment :: Console"
    ],
    install_requires=[
        'six',
        'wheel',
        'prettytable',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    extras_require={
        'docs': [
            'sphinx',
            'sphinx-argparse',
            'alabaster',
        ],
        'wui': wui_requires,
        'build': [
            'doit',
            'setuptools_scm',
            'wheel',
            'twine',
            'pygithub',
            'pyinstaller'
        ]
    },
    platforms='any',
    entry_points={
        'console_scripts': ['fpvgcc=fpvgcc.cli:main'],
    },
    include_package_data=True
)
