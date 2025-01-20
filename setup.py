# -*- coding: utf-8 -*-
# Copyright (c) 2022 pyetlxML authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import setuptools

with open('./README.md', mode = 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

version = 'dev'
if os.environ.get('BUILD_VERSION') is not None:
    version = os.environ.get('BUILD_VERSION')

setuptools.setup(
    name='pyetlx',
    version=version,
    author='realdatadriven',
    author_email='real.datadriven@gmail.com',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/realdatadriven/pypyetlx',
    project_urls={
        'Documentation': 'https://github.com/realdatadriven/pypyetlx',
        'Source': 'https://github.com/realdatadriven/pypyetlx',
        'Tracker': 'https://github.com/realdatadriven/pypyetlx/issues',
    },
    packages=setuptools.find_packages(exclude='_test'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    install_requires=[
        'pandas',
    ],
    py_modules=['pyetlx'],
    zip_safe=False,

    python_requires='>=3.7, <4'
)
