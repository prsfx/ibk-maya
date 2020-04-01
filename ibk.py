#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!python2

MajorVersion = "1"
MinorVersion = "0"
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

_PROJECTNAME_   =       "IBK for Maya "
_VERSION_       =       " v" + MajorVersion + "." + MinorVersion + "." + PatchVersion + " " + PreReleaseVersionType

_ABOUT_         =       "© 2020 | Prana Ronita | @prsfx"
_LASTMODIFIED_  =       "2020-April-1"

#----------------------------------------------------------------                               ----------------------------------------------------------------#

"""import modules"""
import os
import ibk
import xml.etree.ElementTree as xml

from config.vendor.LoDb import *
from config.vendor.LoDb import loadUiType
from config.vendor.LoDb import wrapinstance

from cStringIO import StringIO

from maya import mel as mel
from maya import cmds as cmds
from maya import OpenMayaUI as omui

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

#----------------------------------------------------------------                               ----------------------------------------------------------------#

"""decalre and function"""
# primary source path
Source              = os.path.dirname(__file__)

# global for selection command
slctn               = cmds.ls(sl=True)


# look up for Maya main window
def mayaMainWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapinstance(long(main_window_ptr), QtWidgets.QWidget)

# check if it's Maya
def isMaya():
    try:
        import maya.cmds as cmds
        cmds.about(batch=True)
        return True
    except ImportError:
        return Falses


# tweener
def tweenIBK(percentage, slctn=None, attrs=None, selection=True):
    #valChanged = str(self.ibk_horizontalSlider.value())

    if not slctn and not selection:
        raise ValueError("No object selection...")

    if not slctn:
        slctn = cmds.ls(sl=True)[0]

    if not attrs:
        attrs = cmds.listAttr(slctn, keyable=True)

    crtm = cmds.currentTime(q=True)

    for attr in attrs:
        attrFull = "%s.%s" % (slctn, attr)
        keyframes = cmds.keyframe(attrFull, q=True, tds=True)

        if not keyframes:
            continue

        previousKeyframes = []
        for frame in keyframes:
            if frame < crtm:
                previousKeyframes.append(frame)

        laterKeyframes = [frame for frame in keyframes if frame > crtm]

        if not previousKeyframes and not keyframes:
            continue

        if previousKeyframes:
            previousFrame = max(previousKeyframes)
        else:
            previousFrame = None

        nextFrame = min(laterKeyframes) if laterKeyframes else None

        if not previousFrame or not nextFrame:
            continue

        previousValue = cmds.getAttr(attrFull, time=previousFrame)
        nextValue = cmds.getAttr(attrFull, time=nextFrame)

        difference = nextValue - previousValue
        weightedDifference = (float(difference) * float(percentage)) / 100.0
        currentValue = previousValue + weightedDifference

        cmds.setKeyframe(attrFull, time=crtm, value=currentValue)

#----------------------------------------------------------------                               ----------------------------------------------------------------#

"""declare windows/widget name"""
Ibk_WindowName = "IBK-tool"
IbkMixin_DockName = "IBK-tools-dock"

#----------------------------------------------------------------                               ----------------------------------------------------------------#

"""IBK main class"""
# ibk global form
ibk_form, ibk_base = loadUiType(Source + "/ibk_form.ui")

