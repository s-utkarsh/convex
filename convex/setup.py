#! /usr/bin/python 

from setuptools import setup


with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='Convex',
    version='0.1',
    packages=['Convex'],
    url='github.com/s-utkarsh/convex',
    license='MIT',
    author='Utkarsh Singh',
    author_email='usingh1@ch.iitr.ac.in',
    description='A python implementation of calculating the convex hull in context of ternary phase diagrams.',
    install_requires=['numpy', 'matplotlib', 'plotly']
)
