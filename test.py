import RPi.GPIO as GPIO
import time
import signal
import sys
import os
#import cv2

# Cau hinh duong dan den file alarm.wav
wav_path = "/home/pi/MiAI_Sleep_Detection_Pi/Nguy-hiểm_-Khoảng-cách-không-an-toàn.wav"

# Ham phat ra am thanh
def play_sound(path):
    os.system('aplay ' + path)


# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 18
pinEcho = 24

def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

def test():
    #global distance
	# set Trigger to HIGH
    GPIO.output(pinTrigger, True)
	# set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    startTime = time.time()
    stopTime = time.time()

	# save start time
    while 0 == GPIO.input(pinEcho):
        startTime = time.time()

	# save time of arrival
    while 1 == GPIO.input(pinEcho):
        stopTime = time.time()

	# time difference between start and arrival
    TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    if distance <= 20:
        play_sound(wav_path)
    else:
        pass

    print ("Distance: %.1f cm" % distance)
    time.sleep(1)

def test2():
    while True:
        test()
test2()