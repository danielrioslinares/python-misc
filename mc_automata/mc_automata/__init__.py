

from contextlib import contextmanager
from collections import namedtuple
from PIL import Image
import re
import time
import warnings
import math
import difflib
import ctypes
from ctypes import windll
from ctypes import wintypes


import win32gui, win32con, win32api, win32process, win32ui
import win32com.client

import pywinauto
from pywinauto.application import Application
from pywinauto.controls.hwndwrapper import DialogWrapper

import mouse, keyboard

import mss

import numpy as np




warnings.simplefilter('ignore')




# Controls defined by (device, code)
default_controls = {
	# Movement
	"Strafe Left" : ("keyboard", "a"),
	"Strafe Right" : ("keyboard", "d"),
	"Walk Backwards" : ("keyboard", "s"),
	"Walk Forwards" : ("keyboard", "w"),
	"Sneak" : ("keyboard", "shift"), # TODO LSHIFT IS NOT DETECTED BY MINECRAFT :(
	"Sprint" : ("keyboard", "ctrl"), # TODO LCTRL IS NOT DETECTED BY MINECRAFT :(
	# Gameplay
	"Attack" : ("mouse", "left"),
	"Pick block" : ("mouse", "middle"),
	"Use Item/Place Block" : ("mouse", "right"),
	"Jump" : ("keyboard", "space"),
	"Drop" : ("keyboard", "q"),
	# Inventory
	"Drop Selected Item" : ("keyboard", "q"),
	"Hotbar Slot 1" : ("keyboard", "1"),
	"Hotbar Slot 2" : ("keyboard", "2"),
	"Hotbar Slot 3" : ("keyboard", "3"),
	"Hotbar Slot 4" : ("keyboard", "4"),
	"Hotbar Slot 5" : ("keyboard", "5"),
	"Hotbar Slot 6" : ("keyboard", "6"),
	"Hotbar Slot 7" : ("keyboard", "7"),
	"Hotbar Slot 8" : ("keyboard", "8"),
	"Hotbar Slot 9" : ("keyboard", "9"),
	"Open/Close Inventory" : ("keyboard", "e"),
	"Swap Item In Hands" : ("keyboard", "f"),
	# Multiplayer
	"Open Chat" : ("keyboard", "t"),
	# Miscellaneous
	"Debug" : ("{F3}", "t"),
}

# Settings
default_settings = {
	"GUI Scale" : 3,
	"Sensitivity" : 1.00,
}

# Font
#	0 means that the pixel doesn't match the color
#	1 means that the pixel does match the color
#	2 means that the pixel shall not match the color
default_font = {
	'0' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,1,1],
		   [1,0,1,0,1],
		   [1,1,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'1' : [[0,0,1,0,0],
		   [0,1,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [1,1,1,1,1],
		   [0,0,0,0,0]],
	'2' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,1,1,0],
		   [0,1,0,0,0],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [0,0,0,0,0]],
	'3' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,1,1,0],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'4' : [[0,0,0,1,1],
		   [0,0,1,0,1],
		   [0,1,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,0,0]],
	'5' : [[1,1,1,1,1],
		   [1,0,0,0,0],
		   [1,1,1,1,0],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'6' : [[0,0,1,1,0],
		   [0,1,0,0,0],
		   [1,0,0,0,0],
		   [1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'7' : [[1,1,1,1,1],
		   [1,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,1,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,0,0,0]],
	'8' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'9' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,1],
		   [0,0,0,1,0],
		   [0,1,1,0,0],
		   [0,0,0,0,0]],
	'/' : [[0,0,0,0,1],
		   [0,0,0,1,0],
		   [0,0,0,1,0],
		   [0,0,1,0,0],
		   [0,1,0,0,0],
		   [0,1,0,0,0],
		   [1,0,0,0,0],
		   [0,0,0,0,0]],
	'-' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,1,1,1,1],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0]],
	'A' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'a' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,1,0],
		   [0,0,0,0,1],
		   [0,1,1,1,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,0]],
	'B' : [[1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [0,0,0,0,0]],
	'b' : [[1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,1,1,0],
		   [1,1,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [0,0,0,0,0]],
	'o' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'C' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'c' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,0],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'D' : [[1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [0,0,0,0,0]],
	'd' : [[0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,1,1,0,1],
		   [1,0,0,1,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,0]],
	'E' : [[1,1,1,1,1],
		   [1,0,0,0,0],
		   [1,1,1,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,1,1,1,1],
		   [0,0,0,0,0]],
	'e' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [1,0,0,0,0],
		   [0,1,1,1,1],
		   [0,0,0,0,0]],
	'F' : [[1,1,1,1,1],
		   [1,0,0,0,0],
		   [1,1,1,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [0,0,0,0,0]],
	'f' : [[0,0,0,1,1],
		   [0,0,1,0,0],
		   [0,1,1,1,1],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,0,0,0]],
	'G' : [[0,1,1,1,1],
		   [1,0,0,0,0],
		   [1,0,0,1,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'g' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,1,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,1],
		   [1,1,1,1,0]],
	'H' : [[1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'h' : [[1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,1,1,0],
		   [1,1,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'J' : [[0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,0]],
	'j' : [[0,0,0,0,1],
		   [0,0,0,0,0],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0]],
	'I' : [[1,1,1],
		   [0,1,0],
		   [0,1,0],
		   [0,1,0],
		   [0,1,0],
		   [0,1,0],
		   [1,1,1],
		   [0,0,0]],
	'i' : [[1],
		   [0],
		   [1],
		   [1],
		   [1],
		   [1],
		   [1],
		   [0]],
	'K' : [[1,0,0,0,0],
		   [1,0,0,0,1],
		   [1,0,0,1,0],
		   [1,1,1,0,0],
		   [1,0,0,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'k' : [[1,0,0,0],
		   [1,0,0,0],
		   [1,0,0,1],
		   [1,0,1,0],
		   [1,1,0,0],
		   [1,0,1,0],
		   [1,0,0,1],
		   [0,0,0,0]],
	'L' : [[1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,1,1,1,1],
		   [0,0,0,0,0]],
	't' : [[0,1,0],
		   [0,1,0],
		   [1,1,1],
		   [0,1,0],
		   [0,1,0],
		   [0,1,0],
		   [0,0,1],
		   [0,0,0]],
	'l' : [[1,0],
		   [1,0],
		   [1,0],
		   [1,0],
		   [1,0],
		   [1,0],
		   [0,1],
		   [0,0]],
	'M' : [[1,0,0,0,1],
		   [1,1,0,1,1],
		   [1,0,1,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'm' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,1,0,1,0],
		   [1,0,1,0,1],
		   [1,0,1,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'N' : [[1,0,0,0,1],
		   [1,1,0,0,1],
		   [1,0,1,0,1],
		   [1,0,0,1,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'n' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'O' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'P' : [[1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [0,0,0,0,0]],
	'p' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,1,1,0],
		   [1,1,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0]],
	'Q' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,1,0],
		   [0,1,1,0,1],
		   [0,0,0,0,0]],
	'q' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,0,1],
		   [1,0,0,1,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1]],
	'R' : [[1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'r' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,1,1,0],
		   [1,1,0,0,1],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [1,0,0,0,0],
		   [0,0,0,0,0]],
	'S' : [[0,1,1,1,1],
		   [1,0,0,0,0],
		   [0,1,1,1,0],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	's' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,1,1,1,1],
		   [1,0,0,0,0],
		   [0,1,1,1,0],
		   [0,0,0,0,1],
		   [1,1,1,1,0],
		   [0,0,0,0,0]],
	'T' : [[1,1,1,1,1],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,0,0,0]],
	'U' : [[1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [0,0,0,0,0]],
	'u' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,0]],
	'V' : [[1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,0,1,0],
		   [0,1,0,1,0],
		   [0,0,1,0,0],
		   [0,0,0,0,0]],
	'v' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,0,1,0],
		   [0,0,1,0,0],
		   [0,0,0,0,0]],
	'W' : [[1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,1,0,1],
		   [1,1,0,1,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'w' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,1,0,1],
		   [1,0,1,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,0]],
	'X' : [[1,0,0,0,1],
		   [0,1,0,1,0],
		   [0,0,1,0,0],
		   [0,1,0,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'x' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,0,0,1],
		   [0,1,0,1,0],
		   [0,0,1,0,0],
		   [0,1,0,1,0],
		   [1,0,0,0,1],
		   [0,0,0,0,0]],
	'Y' : [[1,0,0,0,1],
		   [0,1,0,1,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,0,0,0]],
	'y' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,1],
		   [1,1,1,1,0]],
	'Z' : [[1,1,1,1,1],
		   [0,0,0,0,1],
		   [0,0,0,1,0],
		   [0,0,1,0,0],
		   [0,1,0,0,0],
		   [1,0,0,0,0],
		   [1,1,1,1,1],
		   [0,0,0,0,0]],
	'z' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,1,1,1,1],
		   [0,0,0,1,0],
		   [0,0,1,0,0],
		   [0,1,0,0,0],
		   [1,1,1,1,1],
		   [0,0,0,0,0]],
	'_' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [1,1,1,1,1]],
	'@' : [[0,0,0,0,0,0],
		   [0,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [1,0,1,1,0,1],
		   [1,0,1,0,0,1],
		   [1,0,1,1,1,1],
		   [1,0,0,0,0,0],
		   [0,1,1,1,1,0]],
	'[' : [[1,1,1],
		   [1,0,0],
		   [1,0,0],
		   [1,0,0],
		   [1,0,0],
		   [1,0,0],
		   [1,1,1],
		   [0,0,0]],
	']' : [[1,1,1],
		   [0,0,1],
		   [0,0,1],
		   [0,0,1],
		   [0,0,1],
		   [0,0,1],
		   [1,1,1],
		   [0,0,0]],
	'(' : [[0,0,1],
		   [0,1,0],
		   [1,0,0],
		   [1,0,0],
		   [1,0,0],
		   [0,1,0],
		   [0,0,1],
		   [0,0,0]],
	')' : [[1,0,0],
		   [0,1,0],
		   [0,0,1],
		   [0,0,1],
		   [0,0,1],
		   [0,1,0],
		   [1,0,0],
		   [0,0,0]],
	',' : [[0],
		   [0],
		   [0],
		   [0],
		   [0],
		   [0],
		   [1],
		   [1]],
	':' : [[0],
		   [0],
		   [1],
		   [0],
		   [0],
		   [0],
		   [1],
		   [0]],
	'.' : [[0],
		   [0],
		   [0],
		   [0],
		   [0],
		   [0],
		   [1],
		   [0]],
	'>' : [[1,0,0,0],
		   [0,1,0,0],
		   [0,0,1,0],
		   [0,0,0,1],
		   [0,0,1,0],
		   [0,1,0,0],
		   [1,0,0,0],
		   [0,0,0,0]],
	'<' : [[0,0,0,1],
		   [0,0,1,0],
		   [0,1,0,0],
		   [1,0,0,0],
		   [0,1,0,0],
		   [0,0,1,0],
		   [0,0,0,1],
		   [0,0,0,0]],
	' ' : [[0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0]],
}

