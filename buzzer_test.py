#buzzer_test.py
#Description: Creating the sound for winning and losing
#Author: Shawna Sanjay - ssanjay2@seattleu.edu

import RPi.GPIO as GPIO
from time import sleep
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

tb = TonalBuzzer(23)
tone_A3 = Tone(note= "A3")
tone_G5 = Tone(note= "G5")

try:
    while True:
        tb.play(tone_G5)
        print("You Win")
        sleep(0.5)
        
        tb.stop()
        print("no beep")
        sleep(0.5)
        
        tb.play(tone_A3)
        print("You Lose")
        sleep(0.5)
        
        tb.stop()
        print("no beep")
        sleep(0.5)
        
except KeyboardInterrupt:
    print("Exiting...")

finally:
    pass
