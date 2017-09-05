# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='mhs5200',
      version='0.1',
      description='Python module for controlling inexpensive MHS-5200 signal generators.',
      url='https://github.com/jed-frey/python_mhs5200',
      author='Jed Frey',
      license='BSD',
      packages=['mhs5200'],
      setup_requires=[
              'pytest-runner',
              'pyserial',
      ],
      tests_require=[
          'pytest',
          'pytest-html',
          'pytest-flake8',
      ],
      zip_safe=False,
      )
