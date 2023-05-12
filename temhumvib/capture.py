#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os, subprocess, datetime

def capture():
    #define directory for saving images
    cwd = '/home/pi/Desktop/grid_images'

    #GPIO SETUP
    sensor = 18
    light1 = 16
    light2 = 11

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN)
    GPIO.setup(light1,GPIO.OUT)
    GPIO.setup(light2,GPIO.OUT)

    print ("IR Sensor Ready.....\n")

    try:
        while (GPIO.input(sensor)==False): #blotting pads are in rest position
            GPIO.output(light1,False)
            GPIO.output(light2,False)
            print("Waiting for blot...")
            time.sleep(0.5)
            
        while (GPIO.input(sensor)==True): #blotting pads are blotting
            print("Blotting in progress!")
            #time.sleep(0.1)
            if (GPIO.input(sensor)==False): #blotting is done 
                print("Done blotting!")
                #make a folder
                now = str(datetime.datetime.now())
                now = now.replace(":", "")
                now = now.replace(".", "")
                now = now.replace(" ", "-")
                path = os.path.join(cwd, now)
                os.mkdir(path)
                os.chdir(path)
                #turn on IR light
                GPIO.output(light1, True)
                GPIO.output(light2, True)
                #take a video
                time.sleep(0.5)
                subprocess.run(["libcamera-vid -n -o vid.h264 -t 500 --vflip=1 --hflip=1 --framerate 210 --shutter 20 --width 640 --height 400 --awbgains 0,0 --flush 1 --denoise off --brightness 0 --contrast 1 --saturation 1 --sharpness 1 --gain 1 --save-pts timestamps.txt"], shell=True, capture_output=True)
                #turn off IR light
                GPIO.output(light1, False)
                GPIO.output(light2, False)
                #extract video frames
                subprocess.run(["ffmpeg -i vid.h264 'vid_frame%03d.png'"], shell=True, capture_output=True)
                print("Video captured! In %s" % path)
                return

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    capture()
