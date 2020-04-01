# IBK for Maya

Tool python script for animation object in Maya.

# About

. This script is to create in-between key from 1st frame with second frame.

. Slider is for slide percentage value from 0% till 100% from two keyframe.

. Each button are represent in-between value from 0% till 100% from two keyframe.

# Usage

## Install/extract IBK folder to:

    . Linux     = $HOME/maya/scripts
                  or
                  $HOME/maya/{MayaVERSION}/scripts

    . Windows   = Documents/maya/scripts
                  or
                  Documents/maya/{MayaVERSION}/scripts

    . MacOS     = $HOME/Library/Preferences/Autodesk/maya/scripts
                  HOME/Library/Preferences/Autodesk/maya/{MayaVERSION}/scripts

## Load IBK in Maya:

### 1. Select your shelf

### 2. Hover to Python command line/open script editor and type:

    from IBK import install

### 3. If you already installed IBK and want to install it again on another shelf type:

    from IBK import install
    reload(install)

### 4. Click I.B.K. icon on your shelf.

# Note

    If you download it from github, create "IBK" folder on your Maya version or on your Maya script
