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