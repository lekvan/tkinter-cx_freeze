from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
	base = "Win32GUI"

includes      = ["tkinter"]
include_files = [r"C:\\Python\\DLLs\\tcl86t.dll",
                 r"C:\\Python\\DLLs\\tk86t.dll"]

setup(
    name = "NAME",
    version = "1.0",
    options = {"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [Executable("NAME.py", base=base)]
    )