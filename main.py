#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!python2

MajorVersion = "0"
MinorVersion = "1"
PatchVersion = "0"

PreReleaseVersionType = "m"
PreReleaseVersion     = ""

IBK_LICESE = """
MIT License

Copyright (c) 2020 Prana Ronita

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#----------------------------------------------------------------                               ----------------------------------------------------------------#

_AUTHOR_        =       "Prana Ronita"
_PORTFOLIO_     =       "www.prsfx.net"
_EMAIL_         =       "prana.ronita@gmail.com / prsfx.net@gmail.com"
_SOCIAL_        =       "@prsfx"

_PROJECTNAME_   =       "I.B.K. for Maya "
_VERSION_       =       " v" + MajorVersion + "." + MinorVersion + "." + PatchVersion + " " + PreReleaseVersionType

_ABOUT_         =       "© 2020 | Prana Ronita | @prsfx"
_LASTMODIFIED_  =       "2020-April-1"

#----------------------------------------------------------------                               ----------------------------------------------------------------#

# import modules
import os
import xml.etree.ElementTree as xml

from config.LoDb import *
from config.LoDb import loadUiType
from config.LoDb import wrapinstance
