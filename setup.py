#!/usr/bin/env python3
# thoth-common
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup


def get_install_requires():
    with open('requirements.txt', 'r') as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(' ', maxsplit=1)[0] for req in res if req]


def get_version():
    with open(os.path.join('thoth', 'common', '__init__.py')) as f:
        content = f.readlines()

    for line in content:
        if line.startswith('__version__ ='):
            # dirty, remove trailing and leading chars
            return line.split(' = ')[1][1:-2]
    raise ValueError("No version identifier found")


setup(
    name='thoth-common',
    version=get_version(),
    description='Shared code logic in the project Thoth.',
    long_description='Shared code logic in the project Thoth.',
    author='Fridolin Pokorny',
    author_email='fridolin@redhat.com',
    license='GPLv3+',
    packages=[
        'thoth.common',
    ],
    zip_safe=False,
    install_requires=get_install_requires()
)
