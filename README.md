# IBK for Maya

    Tool python script for animation object in Maya.

## About

    . This script is to create in-between key from 1st frame with second frame.

    . Slider is for slide percentage value from 0% till 100% from two keyframe.

    . While each button are represent in-between value from 0% till 100% from two keyframe.

## Usage

    1. install/extract IBK folder to:
        . Linux     = $HOME/maya/scripts
        . Windows   = Documents/maya/scripts
        . MacOS     = $HOME/Library/Preferences/Autodesk/maya/scripts

    2. Load IBK in Maya:
        . Select your shelf
        . Hover to Python command line/open script editor and type:
            code:
                from IBK import install
        . If you already installed IBK and want to install it again on another shelf type:
            code:
                from IBK import install
                reload(install)
