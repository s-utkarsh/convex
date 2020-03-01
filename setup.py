#! /usr/bin/python 

import os
from setuptools import setup

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='convex',
    version='0.1',
    packages=['convex'],
    url='http://github.com/s-utkarsh/convex',
    license='MIT',
    author='Utkarsh Singh',
    author_email='usingh1@ch.iitr.ac.in',
    description='A python implementation of calculating the convex hull in context of ternary phase diagrams.',
    install_requires=['numpy', 'matplotlib', 'plotly']
    long_description=read('README')
)
