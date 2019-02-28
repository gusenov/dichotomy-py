# -*- coding: utf-8 -*-

import os

currentdir = os.getcwd()

from distutils.core import setup
setup(
  name='dichotomy',
  packages=['dichotomy'],
  version='0.1.1',
  description='Библиотека для работы с операциями деления надвое.',
  author='Аббас Гусенов',
  author_email='gusenov@live.ru',
  license='MIT',
  url='https://github.com/gusenov/dichotomy-py',
  download_url='https://github.com/gusenov/dichotomy-py/archive/v0.1.1.tar.gz',
  keywords='dichotomy division',
  classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Mathematics',
      'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
