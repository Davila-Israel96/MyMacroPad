from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import sys

app = {
    "name": "Escape From Tarkov",
    "macros": [
        # 1st Row
        (0xFEFEFF, "ChkMag", [Keycode.LEFT_ALT, Keycode.T]),
        (0x00FE10, "TacDev", [Keycode.CONTROL, Keycode.T]),
        (0x0562FF, "Slot7", [Keycode.SEVEN]),
        # 2nd Row
        (0xFEFEFF, "Exfil", [Keycode.O, 0.1, -Keycode.O, Keycode.O]),
        (0xFE0000, "Mfnct", [Keycode.L, -Keycode.L, 3.5, Keycode.SHIFT, Keycode.T]),
        (0x0562FF, "Slot8", [Keycode.EIGHT]),
        # 3rd Row
        (0x000000, "-", []),
        (0x000000, "-", []),
        (0x0562FF, "Slot9", [Keycode.NINE]),
        # 4th Row
        (0x000000, "-", []),
        (0x000000, "-", []),
        (0x0562FF, "Slot0", [Keycode.ZERO]),
    ],
}