#
default_inventory_grid_slot_number = {
	'0' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,1,1],
		   [1,0,1,0,1],
		   [1,1,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,1,0,0,0]],
	'1' : [[0,0,1,0,0],
		   [0,1,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [1,1,1,1,1],
		   [1,0,0,0,0]],
	'2' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,1,1,0],
		   [0,1,0,0,0],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [1,0,0,0,0]],
	'3' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,1,1,0],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,1,0,0,0]],
	'4' : [[0,0,0,1,1],
		   [0,0,1,0,1],
		   [0,1,0,0,1],
		   [1,0,0,0,1],
		   [1,1,1,1,1],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [1,1,1,1,1]],
	'5' : [[1,1,1,1,1],
		   [1,0,0,0,0],
		   [1,1,1,1,0],
		   [0,0,0,0,1],
		   [0,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,1,0,0,0]],
	'6' : [[0,0,1,1,0],
		   [0,1,0,0,0],
		   [1,0,0,0,0],
		   [1,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,1,0,0,0]],
	'7' : [[1,1,1,1,1],
		   [1,0,0,0,1],
		   [0,0,0,0,1],
		   [0,0,0,1,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [0,0,1,0,0],
		   [1,1,1,0,1]],
	'8' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,0],
		   [1,1,0,0,0]],
	'9' : [[0,1,1,1,0],
		   [1,0,0,0,1],
		   [1,0,0,0,1],
		   [0,1,1,1,1],
		   [0,0,0,0,1],
		   [0,0,0,1,0],
		   [0,1,1,0,0],
		   [1,1,0,0,1]],
}

# Sprites minimized to single colored pixels
default_sprites = {
	# Health bar (only red color 255 19 19 to treat it as a char)
	'❤2' : [[0,1,1,0,1,1,0],
		     [1,0,1,1,1,1,1],
		     [1,1,1,1,1,1,1],
		     [0,1,1,1,1,1,0],
		     [0,0,1,1,1,0,0],
		     [0,0,0,1,0,0,0],
		     [0,0,0,0,0,0,0],
		     [0,0,0,0,0,0,0]],
	'❤1' : [[0,1,1,0,0,0,0],
		     [1,0,1,1,0,0,0],
		     [1,1,1,1,0,0,0],
		     [0,1,1,1,0,0,0],
		     [0,0,1,1,0,0,0],
		     [0,0,0,1,0,0,0],
		     [0,0,0,0,0,0,0],
		     [0,0,0,0,0,0,0]],
	'♨2' : [[0,1,0], # Only the 4 pixel right next to the bone
		     [1,0,1],
		     [0,1,0],
		     [0,0,0],
		     [0,0,0],
		     [0,0,0],
		     [0,0,0],
		     [0,0,0]],
	'♨1' : [[0,0], # Idem
		     [1,0],
		     [0,1],
		     [0,0],
		     [0,0],
		     [0,0],
		     [0,0],
		     [0,0]],
}

# Durability Sprites
default_durability_sprites = {
	'1' : [ [1] ],
}

# Durability colors
default_durability_colors = [[0,255,1, "~12"],[0,255,17, "~12"],[0,255,51, "~12"],[0,255,69, "~12"],[0,255,112, "~12"],[0,255,146, "~12"],[0,255,181, "~12"],[0,255,216, "~12"],[0,250,255, "~12"],[0,207,255, "~12"],[0,172,255, "~12"],[0,129,255, "~12"],[0,86,255, "~12"],[0,60,255, "~12"],[0,51,255, "~12"]]


