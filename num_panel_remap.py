
import time
import ctypes
import keyboard

# Import the SendInput object
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBoardInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBoardInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK	= 0xB0
VK_MEDIA_PLAY_PAUSE	= 0xB3
VK_MEDIA_PREV_TRACK	= 0xB1
VK_CLEAR = 0x0C
VK_BRIGHTNESS_UP = 0x10
VK_BRIGHTNESS_DOWN = 0x11

def key_down(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def key_up(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def key(key_code, length = 0):
    key_down(key_code)
    time.sleep(length)
    key_up(key_code)








timeout = time.time()

while True:  # making a loop
	try:  # used try so that if user pressed other than the given key error will not be shown
		pressed =  keyboard.read_key()
		if pressed == 'left':  # if key 'q' is pressed
			key(VK_MEDIA_PREV_TRACK)
		elif pressed == 'right':
			key(VK_MEDIA_NEXT_TRACK)
		elif pressed == 'clear':
			if time.time() - timeout > 0.1:
				key(VK_MEDIA_PLAY_PAUSE)
				timeout = time.time()
		elif pressed == 'up':
			key(VK_VOLUME_UP)
		elif pressed == 'down':
			key(VK_VOLUME_DOWN)
	except:
		break













































#
