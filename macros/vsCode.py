# macros for Visual Studio Code

# syntax is from <foldername>.<libary> import <class>
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# our main class takes in an app object
app = {
    "name": "VS Code",  # App Name
    "macros": [
        # COLOR - LABEL - KEY SEQUENCE
        # 1st Row
        (0x0000FF, "Term", [Keycode.CONTROL, Keycode.GRAVE_ACCENT]),
        (0x0000FF, "Start", ["npm start"]),
        (0x0000FF, "Install", ["npm install"]),
        # 2nd Row
        (0x0000FF, "FScrn", [Keycode.F11]),
        (0x0000FF, "O.Fold", [Keycode.CONTROL, Keycode.K, -Keycode.K, Keycode.O]),
        (0x0000FF, "N.Win", [Keycode.CONTROL, Keycode.SHIFT, Keycode.N]),
        # 3rd Row
        (0x0000FF, "Copy", [Keycode.CONTROL, Keycode.C]),
        (0x0000FF, "Paste", [Keycode.CONTROL, Keycode.V]),
        (0xFF0100, "Cut", [Keycode.CONTROL, Keycode.X]),
        # 4th Row
    ],
}
