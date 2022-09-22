#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os, subprocess

# change working directory to the camera location
os.chdir('/usr/bin/')

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):

    first_wait = 3      # wait time in seconds
    second_wait = 10

    if GPIO.input(channel):
            print ("Movement up Detected!")
    else:
            print ("Movement down Detected!")

    print('script called. Starting first wait')
    for t in range(first_wait):
        print('waiting %s seconds' %(first_wait-t))
        time.sleep(1)
    print('script started. Going to second wait')
    for t in range(second_wait):
        print('waiting %s seconds' %(second_wait-t))
        time.sleep(1)
    print('script started. calling camera')

    subprocess.run(["libcamera-hello"])


        

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)
# assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
