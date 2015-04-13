#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


try:
    with open('README.md', 'r') as readme:
        LONG_DESCRIPTION = readme.read()
except Exception:
    LONG_DESCRIPTION = None


setup(
    name='python-markdown-bleach',
    version='0.0.8',
    description="Markdown extension to sanitize the raw html within untrusted "
                "markdown sources.",
    long_description=LONG_DESCRIPTION,
    author='Sami Turcotte',
    author_email='samiturcotte@gmail.com',
    url='https://github.com/Wenzil/python-markdown-bleach',
    license='MIT License',
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
    ),
    keywords='markdown bleach',

    packages=[
        'mdx_bleach',
    ],
    install_requires=[
        "bleach >= 1.4.1",
        "Markdown >= 2.6.1",
    ],

)
