# macros for general uses
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode

app = {
    "name": "Media | UI | Prgms",
    "macros": [
        # 1st Row
        (0x00FF00, "Vol+", [[ConsumerControlCode.VOLUME_INCREMENT]]),
        (0xFF00FF, "FScrn", [Keycode.F11]),
        (0x0100FF, "Files", [Keycode.LEFT_GUI, Keycode.ONE]),
        # 2nd Row
        (0x00FF00, "|> ||", [[ConsumerControlCode.PLAY_PAUSE]]),
        (0xFF00FF, "SwWin", [Keycode.ALT, Keycode.TAB]),
        (0x0100FF, "Brwsr", [Keycode.LEFT_GUI, Keycode.SIX]),
        # 3rd Row
        (0x00FF00, "Vol-", [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0xFF00FF, "Copy", [Keycode.CONTROL, Keycode.C]),
        (
            0x0100FF,
            "Cmnd",
            [Keycode.LEFT_GUI, Keycode.X, -Keycode.LEFT_GUI, -Keycode.X, Keycode.C],
        ),
        # 4th Row
        (0x00FF00, "Mute", [[ConsumerControlCode.MUTE]]),
        (0xFF00FF, "Paste", [Keycode.CONTROL, Keycode.V]),
        (0xFF0000, "Exit", [Keycode.ALT, Keycode.F4]),
    ],
}
