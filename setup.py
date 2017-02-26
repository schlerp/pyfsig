#!/usr/bin/env python

from distutils.core import setup

setup(name='pyfsig',
      version='0.1',
      description='File signatures and tools to help work out the type of file from the magic bytes (file header).',
      author='schlerp',
      author_email='schlerpderpson@gmail.com',
      url='https://github.com/schlerp/pyfsig',
      packages=['pyfsig'],
      package_dir={'pyfsig': 'src/pyfsig'},
      classifiers=['Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   ],
      )