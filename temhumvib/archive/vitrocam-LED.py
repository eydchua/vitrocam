#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os, subprocess, datetime

# create directory for saving images
cwd = '/home/pi/Desktop/grid_images'

#GPIO SETUP
sensor = 16
buzzer = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("IR Sensor Ready.....\n")

while 1:
    if (GPIO.input(sensor)==False): #blotting pads are in rest position
        print("Waiting for blot...")
        time.sleep(0.5)
    if (GPIO.input(sensor)==True): #blotting pads are blotting
        GPIO.output(buzzer, True)
        print("Blotting in progress!")
        time.sleep(0.1)
        if (GPIO.input(sensor)==False): #blotting is done 
            print("Done blotting!")
            #make a folder
            now = str(datetime.datetime.now())
            path = os.path.join(cwd, now)
            os.mkdir(path)
            os.chdir(path)
            #take a video
            subprocess.run(["libcamera-vid -n -o vid.h264 -t 1000 --framerate 210 --shutter 30 --width 640 --height 400 --awbgains 0,0 --flush 1 --denoise off --brightness 0 --contrast 1 --saturation 1 --sharpness 1 --gain 10 --save-pts timestamps.txt"], shell=True, capture_output=True)
            #extract video frames
            subprocess.run(["ffmpeg -i vid.h264 'vid_frame%03d.png'"], shell=True, capture_output=True)
            while GPIO.input(sensor):
                time.sleep(0.2)
    else:
        GPIO.output(buzzer, False)
