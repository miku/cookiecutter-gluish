# coding: utf-8

# star import, so build script only needs to import this
import glob
import os

modules = glob.glob("%s/*.py" % (os.path.dirname(__file__)))
__all__ = [os.path.basename(f)[:-3] for f in modules]
