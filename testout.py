import RPi.GPIO as GPIO
import time

AIN1 = 26
AIN2 = 8
AIN3 = 10
AIN4 = 22
AIN5 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(AIN3, GPIO.OUT)
GPIO.setup(AIN4, GPIO.OUT)
GPIO.setup(AIN5, GPIO.OUT)

#GPIO.output(AIN1, GPIO.HIGH)
GPIO.output(AIN2, GPIO.HIGH)
GPIO.output(AIN3, GPIO.LOW)
GPIO.output(AIN4, GPIO.HIGH)
GPIO.output(AIN5, GPIO.LOW)
time.sleep(5.0)
print("A")

#GPIO.output(AIN1, GPIO.LOW)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(AIN3, GPIO.HIGH)
GPIO.output(AIN4, GPIO.LOW)
GPIO.output(AIN5, GPIO.HIGH)
time.sleep(5.0)
GPIO.cleanup()
