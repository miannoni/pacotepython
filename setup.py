#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_matteo',
      version='0.1.1',
      author="Matteo Iannoni",
      author_email='matteoi@al.insper.edu.br',
      packages=['dev_aberto'],
      install_requires=[
        'requests'
      ],
      scripts=['scripts/hello.py'],
      license='LICENSE',
      description='Pacote mais legal dos 7 mares'
      )
