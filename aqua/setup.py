from os import path
from setuptools import setup, find_packages

from aqua import __version__


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split('\n')

with open(path.join(here, 'README.md')) as f:
    readme = f.read()

setup(
    name='aqua',
    version=__version__,
    description='A library and server for controlling HPLC systems',
    long_description=readme,
    author='Liam Marshall',
    author_email='limarshall@wisc.edu',
    license='Apache',
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(exclude=['test*']),
    install_requires=requirements)
