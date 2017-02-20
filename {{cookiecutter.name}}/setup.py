#!/usr/bin/env python
# coding: utf-8

import sys

from {{cookiecutter.name}} import __version__

if sys.version_info < (2, 7) or sys.version_info.major > 2:
    print("siskin runs with Python 2.7 or higher, but not with Python 3 yet")
    sys.exit(1)

try:
    from setuptools import setup
except:
    from distutils.core import setup

install_requires = [
    # As soon as https://github.com/spotify/luigi/pull/2033 is merged,
    # use 'luigi>=2.2' again.
    'luigi==2.5.0',
    'gluish>=0.2.7',
]

setup(name='{{ cookiecutter.name }}',
      version=__version__,
      description='Data Pipelines.',
      author='{{ cookiecutter.author }}',
      author_email='{{ cookiecutter.author_email }}',
      packages=[
          '{{ cookiecutter.name }}',
      ],
      package_dir={'{{ cookiecutter.name }}': '{{ cookiecutter.name }}'},
      package_data={'{{ cookiecutter.name }}': ['assets/*']},
      scripts=[
          'bin/{{ cookiecutter.name }}-build',
          'bin/{{ cookiecutter.name }}-ls',
          'bin/{{ cookiecutter.name }}-output',
          'bin/{{ cookiecutter.name }}-rm',
      ],
      install_requires=install_requires,
      zip_safe=False,
      )
