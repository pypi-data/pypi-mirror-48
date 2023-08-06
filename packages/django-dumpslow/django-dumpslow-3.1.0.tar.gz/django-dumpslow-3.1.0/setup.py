#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# django-dumpslow -- Django application to log and summarize slow requests
#                    <http://chris-lamb.co.uk/projects/django-dumpslow>
#
# Copyright © 2009-2019 Chris Lamb <chris@chris-lamb.co.uk>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.

setup_args = dict(
    name='django-dumpslow',
    version='3.1.0',
    license='BSD-2-Clause',
    url='https://chris-lamb.co.uk/projects/django-dumpslow',
    packages=(
        'django_dumpslow',
        'django_dumpslow.management',
        'django_dumpslow.management.commands',
    ),
    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
    description="Django application to log and summarize slow requests",

    install_requires=(
        'Django>=1.11',
        'redis>=3.0',
        'tabulate',
    ),
)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)
