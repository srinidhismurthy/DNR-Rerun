import cx_Freeze
from cx_Freeze import setup, Executable
import os
import re
# from tkinter import *
# import tkinter
# import io
# from contextlib import redirect_stdout
# import logging
# import inspect
import sys

os.environ["TCL_LIBRARY"] = "C:\\Python36-32\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Python36-32\\tcl\\tk8.6"

base = "Win32GUI"

if sys.platform =='Win32':
    base="Win32GUI"


executables = [Executable("DNR_Masterplan.py", base=base)]

setup(
    name = "QAPSearch-Functions(.inc)",
    options = {'build_exe': {'packages':["tkinter"], "include_files": ["tcl86t.dll", "tk86t.dll"]}},
    version = "1.1",
    description = 'To search all the functions defined in .inc files(in silkframe and SilkScripts folders under QAP folder)',
    executables = executables
)
