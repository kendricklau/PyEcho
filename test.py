import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while(True):
    print "HIGH"
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(2.5)
    print "LOW"
    GPIO.output(23, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    time.sleep(2.5)
