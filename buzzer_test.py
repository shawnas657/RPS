#buzzer_test.py
#Description: Creating the sound for winning and losing
#Author: Shawna Sanjay - ssanjay2@seattleu.edu

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 23

while(True):
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.output(buzzer, GPIO.HIGH)
    print("beep")
    sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    print("no beep")
    sleep(0.1)