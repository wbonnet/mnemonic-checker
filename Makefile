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

#
# Target : init
#
# Description :
#	
#	Install all requirements using PIP
#
init:
	pip install -r requirements.txt

#
# Target : test, tests
#
# Description :
#	
#	Run unit tests
#
tests: test
	
test:
	nosetests