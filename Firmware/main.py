 # Firmware for MADPAD in CircuitPython which is to be flashed to the RP2040 
#atm each key just prints out a number - will change this later 


import board
import digitalio
import time
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#oled
displayio.release_displays()
i2c = board.I2C()
oled = SSD1306_I2C(128, 32, i2c)

#popup at start
splash = displayio.Group()
text = label.Label(terminalio.FONT, text="MADPAD HI ", x=10, y=10)
splash.append(text)
oled.show(splash)
time.sleep(2)

#key pin declaration
key_pins = [
    board.A0, board.A1, board.A2,
    board.A3, board.SDA, board.SCL,
    board.TX, board.RX, board.SCK
]

keys = []
for pin in key_pins:
    k = digitalio.DigitalInOut(pin)
    k.direction = digitalio.Direction.INPUT
    k.pull = digitalio.Pull.UP
    keys.append(k)

#hid keyboard so it can type on computer when plugged in
kbd = Keyboard(usb_hid.devices)

#TEMP - will remove this when i change to definite key functions
key_map = {
    0: Keycode.ONE,
    1: Keycode.TWO,
    2: Keycode.THREE,
    3: Keycode.FOUR,
    4: Keycode.FIVE,
    5: Keycode.SIX,
    6: Keycode.SEVEN,
    7: Keycode.EIGHT,
    8: Keycode.NINE,
}

#so no ghost typing
last_states = [True] * 9
debounce_time = 0.05  # 50 ms

#for text on oled
def show_message(msg, duration=1.0):
    group = displayio.Group()
    text_area = label.Label(terminalio.FONT, text=msg, x=10, y=10)
    group.append(text_area)
    oled.show(group)
    time.sleep(duration)

    #after last key pressed, returns to READY
    ready = displayio.Group()
    ready_text = label.Label(terminalio.FONT, text="Ready...", x=10, y=10)
    ready.append(ready_text)
    oled.show(ready)

#main
while True:
    for i in range(9):
        current = keys[i].value
        if not current and last_states[i]:  
            kbd.send(key_map[i])  
            show_message(f"Key {i+1} pressed", 1.0) #only 1s on OLED
            last_states[i] = False
            time.sleep(debounce_time)
        elif current:
            last_states[i] = True
    time.sleep(0.01)
