#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Note: This is only for drag and drop installation to viewport on top shelf or using import method

Python command:
from IBK import install

If above code doesn't works. Please delete prsfxTools shelf if any.
Then use Pythoncommand:
from IBK import install
reload(install)
"""

import os
import sys
import platform
import getpass

try:
    import maya.mel as mel
    import maya.cmds as cmds
    isMaya = True
except ImportError:
    isMaya = False

Ver         = int(cmds.about(api=True))
CheckOS     = platform.system()
CheckUser   = getpass.getuser()
CheckPyVer  = sys.version


def MayaApiVersion():
    return int(cmds.about(api=True))


def onMayaDroppedPythonFile(*args, **kwargs):
    pass

def onMayaDropped():
    if MayaApiVersion() <= 20200500:
        SourcePath      =       os.path.dirname(__file__)
        IconPath        =       SourcePath + "/icons/ibk_icon.png"

        #SourcePath      =       os.path.normpath(SourcePath)
        #IconPath        =       os.path.normpath(IconPath)

        if not os.path.exists(IconPath):
            raise IOError("Can't find " + IconPath)

        for path in sys.path:
            if os.path.exists(path):
                print("IBK already installed at: " + SourcePath)
                pass

        command = """
import IBK
from IBK import main as ibkm
reload(ibkm)
    """.format(path=SourcePath)

        shelf = mel.eval('$gShelfTopLevel=$gShelfTopLevel')
        parent = cmds.tabLayout(shelf, query=True, selectTab=True)
        cmds.shelfButton(
            command     = command,
            iol         = "I.B.K.",
            annotation  = "In-Between Key",
            sourceType  = "Python",
            image       = IconPath,
            image1      = IconPath,
            parent      = parent
        )
    else:
        print("Is it ready for python3?")

if isMaya:
    onMayaDropped()
