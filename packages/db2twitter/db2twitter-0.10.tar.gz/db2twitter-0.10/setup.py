# -*- coding: utf-8 -*-
# Copyright © 2015-2017 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Setup for db2twitter
'''Setup for db2twitter'''

# 3rd party libraries imports
from setuptools import setup, find_packages

CLASSIFIERS = [
    'Intended Audience :: End Users/Desktop',
    'Environment :: Console',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='db2twitter',
    version='0.10',
    license='GNU GPL v3',
    description='extract info from a database and send it to twitter',
    long_description='extract information from a database, write a tweet with them and send this tweet',
    classifiers=CLASSIFIERS,
    author='Carl Chenet',
    author_email='chaica@ohmytux.com',
    url='https://gitlab.com/chaica/db2twitter',
    download_url='https://gitlab.com/chaica/db2twitter',
    packages=find_packages(),
    scripts=['scripts/db2twitter'],
    install_requires=['redis', 'tweepy', 'sqlalchemy','pillow','Mastodon.py'],
)
