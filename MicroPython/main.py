"""
Created by: Caleb Andreas
Created on: Oct 2024
This module is a Micro:bit MicroPython program that can measure distance with a sonar.
"""

from microbit import *
from time import sleep


class HCSR04:
    # This class abstracts out the functionality of the HC-SR04 and
    # returns distance in mm.
    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

    def distance_mm(self):
        spi.init(
            baudrate=125000,
            sclk=self.sclk_pin,
            mosi=self.trigger_pin,
            miso=self.echo_pin,
        )
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            # find first non full high value afterwards
            try:
                k, value = next(
                    (ind, v)
                    for ind, v in enumerate(resp[i : length - 2])
                    if resp[i + ind + 1] == 0
                )
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist = -1 if i < 0 else round(((pre + (k - i) * 8.0 + post) * 8 * 0.172) / 2)
        return dist


# Variables.
sonar = HCSR04()
display.show(Image.HAPPY)

# Find distance on a button press.
while True:
    if button_a.is_pressed():
        display.clear()
        display.show(sonar.distance_mm() / 10)
        sleep(1000)
        display.show(Image.HAPPY)
