# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in lifelineamb/__init__.py
from lifelineamb import __version__ as version

setup(
	name='lifelineamb',
	version=version,
	description='Website for LifeLine Ambulance',
	author='4C Solutions',
	author_email='4csolutions.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
