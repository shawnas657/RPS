#buzzer_test.py
#Description: Creating the sound for winning and losing
#Author: Shawna Sanjay - ssanjay2@seattleu.edu

import RPi.GPIO as GPIO
from time import sleep
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

tb = TonalBuzzer(23)
tone_C5 = Tone(note= "C5")

try:
    while True:
        tb.play(tone_C5)
        print("beep")
        sleep(0.1)
        
        tb.stop()
        print("no beep")
        sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pass
