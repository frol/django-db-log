#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-db-log',
    version='.'.join(map(str, __import__('djangodblog').__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/tutca/django-db-log',
    description = 'Exception Logging to a Database in Django',
    mantainer = u'Matías Iturburu',
    mantainer_email = 'maturburu@gmail.com ',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
