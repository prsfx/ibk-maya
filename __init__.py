# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


MayaVer     = int(cmds.about(api=True))


def MayaApiVersion():
    return int(cmds.about(api=True))


if MayaApiVersion() < 20170000:
    print("Soft warning: This version is not supported.")
    print("Your version: " + str(MayaVer) + "\n")

elif MayaApiVersion() <= 20200500:
    from IBK import ibk
    reload(ibk)
    ibk.main()


elif MayaApiVersion() > 20200500:
    print("It's about time to use Python 3?")
    print("Your version: " + str(MayaVer) + "\n")

else:
    print("This is absurd.")
