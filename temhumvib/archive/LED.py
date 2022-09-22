
import RPi.GPIO as GPIO
import time

sensor = 18
buzzer = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("IR Sensor Ready.....\n")


try: 
   while True:
      if GPIO.input(sensor)==False:
          GPIO.output(buzzer,False)
          print ("Object Detected")

      if GPIO.input(sensor)==True:
          GPIO.output(buzzer,True)
          print ("Nothing here")


except KeyboardInterrupt:
    GPIO.cleanup()
