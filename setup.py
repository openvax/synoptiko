# Copyright (c) 2018. Mount Sinai School of Medicine
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
import re

from setuptools import find_packages, setup

project_name = "synoptiko"
description = "Summary report of somatic mutations from cancer DNA sequencing data"
author = "Alex Rubinsteyn"
author_email = "alex@openvax.org"

project_name_no_dashes = project_name.replace("-", "_")
current_directory = os.path.dirname(__file__)
readme_filename = 'README.md'
readme_path = os.path.join(current_directory, readme_filename)

try:
    with open(readme_path) as f:
        readme_markdown = f.read()
except OSError as e:
    print(e)
    print(f"Failed to open {readme_path}")
    readme_markdown = ""

def parse_field(name):
    with open(f'{project_name_no_dashes}/__init__.py') as f:
        value = re.search(
            rf'^{name}\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(),
            re.MULTILINE).group(1)
    if not value:
        raise RuntimeError(f"Cannot find '{name}' in {project_name}'s __init__.py")
    return value

version = parse_field("__version__")

if not version:
    raise RuntimeError('Cannot find version information')

if __name__ == '__main__':
    setup(
        name=project_name_no_dashes,
        version=version,
        python_requires='>=3.11',
        description=description,
        author=author,
        author_email=author_email,
        url=f"https://github.com/openvax/{project_name}",
        license="http://www.apache.org/licenses/LICENSE-2.0.html",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
        install_requires=open(os.path.join(current_directory, 'requirements.txt')).read().splitlines(),
        extras_require={'test': ['pytest>=8,<10', 'pytest-cov>=5', 'ruff>=0.15']},
        long_description=readme_markdown,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        package_data={"synoptiko": ["*.csv"]},
        include_package_data=True,
        entry_points={
            'console_scripts': [
                'synoptiko = synoptiko.cli:main'
            ]
        }
    )