# ibk main class
class ibkUI(ibk_form, ibk_base):
    def __init__(self, parent=None):
        super(ibkUI, self).__init__(parent)

        # setup ui
        self.setupUi(self)

        # value slider
        self.ibk_horizontalSlider.valueChanged.connect(self.__valueIbkInfoChanged)

        # value button
        self.ibk_000_pButton.clicked.connect(self.__000tweenButton)
        self.ibk_010_pButton.clicked.connect(self.__010tweenButton)
        self.ibk_020_pButton.clicked.connect(self.__020tweenButton)
        self.ibk_030_pButton.clicked.connect(self.__030tweenButton)
        self.ibk_040_pButton.clicked.connect(self.__040tweenButton)
        self.ibk_050_pButton.clicked.connect(self.__050tweenButton)
        self.ibk_060_pButton.clicked.connect(self.__060tweenButton)
        self.ibk_070_pButton.clicked.connect(self.__070tweenButton)
        self.ibk_080_pButton.clicked.connect(self.__080tweenButton)
        self.ibk_090_pButton.clicked.connect(self.__090tweenButton)
        self.ibk_100_pButton.clicked.connect(self.__100tweenButton)

    #---------------------------------------------------------------#

    # value slider
    def __valueIbkInfoChanged(self, *args):
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = str(self.ibk_horizontalSlider.value())

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    # value button
    def __000tweenButton(self, *args):
        ValueInput = 0
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __010tweenButton(self, *args):
        ValueInput = 10
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __020tweenButton(self, *args):
        ValueInput = 20
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __030tweenButton(self, *args):
        ValueInput = 30
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __040tweenButton(self, *args):
        ValueInput = 40
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __050tweenButton(self, *args):
        ValueInput = 50
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __060tweenButton(self, *args):
        ValueInput = 60
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __070tweenButton(self, *args):
        ValueInput = 70
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __080tweenButton(self, *args):
        ValueInput = 80
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __090tweenButton(self, *args):
        ValueInput = 90
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    def __100tweenButton(self, *args):
        ValueInput = 100
        CurrentTime = cmds.currentTime(q=True)
        ValueChanged = self.ibk_horizontalSlider.setValue(ValueInput)

        # check how many value will change
        print("Slider value changed... " + ValueChanged +"%")

        tweenIBK(ValueChanged)

        cmds.keyframe(slctn, tds=True, t=(CurrentTime, CurrentTime))

    # close
    def closeEvent(self, *args):
        self.parent().close()

#----------------------------------------------------------------                               ----------------------------------------------------------------#

# ibk mixin class
class ibkToolMixinWindowDock(MayaQWidgetDockableMixin, ibk.ibkUI):

    # tool name to connect instances
    ibkTool_name = Ibk_WindowName

    def __init__(self, parent=None):
        # try delete instance first
        self.deleteInstances()

        super(ibkToolMixinWindowDock, self).__init__(parent)

        # get maya main window
        mayaMainWindow()

        # set window title
        self.setWindowTitle(Ibk_WindowName)

        # set window flags
        self.setWindowFlags(QtCore.Qt.Window)

        # delete dialog
        """
        As with close() , 
        deletes the dialog if the WA_DeleteOnClose flag is set. 
        If the dialog is the application’s main widget, the application terminates. 
        If the dialog is the last window closed, the lastWindowClosed() signal is emitted.
        """
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        #---------------------------------------------------------------#

    # triger delete instances
    def dockCloseEventTriggered(self, *args):
        self.deleteInstances()

    # delete instances inside Maya
    def deleteInstances(self, *args):
        for obj in mayaMainWindow().children():
            if str(type(obj)) == ibkToolMixinWindowDock:
                if obj.widget().objectName() == self.__class__.ibkTool_name:
                    print 'Deleting instance {0}'.format(obj)
                    mayaMainWindow().removeDockWidget(obj)
                    obj.setParent(None)
                    obj.deleteLater()

    # delete maya control workspace
    def deleteControl(self, control):
        if cmds.workspaceControl(control, q=True, exists=True):
            cmds.workspaceControl(control, e=True, close=True)
            cmds.deleteUI(control, control=True)

    # run ibk mixin class
    def run(self):
        # set object name
        self.setObjectName(Ibk_WindowName)

        # workspace control name
        workspaceControlName = self.objectName() + "WorkspaceControl"

        # delete workspace control
        self.deleteControl(workspaceControlName)

        # set dock/undock parameter here
        self.show(dockable=True, area="middle", floating=True)

        # workspace area
        cmds.workspaceControl(workspaceControlName, e=True, wp="preferred", mw=282, mh=60)
       
        # raise to window
        self.raise_()

        # dock it by using this if you need it
        self.setDockableParameters(width=282, height=60)

#----------------------------------------------------------------                               ----------------------------------------------------------------#

"""Launch setup"""
# Maya mixin setup
def launch_ibk():
    ibkMixinWindow = ibkToolMixinWindowDock()
    ibkMixinWindow.run()
    return ibkMixinWindow

# main launcher setup
def main(*args, **kwargs):
    if ibk.isMaya():
        libk = launch_ibk()
    return libk

if __name__ == "__main__":
    with ibk.app():
        ibk.main()
