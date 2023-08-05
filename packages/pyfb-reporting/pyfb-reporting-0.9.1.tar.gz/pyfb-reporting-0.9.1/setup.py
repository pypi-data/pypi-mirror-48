#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from pyfb_reporting/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("pyfb_reporting", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pyfb-reporting',
    version=version,
    description="""Reporting application for PyFB project""",
    long_description=readme + '\n\n' + history,
    author='Mathias WOLFF',
    author_email='mathias@celea.org',
    url='https://github.com/mwolff44/pyfb-reporting',
    packages=[
        'pyfb_reporting',
    ],
    include_package_data=True,
    install_requires=[
        "django-model-utils>=2.0",
        "django-extensions>=2.1.3",
        "djangorestframework>=3.7.7",
        "django-crispy-forms>=1.7.0",
        "pyfb-direction>=0.9.0",
        "pyfb-company>=0.9.0",
        "pyfb-endpoint>=0.9.0",
        "pyfb-rating>=0.9.0",
        "pyfb-routing>=0.9.0",
        "pyfb-kamailio>=0.9.0",
        "pyfb-did>=0.9.0",
        "django-partial-index>=0.5.2",
    ],
    license="MIT",
    zip_safe=False,
    keywords='pyfb-reporting',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
