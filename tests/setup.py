#!/usr/bin/env python

from setuptools import setup
import glob
import os

datafiles = []
for topdir in ['rhui3_tests']:
    for dirname, dirnames, filenames in os.walk(topdir):
        datafiles.append(('share/rhui3_tests_lib/' + dirname, map(lambda x: dirname + "/" + x, filenames)))

setup(name='rhui3_tests_lib',
    version='1.0',
    description='RHUI3 Testing Library',
    author='Martin Minar',
    author_email='mminar@redhat.com',
    url='https://github.com/RedHatQE/rhui3-automation',
    license="GPLv3+",
    packages=[
        'rhui3_tests_lib'
        ],
    data_files=datafiles,
    classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Operating System :: POSIX',
            'Intended Audience :: Developers',
            'Development Status :: 4 - Beta'
    ],
    scripts=glob.glob('scripts/*.py') + glob.glob('scripts/*.sh')
)

