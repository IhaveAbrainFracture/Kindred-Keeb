print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Keyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap  #underdefined
from kmk.modules.layers import layers 

# all imports
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,board.GP6, board.GP7,board.GP8, board.GP9,board.GP10,board.GP11, board.GP12, board.GP13, board.GP14 )
keyboard.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
keyboard.diode_orientation = DiodeOrientation.COL2ROW   # i think its col2row
keyboard.modules.append(layers)

PASTE =KC.MACRO(
  (
    KC.LCTL(KC.V)),
  )

COPY =KC.MACRO(
  (
    KC.LCTL(KC.C)),
  )


Ctrl_Tab =KC.MACRO(
  (
    KC.LCTL(KC.TAB)),
  )

Alt_Tab =KC.MACRO(
  (
    KC.LALT(KC.LTAB),
  )
)

SAVE = KC.MARCO (
    (
        KC.LCTL(KC.S)
    )
)

keyboard.keymap =     [ [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3, KC.N4, KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, PASTE,
        KC.TAB,  KC.Q,   KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, COPY,
        KC.CAPS, KC.A,   KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,   KC.K,   KC.L,    KC.SCLN, KC.QUOT,          KC.ENT,  SAVE,
        KC.LSFT, KC.Z,    KC.X,   KC.C ,  KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,      KC.RSFT, KC.MO(1), Alt_Tab,
        KC.LCTL, KC.LGUI, KC.LALT,                            KC.SPC,                             KC.RALT, KC.MO(2), KC.MENU, KC.RCTL, Ctrl_Tab,
    ],
    # L1 function keys
    [
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,
        KC.TRNS, KC.TRNS, KC.UP,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.PSCR, KC.SLCK, KC.PAUS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.TRNS, KC.TRNS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,  KC.TRNS,          KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS,                            KC.TRNS,                            KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    # Audio (might update for more stuff)
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.VOLU, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.MPRV, KC.VOLD, KC.MNXT, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS,                            KC.MPLY,                            KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]


if __name__ == '__main__':
    keyboard.go()