import board

import digitalio

import usb_hid

from adafruit_hid.keyboard import Keyboard

from adafruit_hid.keycode import Keycode

# Inicializace klávesnice jako HID zařízení

keyboard = Keyboard(usb_hid.devices)

# Definice tlačítek

button_pins = [board.GP2, board.GP3, board.GP4, board.GP5]

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]

# Nastavení tlačítek jako vstupy s pull-up rezistorem

for button in buttons:

    button.direction = digitalio.Direction.INPUT

    button.pull = digitalio.Pull.UP

# Mapování tlačítek na klávesy

key_map = [Keycode.A, Keycode.B, Keycode.C, Keycode.D]  

while True:

    for i, button in enumerate(buttons):

        if not button.value:  # Tlačítko stisknuto (LOW)

            keyboard.press(key_map[i])  # Odeslání klávesy

        else:

            keyboard.release(key_map[i])  # Uvolnění klávesy 