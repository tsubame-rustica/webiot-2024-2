import RPi.GPIO as GPIO
import time
import motor_lib
import camera_test
import asyncio
import socket_server

# GPIOピンの設定
GPIO.setmode(GPIO.BOARD)
path = './data/get_action.txt'

SENSOR1 = 29
SENSOR2 = 31
GPIO.setup(SENSOR1, GPIO.IN)  # IRセンサー1の入力ピン
GPIO.setup(SENSOR2, GPIO.IN)  # IRセンサー2の入力ピン

# ubuntu de nihongo douyatte utsunenn
def linetrace():
    while True:
        with open(path, mode='w', encoding='utf-8') as f:
            data = list(f)
            f.write()
            print(data)
        val, id = camera_test.detect_barcode()

        if data[0] == data[1] == 1:
            if GPIO.input(SENSOR1) == GPIO.HIGH and GPIO.input(SENSOR2) == GPIO.HIGH:
                # 直進
                motor_lib.func_forward()
                print("heres MID!")
                # ロボットの動作を制御するためのコードを追加する

            elif GPIO.input(SENSOR1) == GPIO.HIGH:
                # 左右のどちらかに旋回
                motor_lib.func_right()
                print("heres LEFT, Go Right!")
                # ロボットの動作を制御するためのコードを追加する

            elif GPIO.input(SENSOR2) == GPIO.HIGH:
                # 左右のどちらかに旋回
                motor_lib.func_left()
                print("heres RIGHT, Go Left!")
                # ロボットの動作を制御するためのコードを追加する

            else:
                # 停止 手動操縦でラインまで復帰できるようにするのもアリ
                motor_lib.func_brake()
                print("where am i?")
                # ロボットの動作を制御するためのコードを追加する
        elif (val):
            x = int(id / (10**5))
            y = int((id - x*10**5) / 100)
            f = int((id - x*10**5 - y*100) / 10)
            with open("./data/connect_id.txt", mode='r', encoding='utf-8') as fl:
                connect = object(fl)
            with open("./data/pos.txt", mode='w', encoding='utf-8') as f:
                data = list(f)
                f.write()
            asyncio.run(socket_server.SocketData.send_msg(f'{x}{y}'))
                
        time.sleep(1)  # 安定のための遅延

# 実行
linetrace()

# GPIOピンのクリーンアップ
GPIO.cleanup()
