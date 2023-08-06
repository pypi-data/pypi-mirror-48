#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools,os

with open("README.md", "r") as fh:
    long_description = fh.read()
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setuptools.setup(
    name="wappalyze",
    version="1.0",
    author="Syed Abuthahir",
    author_email="developerabu@gmail.com",
    description="Framework Identifier tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abuvanth/framework-identifier",
    packages=setuptools.find_packages(),
    package_dir={'wappalyze': 'wappalyze'},
    package_data={'wappalyze': ['app.json']},
    install_requires=install_requires,
    scripts=['wappalyze/wappalyze.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
