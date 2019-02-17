#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from distutils.core import setup

version = "0.1.0b1"

setup(name='aiotuya',
      packages=['aiotuya'],
      version=version,
      author='François Wautier, Max Isom et al.',
      author_email='francois@wautier.eu',
      description='Pure Python library to control Tuya devices',
      url='https://github.com/frawau/aiotuya',
      download_url='https://github.com/frawau/aiotuya/archive/'+version+'.tar.gz',
      platforms=['unix', 'linux', 'osx'],
      license='LGPL',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython'
      ],
      keywords=[
          'Tuya', 'IoT', 'WiFi', 'Home Automation',  'asyncio',
      ],
      install_requires=[
          'colorsys', 'csv'
      ],
      entry_points={
          'console_scripts': [
              'aiotuya=aiotuya.__main__:main'
          ],
      },
      )
