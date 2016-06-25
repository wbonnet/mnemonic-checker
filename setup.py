#
# The contents of this file are subject to the Apache 2.0 license you may not
# use this file except in compliance with the License.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
#
# Copyright 2016 William Bonnet.  
# All rights reserved. Use is subject to license terms.
#
#
# Contributors list :
#
#    William Bonnet     wbonnet@theitmakers.com
#
#

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mnemonic checker for valid instruction according to a given CPU',
    'author': 'William Bonnet',
    'url': 'https://github.com/wbonnet/mnemonic-checker/',
    'download_url': 'https://github.com/wbonnet/mnemonic-checker/',
    'author_email': 'wbonnet@theitmakers.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mnemonic-checker'],
    'scripts': [],
    'name': 'mnemonic-checker'
}

setup(**config)