# RPi.GPIOのライブラリを「GPIO」という名前で使います
import RPi.GPIO as GPIO
import time

# GPIOのピン番号指定を「BCM」に設定します
GPIO.setmode(GPIO.BCM)


# PWMに使うピンに名前をつけます
pin_pwm = 13
AIN1 = 17
AIN2 = 22
AIN3 = 23
AIN4 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm, GPIO.OUT)
P13 = GPIO.PWM(pin_pwm, 100)

def init():
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(AIN3, GPIO.OUT)
    GPIO.setup(AIN4, GPIO.OUT)

def forward(tf):
    init()
    P13.start(60)
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, True)
    GPIO.output(AIN3, True)
    GPIO.output(AIN4, True)
    time.sleep(tf)
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, False)
    GPIO.output(AIN3, False)
    GPIO.output(AIN4, False)
    time.sleep(tf)
    GPIO.cleanup()

forward(3)
