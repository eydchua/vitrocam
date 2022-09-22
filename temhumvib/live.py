#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os, subprocess, datetime

def liveView():
    #GPIO SETUP
    sensor = 18
    light1 = 16
    light2 = 11

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN)
    GPIO.setup(light1,GPIO.OUT)
    GPIO.setup(light2,GPIO.OUT)

    try:
        #turn on IR light
        GPIO.output(light1, True)
        GPIO.output(light2, True)
        subprocess.run(["libcamera-vid -t 60000 --vflip=1 --hflip=1 --framerate 210 --shutter 30 --width 640 --height 400 --awbgains 0,0 --flush 1 --denoise off --brightness 0 --contrast 1 --saturation 1 --sharpness 1 --gain 1"], shell=True, capture_output=True)
        #turn off IR light
        GPIO.output(light1, False)
        GPIO.output(light2, False)
        print("Live view done!")
        return

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    liveView()
