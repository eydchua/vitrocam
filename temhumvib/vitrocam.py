

#!/usr/bin/python
import RPi.GPIO as GPIO
import preview, capture, live

if __name__ == '__main__':
    
    try:
        while 1:
            mode = input("Press p for preview, or v for blotting video, or l for live view: ")

            if mode == "p":
                preview.preview()
                
            if mode == "v":
                capture.capture()

            if mode == "l":
                live.liveView()

    except KeyboardInterrupt:
        GPIO.cleanup()

