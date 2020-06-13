#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import atexit

class Sg5010:
    def __init__(self, pin, direction):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = int(pin)
        self.direction = int(direction)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0.0)
#       atexit.register(self.cleanup)

    def cleanup(self):
        self.servo.ChangeDutyCycle(self.henkan(0))
        time.sleep(0.3)
        self.servo.stop()
        GPIO.cleanup()

    def currentdirection(self):
        return self.direction

    def henkan(self, value):
        return 0.05 * value + 7.0

    
    def setdirection(self, direction, speed):
        for d in range(self.direction, direction, int(speed)):
            self.servo.ChangeDutyCycle(self.henkan(d))
            self.direction = d
            time.sleep(0.1)
        self.servo.ChangeDutyCycle(self.henkan(direction))
        self.direction = direction

if __name__ == "__main()__":
    pass
