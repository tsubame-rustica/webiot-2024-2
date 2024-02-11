import time
import RPi.GPIO as GPIO

#モータードライバー関連は右リンク参照 https://creators-small-room.hatenablog.com/entry/motor-driver

#ピン番号の割り当て方式を「コネクタのピン番号」に設定
GPIO.setmode(GPIO.BOARD)

#使用するピン番号を代入
AIN1 = 8
AIN2 = 10
PWMA = 12

BIN1 = 22
BIN2 = 24
PWMB = 26


# AIN1_2 = 8
# AIN2_2 = 10
# PWMA_2 = 12

# BIN1_2 = 22
# BIN2_2 = 24
# PWMB_2 = 26


#各ピンを出力ピンに設定
GPIO.setup(AIN1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(BIN1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(BIN2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PWMB, GPIO.OUT, initial = GPIO.LOW)



GPIO.setup(AIN1_2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(AIN2_2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PWMA_2, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(BIN1_2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(BIN2_2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PWMB_2, GPIO.OUT, initial = GPIO.LOW)


#PWMオブジェクトのインスタンスを作成
#出力ピン：12,26  周波数：100Hz
p_a = GPIO.PWM(PWMA,100)
p_b = GPIO.PWM(PWMB,100)

p_a_2 = GPIO.PWM(PWMA_2,100)
p_b_2 = GPIO.PWM(PWMB_2,100)


#PWM信号を出力
p_a.start(0)
p_b.start(0)

p_a_2.start(0)
p_b_2.start(0)

#デューティを設定(0~100の範囲で指定)
#速度は80%で走行する。
val = 80

#デューティ比を設定
p_a.ChangeDutyCycle(val)
p_b.ChangeDutyCycle(val)

p_a_2.ChangeDutyCycle(val)
p_b_2.ChangeDutyCycle(val)

#ブレーキする関数
def func_brake():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.HIGH)


    GPIO.output(AIN1_2, GPIO.HIGH)
    GPIO.output(AIN2_2, GPIO.HIGH)
    GPIO.output(BIN1_2, GPIO.HIGH)
    GPIO.output(BIN2_2, GPIO.HIGH)


#前進する関数
def func_forward():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)

    GPIO.output(AIN1_2, GPIO.LOW)
    GPIO.output(AIN2_2, GPIO.HIGH)
    GPIO.output(BIN1_2, GPIO.LOW)
    GPIO.output(BIN2_2, GPIO.HIGH)


#後進する関数
def func_back():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)

    GPIO.output(AIN1_2, GPIO.HIGH)
    GPIO.output(AIN2_2, GPIO.LOW)
    GPIO.output(BIN1_2, GPIO.HIGH)
    GPIO.output(BIN2_2, GPIO.LOW)


#右回転する関数
def func_right():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)

    GPIO.output(AIN1_2, GPIO.LOW)
    GPIO.output(AIN2_2, GPIO.HIGH)
    GPIO.output(BIN1_2, GPIO.HIGH)
    GPIO.output(BIN2_2, GPIO.LOW)


#左回転する関数
def func_left():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)

    GPIO.output(AIN1_2, GPIO.HIGH)
    GPIO.output(AIN2_2, GPIO.LOW)
    GPIO.output(BIN1_2, GPIO.LOW)
    GPIO.output(BIN2_2, GPIO.HIGH)



# reset
def clear():

    p_a.stop()
    p_b.stop()

    p_a_2.stop()
    p_b_2.stop()

    #GPIOを開放
    GPIO.cleanup()