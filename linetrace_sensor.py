import RPi.GPIO as GPIO
import time

# GPIOピンの設定
GPIO.setmode(GPIO.BOARD)

SENSOR1 = 29
SENSOR2 = 31
GPIO.setup(SENSOR1, GPIO.IN)  # IRセンサー1の入力ピン
GPIO.setup(SENSOR2, GPIO.IN)  # IRセンサー2の入力ピン

# ubuntu de nihongo douyatte utsunenn
def linetrace():
    while True:
        if GPIO.input(SENSOR1) == GPIO.HIGH and GPIO.input(SENSOR2) == GPIO.HIGH:
            # 直進
            print("heres MID!")
            # ロボットの動作を制御するためのコードを追加する

        elif GPIO.input(SENSOR1) == GPIO.HIGH:
            # 左右のどちらかに旋回
            print("heres LEFT, Go Right!")
            # ロボットの動作を制御するためのコードを追加する

        elif GPIO.input(SENSOR2) == GPIO.HIGH:
            # 左右のどちらかに旋回
            print("heres RIGHT, Go Left!")
            # ロボットの動作を制御するためのコードを追加する

        else:
            # 停止 手動操縦でラインまで復帰できるようにするのもアリ
            print("where am i?")
            # ロボットの動作を制御するためのコードを追加する

        time.sleep(1)  # 安定のための遅延

# 実行
linetrace()

# GPIOピンのクリーンアップ
GPIO.cleanup()
