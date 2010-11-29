"""
The settings package loads appropriate settings for development, testing,
or production deployments based upon the platform hostname and filesystem
directory name when imported.
"""
import os
import platform

# Define environment-dependent settings modules
envSettings = {
    ("donteventryit","/home/darthrayder/dev/"):"local",
    ("newdelhi","/home/robertlray/beta.videoportrait.net/"): "beta",
    ("newdelhi","/home/erikdykema/videoportrait.net/"): "prod",
}

def exitImportError(moduleName):
    """Helper function for exiting upon a settings module import error."""
    import sys
    sys.stderr.write("Unable to import setting module: %s\n",moduleName)
    sys.exit(1)

def loadSettings(moduleName,locals=locals()):
    """Helper function for loading settings attributes from modules."""
    try:
        module = __import__(moduleName,globals(),locals)
    except ImportError:
        exitImportError(moduleName)
    for attrName in dir(module):
       if attrName == attrName.upper():
           locals[attrName] = getattr(module,attrName)

# Load common and environment-dependent project settings
node = platform.node()
loadSettings("common")
loadSettings(envSettings[(node,VIDEOPORTRAIT_ROOT)])