#
class MinecraftAFKSubstitute(object):

	# Minecraft released versions
	VERSIONS = {
		"1.14" : {
			# General
			"Window Title" : "Minecraft 1.14.1",
			"Character settings" : {
				"Odometry sneak speed" : 1.310, # m/s
				"Odometry walk speed" : 4.317, # m/s
				"Odometry sprint speed" : 5.612, # m/s
			},
			"World information" : {
				# Debug left side bounds
				"XYZ" : {"top" : 83, "left" : 26, "width" : 200, "height" : 8, "position" : "left", "colors" : [[224,224,224, "=="]], "font" : default_font},
				"YP" : {"top" : 110, "left" : 150, "width" : 200, "height" : 8, "position" : "left", "colors" : [[224,224,224, "=="]], "font" : default_font},
				"Biome" : {"top" : 137, "left" : 34, "width" : 200, "height" : 8, "position" : "left", "colors" : [[224,224,224, "=="]], "font" : default_font},
				"Looking at Block" : {"top" : 173, "left" : 89, "width" : 200, "height" : 8, "position" : "left", "colors" : [[224,224,224, "=="]], "font" : default_font},
				"Server Light" : {"top" : 128, "left" : 72, "width" : 90, "height" : 8, "position" : "left", "colors" : [[224,224,224, "=="]], "font" : default_font},
				# Debug right side bounds
				"Targeted Block (isAvailable?)" : {"top" : 92, "left" : -78, "width" : 77, "height" : 8, "position" : "right", "colors" : [[224,224,224, "=="]], "font" : default_font},
				"Targeted Block" : {"top" : 101, "left" : -230, "width" : 230, "height" : 8, "position" : "right", "colors" : [[224,224,224, "=="]], "font" : default_font}, # Biggest possible block to look at : "minecraft:heavy_weighted_pressure_plate"
				# Sounds
				"Subtitles list" : {
					i : {"top" : 34-i*9, "left" : -120, "width" : 120, "height" : 8, "position" : "bottom right", "colors" : [[200,200,200,">"]], "font" : default_font} for i in range(9)
					}
			},
			"Character information" : {
				# Sprites
				"Health bar" : {"top" : 39, "left" : -90, "width" : 85, "height" : 8, "position" : "bottom centre", "colors" : [[19,19,255, "=="]], "font" : default_sprites},
				"Hungry bar" : {"top" : 39, "left" : +11, "width" : 85, "height" : 8, "position" : "bottom centre", "colors" : [[42,42,212, "=="]], "font" : default_sprites},
				# Misc
				"Experience" : {"top" : 36, "left" : -11, "width" : 22, "height" : 8, "position" : "bottom centre", "colors" : [[32,255,128, "=="]], "font" : default_font}, # Not more than 9999 leves :( hope you understand it
			},
			"UI overlay" : {
				# Player inventory
				"Inventory (recipe on) string Crafting" : {"top" : -75, "left" : 86, "width" : 42, "height" : 8, "position" : "centre", "colors" : [[64,64,64, "=="]], "font" : default_font}, # In the inventory the word Crafting when the recipe UI is off
				"Inventory (recipe off) string Crafting" : {"top" : -75, "left" : 9, "width" : 42, "height" : 8, "position" : "centre", "colors" : [[64,64,64, "=="]], "font" : default_font}, # In the inventory the word Crafting when the recipe UI is off
				"Inventory (recipe on) slot list of amount" : {# Maxed out at 99
					-106 : {"top" : -12, "left" : 71, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number},
					**{100+i : {"top" : -12-18*(i % 4), "left" : 2, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(4)},
					**{i : {"top" : 68+18*(i // 9), "left" : 2+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					**{i+9 : {"top" : 10+18*(i // 9), "left" : 2+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(27)},
					**{i+80 : {"top" : -56+18*(i // 2), "left" : 92+18*(i % 2), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(4)},
					85 : {"top" : -46, "left" : 149, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number},
					},
				"Inventory (recipe off) slot list of amount" : {# Maxed out at 99
					-106 : {"top" : -12, "left" : 71-77, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number},
					**{100+i : {"top" : -12-18*(i % 4), "left" : 2-77, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(4)},
					**{i : {"top" : 68+18*(i // 9), "left" : 2-77+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					**{i+9 : {"top" : 10+18*(i // 9), "left" : 2-77+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(27)},
					**{i+80 : {"top" : -56+18*(i // 2), "left" : 92-77+18*(i % 2), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(4)},
					85 : {"top" : -46, "left" : 149-77, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number},
					},
				"Inventory (recipe on) slot list of durability" : {
					-106 : {"top" : -12+4, "left" : 71-3, "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites},
					**{100+i : {"top" : -12+4-18*(i % 4), "left" : 2-3, "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(4)},
					**{i : {"top" : 68+4+18*(i // 9), "left" : 2-3+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(9)},
					**{i+9 : {"top" : 10+4+18*(i // 9), "left" : 2-3+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(27)},
					**{i+80 : {"top" : -56+4+18*(i // 2), "left" : 92-3+18*(i % 2), "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(4)},
					85 : {"top" : -46+4, "left" : 149-3, "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites},
					},
				"Inventory (recipe off) slot list of durability" : {
					-106 : {"top" : -12+4, "left" : 71-77-3, "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites},
					**{100+i : {"top" : -12+4-18*(i % 4), "left" : 2-77-3, "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(4)},
					**{i : {"top" : 68+4+18*(i // 9), "left" : 2-77-3+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(9)},
					**{i+9 : {"top" : 10+4+18*(i // 9), "left" : 2-77-3+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(27)},
					**{i+80 : {"top" : -56+4+18*(i // 2), "left" : 92-77-3+18*(i % 2), "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites} for i in range(4)},
					85 : {"top" : -46+4, "left" : 149-77-3, "width" : 14, "height" : 1, "position" : "centre", "colors" : [[0,255,1, "=="],[0,255,17, "=="],[0,255,51, "=="],[0,255,69, "=="],[0,255,112, "=="],[0,255,146, "=="],[0,255,181, "=="],[0,255,216, "=="],[0,250,255, "=="],[0,207,255, "=="],[0,172,255, "=="],[0,129,255, "=="],[0,86,255, "=="],[0,60,255, "=="],[0,51,255, "=="]], "font" : default_durability_sprites},
					},
				"Inventory (recipe on) slot list of items" : {
					-106 : {"top" : -12-12, "left" : 71+12, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					**{100+i : {"top" : -12-12-18*(i % 4), "left" : 2+12, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					**{i : {"top" : 68-12+18*(i // 9), "left" : 2+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+80 : {"top" : -56-12+18*(i // 2), "left" : 92+12+18*(i % 2), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					85 : {"top" : -46-12, "left" : 149+12, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Inventory (recipe off) slot list of items" : {
					-106 : {"top" : -12-12, "left" : 71+12-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					**{100+i : {"top" : -12-12-18*(i % 4), "left" : 2+12-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					**{i : {"top" : 68-12+18*(i // 9), "left" : 2+12+18*(i % 9)-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2+12+18*(i % 9)-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+80 : {"top" : -56-12+18*(i // 2), "left" : 92+12+18*(i % 2)-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					85 : {"top" : -46-12, "left" : 149+12-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Inventory (recipe on, inverted) slot list of items" : {
					-106 : {"top" : -12-12, "left" : 71+12-18-220, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					**{100+i : {"top" : -12-12-18*(i % 4), "left" : 2+12-18-220, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					**{i : {"top" : 68-12+18*(i // 9), "left" : 2+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+80 : {"top" : -56-12+18*(i // 2), "left" : 92+12-18-220+18*(i % 2), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					85 : {"top" : -46-12, "left" : 149+12-18-220, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Inventory (recipe off, inverted) slot list of items" : {
					-106 : {"top" : -12-12, "left" : 71+12-18-220-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					**{100+i : {"top" : -12-12-18*(i % 4), "left" : 2+12-18-220-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					**{i : {"top" : 68-12+18*(i // 9), "left" : 2+12-18-220-77+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2+12-18-220-77+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+80 : {"top" : -56-12+18*(i // 2), "left" : 92+12-18-220-77+18*(i % 2), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(4)},
					85 : {"top" : -46-12, "left" : 149+12-18-220-77, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				# Crafting table
				"Crafting table (recipe on) string Crafting" : {"top" : -75-2, "left" : 86-69, "width" : 42, "height" : 8, "position" : "centre", "colors" : [[64,64,64, "=="]], "font" : default_font}, # In the inventory the word Crafting when the recipe UI is off
				"Crafting table (recipe off) string Crafting" : {"top" : -75-2, "left" : 9-69, "width" : 42, "height" : 8, "position" : "centre", "colors" : [[64,64,64, "=="]], "font" : default_font}, # In the inventory the word Crafting when the recipe UI is off
				"Crafting table (recipe on) slot list of amount" : {# Maxed out at 99
					**{i+37 : {"top" : 68+18*(i // 9), "left" : 2+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					**{i+10 : {"top" : 10+18*(i // 9), "left" : 2+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(27)},
					**{i+1 : {"top" : -12-45+18*(i // 3), "left" : 71-47+18*(i % 3), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					0 : {"top" : -12-27, "left" : 71+49, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Crafting table (recipe off) slot list of amount" : {# Maxed out at 99
					**{i+37 : {"top" : 68+18*(i // 9), "left" : 2-77+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					**{i+10 : {"top" : 10+18*(i // 9), "left" : 2-77+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(27)},
					**{i+1 : {"top" : -12-45+18*(i // 3), "left" : 71-77-47+18*(i % 3), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					0 : {"top" : -12-27, "left" : 71-77+49, "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Crafting table (recipe on) slot list of durability" : {
					**{i+37 : {"top" : 68+4+18*(i // 9), "left" : 2-3+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					**{i+10 : {"top" : 10+4+18*(i // 9), "left" : 2-3+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(27)},
					**{i+1 : {"top" : -12+4-45+18*(i // 3), "left" : 71-47-3+18*(i % 3), "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					0 : {"top" : -12+4-27, "left" : 71+49-3, "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites},
					},
				"Crafting table (recipe off) slot list of durability" : {
					**{i+37 : {"top" : 68+4+18*(i // 9), "left" : 2-3-77+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					**{i+10 : {"top" : 10+4+18*(i // 9), "left" : 2-3-77+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(27)},
					**{i+1 : {"top" : -12+4-45+18*(i // 3), "left" : 71-3-77-47+18*(i % 3), "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					0 : {"top" : -12+4-27, "left" : 71-3-77+49, "width" : 14, "height" : 8, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites},
					},
				"Crafting table (recipe on) slot list of items" : {
					**{i+37 : {"top" : 68-12+18*(i // 9), "left" : 2+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+10 : {"top" : 10-12+18*(i // 9), "left" : 2+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+1 : {"top" : -12-12-45+18*(i // 3), "left" : 71+12-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					0 : {"top" : -12-27-12, "left" : 71+12+49, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Crafting table (recipe off) slot list of items" : {
					**{i+37 : {"top" : 68-12+18*(i // 9), "left" : 2-77+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+10 : {"top" : 10-12+18*(i // 9), "left" : 2-77+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+1 : {"top" : -12-12-45+18*(i // 3), "left" : 71-77+12-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					0 : {"top" : -12-12-27, "left" : 71-77+12+49, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Crafting table (recipe on, inverted) slot list of items" : {
					**{i+37 : {"top" : 68-12+18*(i // 9), "left" : 2+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+10 : {"top" : 10-12+18*(i // 9), "left" : 2+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+1 : {"top" : -12-12-45+18*(i // 3), "left" : 71+12-18-220-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					0 : {"top" : -12-27-12, "left" : 71+12-18-220+49, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				"Crafting table (recipe off, inverted) slot list of items" : {
					**{i+37 : {"top" : 68-12+18*(i // 9), "left" : 2-77+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+10 : {"top" : 10-12+18*(i // 9), "left" : 2-77+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i+1 : {"top" : -12-12-45+18*(i // 3), "left" : 71-77+12-18-220-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					0 : {"top" : -12-12-27, "left" : 71-77+12-18-220+49, "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font},
					},
				# Dropper
				"Dropper string Dropper" : {"top" : -75-2, "left" : 9-29, "width" : 43, "height" : 8, "position" : "centre", "colors" : [[64,64,64, "=="]], "font" : default_font}, # In the inventory the word Dropper
				"Dropper slot list of amount" : {# Maxed out at 99
					**{i+36 : {"top" : 68+18*(i // 9), "left" : 2-12-32+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					**{i+9 : {"top" : 10+18*(i // 9), "left" : 2-12-32+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(27)},
					**{i : {"top" : -12-45+18*(i // 3), "left" : 71-12-47-32+18*(i % 3), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					},
				"Dropper slot list of durability" : {
					**{i+36 : {"top" : 68+4+18*(i // 9), "left" : 2-3-12-32+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					**{i+9 : {"top" : 10+4+18*(i // 9), "left" : 2-3-12-32+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(27)},
					**{i : {"top" : -12+4-45+18*(i // 3), "left" : 71-3-12-32-47+18*(i % 3), "width" : 14, "height" : 1, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					},
				"Dropper slot list of items" : {
					**{i+36 : {"top" : 68-12+18*(i // 9), "left" : 2-12-32+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2-12-32+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i : {"top" : -12-12-45+18*(i // 3), "left" : 71-12-32+12-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					},
				"Dropper (inverted) slot list of items" : {
					**{i+36 : {"top" : 68-12+18*(i // 9), "left" : 2-12-32+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2-12-32+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i : {"top" : -12-12-45+18*(i // 3), "left" : 71-12-32+12-18-220-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					},
				# Dispenser
				"Dispenser string Dispenser" : {"top" : -75-2, "left" : 9-29-5, "width" : 54, "height" : 8, "position" : "centre", "colors" : [[64,64,64, "=="]], "font" : default_font}, # In the inventory the word Dispenser
				"Dispenser slot list of amount" : {# Maxed out at 99
					**{i+36 : {"top" : 68+18*(i // 9), "left" : 2-12-32+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					**{i+9 : {"top" : 10+18*(i // 9), "left" : 2-12-32+18*(i % 9), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(27)},
					**{i : {"top" : -12-45+18*(i // 3), "left" : 71-12-47-32+18*(i % 3), "width" : 14, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_inventory_grid_slot_number} for i in range(9)},
					},
				"Dispenser slot list of durability" : {
					**{i+36 : {"top" : 68+4+18*(i // 9), "left" : 2-3-12-32+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					**{i+9 : {"top" : 10+4+18*(i // 9), "left" : 2-3-12-32+18*(i % 9), "width" : 14, "height" : 1, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(27)},
					**{i : {"top" : -12+4-45+18*(i // 3), "left" : 71-3-12-32-47+18*(i % 3), "width" : 14, "height" : 1, "position" : "centre", "colors" : default_durability_colors, "font" : default_durability_sprites} for i in range(9)},
					},
				"Dispenser slot list of items" : {
					**{i+36 : {"top" : 68-12+18*(i // 9), "left" : 2-12-32+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2-12-32+12+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i : {"top" : -12-12-45+18*(i // 3), "left" : 71-12-32+12-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					},
				"Dispenser (inverted) slot list of items" : {
					**{i+36 : {"top" : 68-12+18*(i // 9), "left" : 2-12-32+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					**{i+9 : {"top" : 10-12+18*(i // 9), "left" : 2-12-32+12-18-220+18*(i % 9), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(27)},
					**{i : {"top" : -12-12-45+18*(i // 3), "left" : 71-12-32+12-18-220-47+18*(i % 3), "width" : 220, "height" : 8, "position" : "centre", "colors" : [[255,255,255, "=="]], "font" : default_font} for i in range(9)},
					},
			},
			"Buttons" : {
				"Back to server list" : "mc_automata/assets/server/Back to server list.png",
				"Direct Connect" : "mc_automata/assets/server/Direct Connect.png",
				"Server Address (blink cursor on)" : "mc_automata/assets/server/Server Address (blink cursor on).png",
				"Server Address (blink cursor off)" : "mc_automata/assets/server/Server Address (blink cursor off).png",
				"Join Server" : "mc_automata/assets/server/Join Server.png",
			}

		},
	}


	def __init__(self, version, controls=default_controls, settings=default_settings, _hWnd=None):

		# Configuration
		self.version = version
		self.controls = default_controls
		self.settings = default_settings

		# Window handling
		self._hWnd = _hWnd if _hWnd is not None else win32gui.FindWindow(None, self.VERSIONS[self.version]["Window Title"])
		self._pidWnd = win32process.GetWindowThreadProcessId(self._hWnd)[1]
		self._app = Application().connect(process=self._pidWnd).window(title=self.VERSIONS[self.version]["Window Title"])

		# Player state
		self.shielding = False # Shield activated (slow down)
		self.sneaking = False # Sneaking (slow down)
		self.sprinting = False # Sprinting (speed up)
		self.effects = {
			"Speed" : 0,
			"Slowness" : 0,
			"Haste" : 0,
			"Mining fatigue" : 0,
		}

	############################################################################


	# continue_when_key(key)
	#
	#	@argument <str> key : keyboard stroke required
	#
	#	@description : stop process until a keyboard stroke
	#
	def continue_when_key(self, key):
		keyboard.wait(key)
	############################################################################



	""" [ Raw action commands ] """

	# mouse_move_relative(dx,dy)
	#
	#	@argument <int> dx : horizontal (positive towards right) increment
	#
	#	@argument <int> dy : vertical (positive towards down) increment
	#
	#	@description : move the cursor to dx,dy relative to the current position
	#
	def mouse_move_relative(self, dx, dy):
		mouse._os_mouse.move_relative(dx, dy)
	############################################################################


	# mouse_move_absolute(x,y)
	#
	#	@argument <int> x : horizontal (positive towards right) position
	#
	#	@argument <int> y : vertical (positive towards down) position
	#
	#	@description : move the cursor to x,y inside the client (not from global
	#		coordinates of the screen)
	#
	def mouse_move_absolute(self, x, y):

		# Get the window position
		outter = self._get_window_dimensions()

		# Move the mouse to the target position
		pywinauto.mouse.move(coords=(outter["left"]+x,outter["top"]+y))
	############################################################################


	# TODO
	def type(self, msg):
		self._app.send_chars(msg)
	############################################################################


	# blocked_input()
	#
	#	@description : using the context manager (with statement) it will block
	#		whatever HID input you have so you don't mess with the mouse if you
	#		are planning to use the PC for other stuff while AFK or as a safety
	#		mechanism
	#
	#	@example :
	#		mc = MinecraftAFKSubstitute("1.14")
	#		with mc.blocked_input():
	#			# Move the mouse around
	#
	@contextmanager
	def blocked_input(self):
		# Mouse stuck
		windll.user32.BlockInput(True)

		# Remember x,y
		x,y = win32api.GetCursorPos()

		# Remember active window
		try:
			hWnd = win32gui.GetForegroundWindow()
		except:
			hWnd = win32gui.FindWindow(None, win32api.GetConsoleTitle())

		# Set Minecraft to foreground
		while True:
			try:
				shell = win32com.client.Dispatch("WScript.Shell")
				shell.SendKeys('%')
				win32gui.SetActiveWindow(self._hWnd)
				win32gui.SetForegroundWindow(self._hWnd)
				break
			except:
				self._hWnd = win32gui.FindWindow(None, self.VERSIONS[self.version]["Window Title"])

		try:
			yield self
		finally:

			# Return to x,y
			pywinauto.mouse.move(coords=(x,y))

			# Return focus to active window
			try:
				win32gui.SetActiveWindow(hWnd)
				win32gui.SetForegroundWindow(hWnd)
			except:
				hWnd = win32gui.FindWindow(None, win32api.GetConsoleTitle())
				win32gui.SetActiveWindow(hWnd)
				win32gui.SetForegroundWindow(hWnd)

			# Unblock the input
			windll.user32.BlockInput(False)
	############################################################################


	# press_and_release(control)
	#
	#	@argument <str> control : one of the keys of the dictionary stored in
	#		self.controls
	#
	#	@description : sends a key or mouse single stroke with the control to
	#		the targeted window. DEPRECATED FOR KEYSTROKES (Minecraft could not
	#		realize)
	#
	def press_and_release(self, control):

		# Get the control device (keyboard / mouse) and control action
		device,action = self.controls[control]

		if device == "keyboard":
			if action == "shift":
				keyboard.press_and_release('shift')
			elif action == "control":
				keyboard.press_and_release('ctrl')
			else:
				try: self._app.send_keystrokes(action)
				except: pass
		elif device == "mouse":
			try: self._app.click(button=action)
			except: pass
	############################################################################


	# press(control)
	#
	#	@argument <str> control : one of the keys of the dictionary stored in
	#		self.controls
	#
	#	@description : sends a key or mouse down stroke with the control to the
	#		targeted window
	#
	def press(self, control):

		if control == "Sneak":
			self.sneaking = True
		elif control == "Sprint":
			self.sprinting = True

		device,action = self.controls[control]

		if device == "keyboard":
			if action == "shift":
				keyboard.press('shift')
			elif action == "control":
				keyboard.press('ctrl')
			else:
				try: self._app.send_keystrokes("{" + action + " down}")
				except: pass
		elif device == "mouse":
			try: self._app.press_mouse(button=action)
			except: pass
	############################################################################


	# release(control)
	#
	#	@argument <str> control : one of the keys of the dictionary stored in
	#		self.controls
	#
	#	@description : sends a key or mouse up stroke with the control to the
	#		targeted window
	#
	def release(self, control):

		if control == "Sneak":
			self.sneaking = False
		elif control == "Sprint":
			self.sprinting = False

		device,action = self.controls[control]

		if device == "keyboard":
			if action == "shift":
				keyboard.press_and_release('shift')
			elif action == "control":
				keyboard.press_and_release('ctrl')
			else:
				try: self._app.send_keystrokes("{" + action + " up}")
				except: pass
		elif device == "mouse":
			try: self._app.release_mouse(button=action)
			except: pass
	############################################################################


	""" [ Data extraction (private) ] """

	# PRIVATE
	# _get_window_dimensions()
	#
	#	@description : sends a key or mouse up stroke with the control to the
	#		targeted window
	#
	def _get_window_dimensions(self):

		# Get rectangle and beautify the data
		rect = DialogWrapper(self._hWnd).client_area_rect()
		wndDimensions = {"top" : int(rect.top),
			"left" : int(rect.left),
			"width" : int(rect.right - rect.left),
			"height" : int(rect.bottom - rect.top),
		}

		# Return
		return wndDimensions
	############################################################################


	# PRIVATE
	# _get_GUI_Scale()
	#
	#	@description : returns the pixel perfect scale (usually 1,2,3) from the
	#		automatic scaling of the game and the self.settings
	#
	def _get_GUI_Scale(self):

		dimensions = self._get_window_dimensions()
		resolution = dimensions["width"],dimensions["height"]

		# Detect auto-fit
		if resolution[0] < 640 or resolution[1] < 480:
			max_GUI_Scale = 1
		elif resolution[0] < 960 or resolution[1] < 720:
			max_GUI_Scale = 2
		elif resolution[0] < 1280 or resolution[1] < 960:
			max_GUI_Scale = 3
		else:
			max_GUI_Scale = 4

		# Return it
		if self.settings["GUI Scale"] == "Auto":
			return max_GUI_Scale
		else:
			return min(int(self.settings["GUI Scale"]), max_GUI_Scale)
	############################################################################


	# PRIVATE
	# _parse_crop_screen_from_dimensions(dimensions)
	#
	#	@argument <dict> dimensions : a dictionary structure of a screenshot
	#		screen location (version dependent, see self.__class__.VERSIONS)
	#
	#	@description : returns a dictionary with the fields "top", "left",
	#		"width" and "height" for the screenshot engine
	#
	def _parse_crop_screen_from_dimensions(self, dimensions):
		# Pixel size (real GUI_Scale)
		pixel_size = self._get_GUI_Scale()
		outter = self._get_window_dimensions()

		# Crop
		if dimensions["position"] == "left":
			inner = {
				"top" : outter["top"] + dimensions["top"] * pixel_size,
				"left" : outter["left"] + dimensions["left"] * pixel_size,
				"width" : dimensions["width"] * pixel_size,
				"height" : dimensions["height"] * pixel_size
			}
		elif dimensions["position"] == "right":
			inner = {
				"top" : outter["top"] + dimensions["top"] * pixel_size - 1 *  (not self._app.is_maximized() and outter["width"] % 2 == 0),
				"left" : outter["left"] + outter["width"] + dimensions["left"] * pixel_size - 1 * (not self._app.is_maximized()),
				"width" : dimensions["width"] * pixel_size,
				"height" : dimensions["height"] * pixel_size
			}
		elif dimensions["position"] == "bottom centre":
			inner = {
				"top" : outter["top"] + outter["height"] - dimensions["top"] * pixel_size + 1 * (not self._app.is_maximized()) + 2 * (self._app.is_maximized()),
				"left" : outter["left"] + int(outter["width"] / 2) + dimensions["left"] * pixel_size - 1 *  (not self._app.is_maximized() and outter["width"] % 2 == 0),
				"width" : dimensions["width"] * pixel_size,
				"height" : dimensions["height"] * pixel_size
			}
		elif dimensions["position"] == "centre":
			inner = {
				"top" : outter["top"] + int(outter["height"] / 2) + dimensions["top"] * pixel_size, # TODO
				"left" : outter["left"] + int(outter["width"] / 2) + dimensions["left"] * pixel_size - (not self._app.is_maximized() and outter["width"] % 2 == 0), # TODO
				"width" : dimensions["width"] * pixel_size,
				"height" : dimensions["height"] * pixel_size
			}
		elif dimensions["position"] == "bottom right":
			inner = {
				"top" : outter["top"] + outter["height"] - dimensions["top"] * pixel_size + 2 * (self._app.is_maximized()),
				"left" : outter["left"] + outter["width"] + dimensions["left"] * pixel_size,
				"width" : dimensions["width"] * pixel_size,
				"height" : dimensions["height"] * pixel_size
			}
		return inner
	############################################################################


	# PRIVATE
	# _parse_screenshot_to_string(dimensions)
	#
	#	@argument <dict> dimensions : a dictionary structure of a screenshot
	#		screen location (version dependent, see self.__class__.VERSIONS)
	#
	#	@description : returns a string scanned from the screenshot of the
	#		dimensions structure
	#
	def _parse_screenshot_to_string(self, dimensions):

		with mss.mss() as sct:

			# Pixel size (real GUI_Scale)
			pixel_size = self._get_GUI_Scale()
			outter = self._get_window_dimensions()

			inner = self._parse_crop_screen_from_dimensions(dimensions)

			# Grab the image
			im = sct.grab( inner )
			t = time.time()

			"""
			# Show image (debug)
			img = Image.new("RGB", im.size)
			pixels = zip(im.raw[2::4], im.raw[1::4], im.raw[0::4])
			img.putdata(list(pixels))
			img.show()
			"""

			# Convert to numpy to scan it
			A = np.array(im, dtype=int)

			# Fit the image to get 3x3 pixels layout display
			while A.shape[1] % pixel_size != 0:
				A = np.delete(A, A.shape[1]-1, axis=1)

			# Scale down the image by pixel_size
			width = int(A.shape[1] / pixel_size)
			height = int(A.shape[0] / pixel_size)
			B = [[0 for j in range(width)] for i in range(height)]
			for j in range(width): # Width
				for i in range(height): # Height
					Bij_on = True
					for ii in range(pixel_size):
						for iii in range(pixel_size):
							for color in dimensions["colors"]:
								if color[3] == "==":
									if A[pixel_size*i+ii,pixel_size*j+iii][0] == color[0] and A[pixel_size*i+ii,pixel_size*j+iii][1] == color[1] and A[pixel_size*i+ii,pixel_size*j+iii][2] == color[2]:
										B[i][j] = 1
										break
								elif color[3] == ">":
									if A[pixel_size*i+ii,pixel_size*j+iii][0] > color[0] and A[pixel_size*i+ii,pixel_size*j+iii][1] > color[1] and A[pixel_size*i+ii,pixel_size*j+iii][2] > color[2]:
										B[i][j] = 1
										break
								elif color[3][0] == "~":
									if abs(A[pixel_size*i+ii,pixel_size*j+iii][0] - color[0]) < int(color[3][1:]) and abs(A[pixel_size*i+ii,pixel_size*j+iii][1] - color[1]) < int(color[3][1:]) and abs(A[pixel_size*i+ii,pixel_size*j+iii][2] - color[2]) < int(color[3][1:]):
										B[i][j] = 1
										break
			# Match characters
			output_string = [] # [(index,char),(index,char),...]
			for key,val in dimensions["font"].items():
				char_width = len(val[0])
				char_height = len(val)
				for j in range(width-char_width):
					match = True
					for char_i in range(len(val)):
						for char_j in range(len(val[char_i])):
							if B[char_i][j+char_j] != val[char_i][char_j]:
								match = False

					# If there is a match...
					if match and B[0][j] is not None:
						# ...remember occurrence index...
						output_string.append((j,key))
						# ...and forget that digit...
						for char_i in range(len(val)):
							for char_j in range(len(val[char_i])):
								B[char_i][j+char_j] = None
			# String
			return t,"".join([v for i,v in sorted(output_string, key = lambda tup: tup[0])])
	############################################################################


	""" [ Data extraction ] """

	# get_XYZ()
	#
	#	@description : returns a tuple with the time of the inspection and a
	#		tuple with (x,y,z) coordinates extracted from the debug mode
	#
	def get_XYZ(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["XYZ"] )
		try: xyz = [float(xi) for xi in s.replace(" ","").split("/")]
		except: xyz = [None,None,None]
		return t,xyz
	############################################################################


	# get_YP()
	#
	#	@description : returns a tuple with the time of the inspection and a
	#		tuple with (yaw,pitch) angles extracted from the debug mode
	#
	def get_YP(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["YP"] )
		try: yp = [float(xi) for xi in re.findall('\((.*?)\)', s)[-1].replace(" ","").split("/")]
		except: yp = [None,None]
		return t,yp
	############################################################################


	# get_Biome()
	#
	#	@description : returns a tuple with the time of the inspection and a
	#		string of the current biome extracted from the debug mode
	#
	def get_Biome(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["Biome"] )
		return t,s.rstrip()
	############################################################################


	# get_targetedBlock()
	#
	#	@description : returns a tuple with the time of the inspection, a string
	#		with the targeted block and a tuple with the (x,y,z) position of the
	#		block itself extracted from the debug mode
	#
	def get_targetedBlock(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["Targeted Block (isAvailable?)"] )
		if s == "Targeted Block":
			try:
				_,s1 = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["Targeted Block"] )
				_,s2 = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["Looking at Block"] )
				return t,s1.replace(" ",""),[float(xi) for xi in s2.split(" ")[:3]]
			except:
				return t,None,None
		else:
			return t,None,None
	############################################################################


	# get_serverLight()
	#
	#	@description : returns a tuple with the time of the inspection, the sky
	#		light and the block light extracted from the debug mode
	#
	def get_serverLight(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["Server Light"] )
		try:
			s,b = re.findall('\((.*?)\)', s)[0].split(",")
			return t,int(s[:-4]),int(b[:-6])
		except:
			return t,None,None
	############################################################################


	# get_experience()
	#
	#	@description : returns a tuple with the time of the inspection and the
	#		experience (1-999) of the player extracted from the hotbar
	#
	def get_experience(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["Character information"]["Experience"] )
		try: return t,float(s)
		except: return t,None
	############################################################################


	# get_health()
	#
	#	@description : returns a tuple with the time of the inspection and the
	#		health (0-20) of the player extracted from the hotbar
	#
	def get_health(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["Character information"]["Health bar"] )
		try: return t,eval("+".join(list(s.replace("❤",""))))
		except: t,None
	############################################################################


	# get_experience()
	#
	#	@description : returns a tuple with the time of the inspection and the
	#		hungry bar (0-20) of the player extracted from the hotbar
	#
	def get_hungry(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["Character information"]["Hungry bar"] )
		try: return t,eval("+".join(list(s.replace("♨",""))))
		except: t,None
	############################################################################


	# get_speed()
	#
	#	@description : returns a tuple with the time of the inspection, the
	#		absolute speed and a tuple with the (vx,vy,vz) components of the
	#		player extracted from the self.get_XYZ method
	#
	def get_speed(self):
		tm = time.time()
		t_1,xyz_1 = self.get_XYZ()
		t_2,xyz_2 = self.get_XYZ()
		x_1,y_1,z_1 = xyz_1
		x_2,y_2,z_2 = xyz_2
		try:
			v_x,v_y,v_z = (x_2-x_1) / (t_2-t_1), (y_2-y_1) / (t_2-t_1), (z_2-z_1) / (t_2-t_1)
			v = (v_x**2 + v_y**2 + v_z**2)**0.5
			return tm, v, (v_x, v_y, v_z)
		except:
			return tm, None, (None, None, None)
	############################################################################


	# get_subtitles(i)
	#
	#	@arguemnt <int> i : slot, 0 is the bottommost and 9 is the highest
	#		possible
	#
	#	@description : returns a tuple with the time of the inspection and the
	#		sound message extracted from the UI
	#
	def get_subtitles(self, i):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["World information"]["Subtitles list"][i] )
		try: return t,s.lstrip().rstrip()
		except: return t,None
	############################################################################


	# are_inventory_and_recipe_open()
	#
	#	@description : returns a tuple with the time of the inspection, a bool
	#		with the inventory_open and a bool with the recipe_open
	#
	def are_inventory_and_recipe_open(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe on) string Crafting"] )
		# OLD VERSION, FAULTY WHEN CURSOR ON TOP if s == "Crafting": return t,True,True
		if difflib.SequenceMatcher(None, s, "Crafting").ratio(): return t,True,True
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe off) string Crafting"] )
		if difflib.SequenceMatcher(None, s, "Crafting").ratio(): return t,True,False
		# OLD VERSION, FAULTY WHEN CURSOR ON TOP if s == "Crafting": return t,True,False
		return t,False,False
	############################################################################


	# are_crafting_table_and_recipe_open()
	#
	#	@description : returns a tuple with the time of the inspection, a bool
	#		with the inventory_open and a bool with the recipe_open TODo
	#
	def are_crafting_table_and_recipe_open(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe on) string Crafting"] )
		# OLD VERSION, FAULTY WHEN CURSOR ON TOP if s == "Crafting": return t,True,True
		if difflib.SequenceMatcher(None, s, "Crafting").ratio(): return t,True,True
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe off) string Crafting"] )
		if difflib.SequenceMatcher(None, s, "Crafting").ratio(): return t,True,False
		# OLD VERSION, FAULTY WHEN CURSOR ON TOP if s == "Crafting": return t,True,False
		return t,False,False
	############################################################################


	# is_dropper_open()
	#
	#	@description : returns a tuple with the time of the inspection and a
	#		bool with the inventory_open
	#
	def is_dropper_open(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dropper string Dropper"] )
		if s == "Dropper":
			return t,True
		else:
			return t,False
	############################################################################


	# is_dispenser_open()
	#
	#	@description : returns a tuple with the time of the inspection and a
	#		bool with the inventory_open
	#
	def is_dispenser_open(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dispenser string Dispenser"] )
		if s == "Dispenser":
			return t,True
		else:
			return t,False
	############################################################################


	# is_chest_open()
	#
	#	@description : returns a tuple with the time of the inspection and a
	#		bool with the inventory_open
	#
	def is_chest_open(self):
		t,s = self._parse_screenshot_to_string( MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Chest string Chest"] )
		if s == "Chest":
			return t,True
		else:
			return t,False
	############################################################################


	# get_inventory_slot(i)
	#
	#	@argument <int> i : slot number from the following layout:
	#		[103]             Crafting
	#		[102]		      [80][81]
	#		[101]             [83][84] -> [85*]
	#		[100]		[-106]
	#		[09][10][11][12][13][14][15][16][17]
	#		[18][19][20][21][22][23][24][25][26]
	#		[27][28][29][30][31][32][33][34][35]
	#		------------------------------------
	#		[00][01][02][03][04][05][06][07][08]
	#
	#	@description : returns a tuple with the time of the inspection, a string
	#		with the name of the item and an int with the number of items in the
	#		stack
	#
	def get_inventory_slot(self, i):
		outter = self._get_window_dimensions()
		pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))
		t,inventory_open,recipe_open = self.are_inventory_and_recipe_open()
		old_x,old_y = win32api.GetCursorPos()
		pywinauto.mouse.move(coords=(old_x,old_y))
		if inventory_open:
			if recipe_open:
				dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe on) slot list of amount"][i]
			else:
				dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe off) slot list of amount"][i]

			outter = self._get_window_dimensions()

			old_x,old_y = win32api.GetCursorPos()

			pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))

			t,s = self._parse_screenshot_to_string( dimensions )

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			if recipe_open:
				dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe on) slot list of durability"][i]
			else:
				dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe off) slot list of durability"][i]


			t,s3 = self._parse_screenshot_to_string( dimensions3 )
			try: s3 = sum([int(i) for i in s3])
			except: s3 = 0

			pywinauto.mouse.move(coords=(inner["left"],inner["top"]))

			if recipe_open:
				dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe on) slot list of items"][i]
				dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe on, inverted) slot list of items"][i]
			else:
				dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe off) slot list of items"][i]
				dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe off, inverted) slot list of items"][i]

			t,s2 = self._parse_screenshot_to_string( dimensions2 )
			s2 = s2.rstrip()
			if s2 == "":
				t,s2 = self._parse_screenshot_to_string( dimensions2_inv )
			s2 = s2.lstrip().rstrip()

			pywinauto.mouse.move(coords=(old_x,old_y))


			try: return t,s2,int(s),None
			except:
				if s2 == "":
					return t,None,None,None
				else:
					return t,s2,1,s3
		else:
			return t,None,None,None
	############################################################################


	# get_crafting_table_slot(i)
	#
	#	@argument <int> i : slot number from the following layout:
	# 		Crafting
	# 		[01][02][03]
	# 		[04][05][06] -> [00]
	# 		[07][08][09]
	# 		Inventory
	# 		[10][11][12][13][14][15][16][17][18]
	# 		[19][20][21][22][23][24][25][26][27]
	# 		[28][29][30][31][32][33][34][35][36]
	# 		------------------------------------
	# 		[37][38][39][40][41][42][43][44][45]
	#
	#	@description : returns a tuple with the time of the inspection, a string
	#		with the name of the item and an int with the number of items in the
	#		stack
	#
	def get_crafting_table_slot(self, i):
		outter = self._get_window_dimensions()
		pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))
		t,inventory_open,recipe_open = self.are_crafting_table_and_recipe_open()
		old_x,old_y = win32api.GetCursorPos()
		pywinauto.mouse.move(coords=(old_x,old_y))
		if inventory_open:
			if recipe_open:
				dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe on) slot list of amount"][i]
			else:
				dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe off) slot list of amount"][i]

			outter = self._get_window_dimensions()

			old_x,old_y = win32api.GetCursorPos()

			pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))

			t,s = self._parse_screenshot_to_string( dimensions )

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			if recipe_open:
				dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe on) slot list of durability"][i]
			else:
				dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe off) slot list of durability"][i]


			t,s3 = self._parse_screenshot_to_string( dimensions3 )
			try: s3 = sum([int(i) for i in s3])
			except: s3 = 0

			pywinauto.mouse.move(coords=(inner["left"],inner["top"]))

			if recipe_open:
				dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe on) slot list of items"][i]
				dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe on, inverted) slot list of items"][i]
			else:
				dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe off) slot list of items"][i]
				dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Crafting table (recipe off, inverted) slot list of items"][i]

			t,s2 = self._parse_screenshot_to_string( dimensions2 )
			s2 = s2.rstrip()
			if s2 == "":
				t,s2 = self._parse_screenshot_to_string( dimensions2_inv )
			s2 = s2.lstrip().rstrip()

			pywinauto.mouse.move(coords=(old_x,old_y))


			try: return t,s2,int(s),None
			except:
				if s2 == "":
					return t,None,None,None
				else:
					return t,s2,1,s3
		else:
			return t,None,None,None
	############################################################################


	# get_dropper_slot(i)
	#
	#	@argument <int> i : slot number from the following layout:
	#		Dropper
	#		[00][01][02]
	#		[03][04][05]
	#		[06][07][08]
	#		Inventory
	#		[09][10][11][12][13][14][15][16][17]
	#		[18][19][20][21][22][23][24][25][26]
	#		[27][28][29][30][31][32][33][34][35]
	#		------------------------------------
	#		[36][37][38][39][40][41][42][43][44]
	#
	#	@description : returns a tuple with the time of the inspection, a string
	#		with the name of the item and an int with the number of items in the
	#		stack
	#
	def get_dropper_slot(self, i):
		outter = self._get_window_dimensions()
		pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))
		t,inventory_open = self.is_dropper_open()
		old_x,old_y = win32api.GetCursorPos()
		pywinauto.mouse.move(coords=(old_x,old_y))
		if inventory_open:
			dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dropper slot list of amount"][i]

			outter = self._get_window_dimensions()

			old_x,old_y = win32api.GetCursorPos()

			pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))

			t,s = self._parse_screenshot_to_string( dimensions )

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dropper slot list of durability"][i]

			t,s3 = self._parse_screenshot_to_string( dimensions3 )
			try: s3 = sum([int(i) for i in s3])
			except: s3 = 0

			pywinauto.mouse.move(coords=(inner["left"],inner["top"]))

			dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dropper slot list of items"][i]
			dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dropper (inverted) slot list of items"][i]

			t,s2 = self._parse_screenshot_to_string( dimensions2 )
			s2 = s2.rstrip()
			if s2 == "":
				t,s2 = self._parse_screenshot_to_string( dimensions2_inv )
			s2 = s2.lstrip().rstrip()

			pywinauto.mouse.move(coords=(old_x,old_y))


			try: return t,s2,int(s),None
			except:
				if s2 == "":
					return t,None,None,None
				else:
					return t,s2,1,s3
		else:
			return t,None,None,None
	############################################################################


	# get_dispenser_slot(i)
	#
	#	@argument <int> i : slot number from the following layout:
	#		Dispenser
	#		[00][01][02]
	#		[03][04][05]
	#		[06][07][08]
	#		Inventory
	#		[09][10][11][12][13][14][15][16][17]
	#		[18][19][20][21][22][23][24][25][26]
	#		[27][28][29][30][31][32][33][34][35]
	#		------------------------------------
	#		[36][37][38][39][40][41][42][43][44]
	#
	#	@description : returns a tuple with the time of the inspection, a string
	#		with the name of the item and an int with the number of items in the
	#		stack
	#
	def get_dispenser_slot(self, i):
		outter = self._get_window_dimensions()
		pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))
		t,inventory_open = self.is_dispenser_open()
		old_x,old_y = win32api.GetCursorPos()
		pywinauto.mouse.move(coords=(old_x,old_y))
		if inventory_open:
			dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dispenser slot list of amount"][i]

			outter = self._get_window_dimensions()

			old_x,old_y = win32api.GetCursorPos()

			pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))

			t,s = self._parse_screenshot_to_string( dimensions )

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dispenser slot list of durability"][i]

			t,s3 = self._parse_screenshot_to_string( dimensions3 )
			try: s3 = sum([int(i) for i in s3])
			except: s3 = 0

			pywinauto.mouse.move(coords=(inner["left"],inner["top"]))

			dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dispenser slot list of items"][i]
			dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dispenser (inverted) slot list of items"][i]

			t,s2 = self._parse_screenshot_to_string( dimensions2 )
			s2 = s2.rstrip()
			if s2 == "":
				t,s2 = self._parse_screenshot_to_string( dimensions2_inv )
			s2 = s2.lstrip().rstrip()

			pywinauto.mouse.move(coords=(old_x,old_y))


			try: return t,s2,int(s),None
			except:
				if s2 == "":
					return t,None,None,None
				else:
					return t,s2,1,s3
		else:
			return t,None,None,None
	############################################################################


	# get_chest_slot(i)
	#
	#	@argument <int> i : slot number from the following layout:
	#		Chest
	#		[00][01][02][03][04][05][06][07][08]
	#		[09][10][11][12][13][14][15][16][17]
	#		[18][19][20][21][22][23][24][25][26]
	#		Inventory
	#		[27][28][29][30][31][32][33][34][35]
	#		[36][37][38][39][40][41][42][43][44]
	#		[45][46][47][48][49][50][51][52][53]
	#		------------------------------------
	#		[54][55][56][57][58][59][60][61][62]
	#
	#	@description : returns a tuple with the time of the inspection, a string
	#		with the name of the item and an int with the number of items in the
	#		stack
	#
	def get_chest_slot(self, i):
		outter = self._get_window_dimensions()
		pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))
		t,inventory_open = self.is_dispenser_open()
		old_x,old_y = win32api.GetCursorPos()
		pywinauto.mouse.move(coords=(old_x,old_y))
		if inventory_open:
			dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Chest slot list of amount"][i]

			outter = self._get_window_dimensions()

			old_x,old_y = win32api.GetCursorPos()

			pywinauto.mouse.move(coords=(outter["left"]+20,outter["top"]+20))

			t,s = self._parse_screenshot_to_string( dimensions )

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			dimensions3 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Chest slot list of durability"][i]

			t,s3 = self._parse_screenshot_to_string( dimensions3 )
			try: s3 = sum([int(i) for i in s3])
			except: s3 = 0

			pywinauto.mouse.move(coords=(inner["left"],inner["top"]))

			dimensions2 = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Chest slot list of items"][i]
			dimensions2_inv = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Chest (inverted) slot list of items"][i]

			t,s2 = self._parse_screenshot_to_string( dimensions2 )
			s2 = s2.rstrip()
			if s2 == "":
				t,s2 = self._parse_screenshot_to_string( dimensions2_inv )
			s2 = s2.lstrip().rstrip()

			pywinauto.mouse.move(coords=(old_x,old_y))


			try: return t,s2,int(s),None
			except:
				if s2 == "":
					return t,None,None,None
				else:
					return t,s2,1,s3
		else:
			return t,None,None,None
	############################################################################


	""" [ Interaction (open loop) (try to use the close loop methods) ] """

	# PRIVATE
	# _ol_rotate_camera(yaw, pitch)
	#
	#	@argument <float> yaw : relative yaw angle in º (horizontal : X axis)
	#
	#	@argument <float> pitch : relative pitch angle in º (vertical : Y axis)
	#
	#	@description : moves the mouse to get a +yaw and +pitch angle.
	#		DEPRECATED, USE self.set_angles FOR MORE PRECISION
	#
	def _ol_rotate_camera(self, yaw, pitch):
		s = self.settings["Sensitivity"]
		self.mouse_move_relative(  s * 600 / 90 * yaw, s * 600 / 90 * pitch )
	############################################################################


	# PRIVATE
	# _ol_walk_odometry(df)
	#
	#	@argument <float> df : blocks
	#
	#	@description : move df blocks based on odometry (estimated speed).
	#		DEPRECATED, USE self.go_* or self.walk_* methods instead
	#
	def _ol_walk_odometry(self, df):

		if self.sneaking:
			v = self.VERSIONS[self.version]["Character settings"]["Odometry sneak speed"]
		elif self.sprinting:
			v = self.VERSIONS[self.version]["Character settings"]["Odometry sprint speed"]
		else:
			v = self.VERSIONS[self.version]["Character settings"]["Odometry walk speed"]

		dt = abs(df / v)

		if df > 0:
			self.press("Walk Forwards")
		else:
			self.press("Walk Backwards")

		time.sleep(dt)

		self.release("Walk Forwards")
		self.release("Walk Backwards")
	############################################################################


	""" [ Interaction (close loop) ] """


	# set_angles(yaw_f, pit_f, tol=0.1, iter=2)
	#
	#	@argument <float> yaw_f : final yaw
	#
	#	@argument <float> pit_f : final pitch
	#
	#	@argument <float> tol : maximum error after iter iterations
	#
	#	@argument <int> iter : maximum iterations to convergence
	#
	#	@description : rotates the camera to yaw_f,pit_f
	#
	def set_angles(self, yaw_f, pit_f, tol=0.1, iter=2):

		yaw,pit = self.get_YP()[1]

		# Both quantities to 0º with a tolerance tol if iterations are higher than iter...
		i = 0
		while True:
			i += 1
			yaw,pit = self.get_YP()[1]
			Δyaw = (yaw - yaw_f + 180) % 360 -180
			self._ol_rotate_camera(-max([Δyaw, ((Δyaw>0)-(Δyaw<0))* 0.15], key=abs),0)
			yaw,pit = self.get_YP()[1]
			if ( (yaw - yaw_f) <= tol and i >= iter) or yaw == yaw_f or (yaw_f == 180 and yaw == -180) or (yaw_f == -180 and yaw == 180):
				break

		i = 0
		while True:
			i += 1
			yaw,pit = self.get_YP()[1]
			Δpit = (pit - pit_f + 180) % 360 -180
			self._ol_rotate_camera(0,-max([Δpit, ((Δpit>0)-(Δpit<0))* 0.15], key=abs))
			yaw,pit = self.get_YP()[1]
			if ( (pit - pit_f) <= tol and i >= iter) or pit == pit_f:
				break
	############################################################################


	# PRIVATE
	# go_forward_xz(df)
	#
	#	@argument <float> df : blocks
	#
	#	@description : move df blocks based on closed loop for debug inspection.
	#		This method only inspect x and z, use self.go_forward_xyz if you
	#		move upstairs or downstairs
	#
	def go_forward_xz(self, df, df_tol=0.05):

		# Get tuple xyz_i = (x_i, y_i, z_i)
		x_i,y_i,z_i = self.get_XYZ()[1]

		# Real overall movement
		df_r = 0

		while True:
			x,y,z = self.get_XYZ()[1]

			df_r = ( (x-x_i)**2 + (z-z_i)**2 )**0.5 * ( (df >= 0) - (df < 0) )

			if abs(df-df_r) < df_tol: break

			if abs(df-df_r) < 3: self.press("Sneak")

			if abs(df-df_r) > 20: self.press("Sprint")

			if abs(df-df_r) < 10: self.release("Sprint")

			self._ol_walk_odometry( 0.66 * (df - df_r) )

			# Wait until the inertia goes away
			while self.get_speed()[1]: continue

		self.release("Walk Forwards")
		self.release("Sneak")
	############################################################################


	# PRIVATE
	# go_straight_xz(df)
	#
	#	@argument <tuple<float,float,float>> xyz : target world position
	#
	#	@argument <float> d_tol : tolerance
	#
	#	@description : move to x,y,z in a straight line keeping the initial
	#		yaw,pitch angles. Only inspects x,z, use self.go_forward_xyz if you
	#		move upstairs/downstairs
	#
	def go_straight_xz(self, xyz, d_tol=0.05):

		df = float('inf')
		while df > d_tol:

			x_i,y_i,z_i = self.get_XYZ()[1]
			x,y,z = xyz

			# Remember the last yaw,pitch pair
			y_i,p_i = self.get_YP()[1]

			# Calculate the yaw
			# OLD y = 360 * math.atan2( (z - z_i), - (x - x_i) ) / (2 * math.pi)

			dx = (x - x_i)
			dz = (z - z_i)
			if dx < 0 and dz < 0:
				y = 90 + 360 * math.atan2( abs(dz), abs(dx) ) / (2 * math.pi)
			elif dx < 0 and dz > 0:
				y = 360 * math.atan2( abs(dx), abs(dz) ) / (2 * math.pi)
			elif dx > 0 and dz > 0:
				y = - 360 * math.atan2( abs(dx), abs(dz) ) / (2 * math.pi)
			elif dx > 0 and dz < 0:
				y = 360 * math.atan2( abs(dx), abs(dz) ) / (2 * math.pi) - 180


			# Calculate the distance
			df = ( (x-x_i)**2 + (z-z_i)**2 )**0.5

			# Set angles
			self.set_angles(y,p_i)

			# Go forward
			self.go_forward_xz(df, df_tol=d_tol)

			# Reorientate
			self.set_angles(y_i,p_i)
	############################################################################


	""" [ Inventory (cursor placement) ] """


	# cursor_to_inventory_slot(i)
	#
	#	@argument <int> i : slot number from the following layout:
	#		[103]             Crafting
	#		[102]		      [80][81]
	#		[101]             [83][84] -> [85*]
	#		[100]		[-106]
	#		[09][10][11][12][13][14][15][16][17]
	#		[18][19][20][21][22][23][24][25][26]
	#		[27][28][29][30][31][32][33][34][35]
	#		------------------------------------
	#		[00][01][02][03][04][05][06][07][08]
	#
	#	@description : returns True if the cursor moved successfully to the
	#		requested item slot
	#
	def cursor_to_ui_inventory(self, i):
		outter = self._get_window_dimensions()
		t,inventory_open,recipe_open = self.are_inventory_and_recipe_open()
		if inventory_open:
			if recipe_open:
				dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe on) slot list of amount"][i]
			else:
				dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Inventory (recipe off) slot list of amount"][i]

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			x = inner["left"]
			y = inner["top"]
			pywinauto.mouse.move(coords=(x,y))

			return True
		else:
			return False


	def cursor_to_ui_dispenser(self, i):
		outter = self._get_window_dimensions()
		t,inventory_open = self.is_dispenser_open()
		if inventory_open:
			dimensions = MinecraftAFKSubstitute.VERSIONS[self.version]["UI overlay"]["Dispenser slot list of amount"][i]

			inner = self._parse_crop_screen_from_dimensions( dimensions )

			x = inner["left"]
			y = inner["top"]
			pywinauto.mouse.move(coords=(x,y))

			return True
		else:
			return False


	# Large chest
	# [00][01][02][03][04][05][06][07][08]
	# [09][10][11][12][13][14][15][16][17]
	# [18][19][20][21][22][23][24][25][26]
	# [27][28][29][30][31][32][33][34][35]
	# [36][37][38][39][40][41][42][43][44]
	# [45][46][47][48][49][50][51][52][53]
	# Inventory
	# [54][55][56][57][58][59][60][61][62]
	# [63][64][65][66][67][68][69][70][71]
	# [72][73][74][75][76][77][78][79][80]
	# ------------------------------------
	# [81][82][83][84][85][86][87][88][89]

	""" Buttons """

	# TODO
	def push_button(self, button):

		with mss.mss() as sct:

			# Pixel size (real GUI_Scale)
			pixel_size = self._get_GUI_Scale()

			# Grab the image
			im = sct.grab( self._get_window_dimensions() )

			# Convert to numpy to scan it
			screen = np.array(im, dtype=int)
			target = np.asarray( Image.open(MinecraftAFKSubstitute.VERSIONS[self.version]["Buttons"][button]) )

			for x1 in range(screen.shape[1] - target.shape[1] + 1):
				for y1 in range(screen.shape[0] - target.shape[0] + 1):
					x2 = x1 + target.shape[1]
					y2 = y1 + target.shape[0]

					# Return true and the crop
					if (screen[y1:y2,x1:x2] == target).all():

						self.mouse_move_absolute( x1 + int(target.shape[1] / 2), y1 + int(target.shape[0] / 2) )
						self.press_and_release("Attack")


						return True, {"top" : y1, "left" : x1, "width" : target.shape[0], "height" : target.shape[1]}

		# If not return False
		return False, None

#
