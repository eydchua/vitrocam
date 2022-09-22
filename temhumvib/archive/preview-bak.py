#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os, subprocess, datetime

def preview():
    #define directory for saving images
    cwd = '/home/pi/Desktop/grid_images'

    #GPIO SETUP
    light1 = 16
    light2 = 11

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(light1,GPIO.OUT)
    GPIO.setup(light2,GPIO.OUT)

    GPIO.output(light1,False)
    GPIO.output(light2,False)

    #make a folder
    now = str(datetime.datetime.now())
    now = now.replace(":", "")
    now = now.replace(".", "")
    path = os.path.join(cwd, now)
    path = str(path)+'_preview'
    os.mkdir(path)
    os.chdir(path)
    #turn on the lights
    GPIO.output(light1,True)
    GPIO.output(light2,True)
    #take an preview video
    subprocess.run(["libcamera-vid -n -o preview.h264 -t 20 --framerate 400 --shutter 20 --width 640 --height 400 --awbgains 0,0 --flush 1 --denoise off --brightness 0 --contrast 1 --saturation 0 --sharpness 1 --gain 1 --save-pts timestamps.txt"], shell=True, capture_output=True)
    #turn off the lights
    GPIO.output(light1,False)
    GPIO.output(light2,False)
    #extract video frames
    subprocess.run(["ffmpeg -i preview.h264 'preview_frame%03d.png'"], shell=True, capture_output=True)
    GPIO.cleanup()

if __name__ == '__main__':
    preview()
