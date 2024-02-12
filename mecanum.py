#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import cgi
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
MOTOR_A1 = 5;
MOTOR_A2 = 6;
MOTOR_B1 = 13;
MOTOR_B2 = 19;
MOTOR_C1 = 26;
MOTOR_C2 = 12;
MOTOR_D1 = 16;
MOTOR_D2 = 20;
 
GPIO.setup(MOTOR_A1, GPIO.OUT)
GPIO.setup(MOTOR_A2, GPIO.OUT)
GPIO.setup(MOTOR_B1, GPIO.OUT)
GPIO.setup(MOTOR_B2, GPIO.OUT)
GPIO.setup(MOTOR_C1, GPIO.OUT)
GPIO.setup(MOTOR_C2, GPIO.OUT)
GPIO.setup(MOTOR_D1, GPIO.OUT)
GPIO.setup(MOTOR_D2, GPIO.OUT)
 
form = cgi.FieldStorage()
recieve = form.getvalue('name')
 
if recieve == 'hhhhh':
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.HIGH)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.HIGH)
    GPIO.output(MOTOR_D2,GPIO.LOW)
    print('Content-type: text/html\n')
    print(recieve)
elif recieve == 'iiii':
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.HIGH)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.HIGH)
    print('Content-type: text/html\n')
    print(recieve)
elif recieve == 'jjjj':
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.HIGH)
    GPIO.output(MOTOR_D1,GPIO.HIGH)
    GPIO.output(MOTOR_D2,GPIO.LOW)
    print('Content-type: text/html\n')
    print(recieve)
elif recieve == 'kkkk':
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.HIGH)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.HIGH)
    print('Content-type: text/html\n')
    print(recieve)
elif recieve == 'ssss':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.LOW)
elif recieve == 'qqqq':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.HIGH)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.LOW)
elif recieve == 'mmmm':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.HIGH)
    GPIO.output(MOTOR_D2,GPIO.LOW)
elif recieve == 'gggg':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.HIGH)
    GPIO.output(MOTOR_D1,GPIO.HIGH)
    GPIO.output(MOTOR_D2,GPIO.LOW)
elif recieve == 'dddd':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)
    GPIO.output(MOTOR_C1,GPIO.HIGH)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.HIGH)
elif recieve == 'oooo':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.LOW)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.HIGH)
elif recieve == 'zzzz':
    print('Content-type: text/html\n')
    print(recieve)
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)
    GPIO.output(MOTOR_C1,GPIO.LOW)
    GPIO.output(MOTOR_C2,GPIO.HIGH)
    GPIO.output(MOTOR_D1,GPIO.LOW)
    GPIO.output(MOTOR_D2,GPIO.LOW)