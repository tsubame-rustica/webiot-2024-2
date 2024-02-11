import RPi.GPIO as GPIO
import time

# GPIOピンの設定
GPIO.setmode(GPIO.BOARD)

SENSOR1 = 19
SENSOR2 = 26
GPIO.setup(SENSOR1, GPIO.IN)  # IRセンサー1の入力ピン
GPIO.setup(SENSOR2, GPIO.IN)  # IRセンサー2の入力ピン

def linetrace():
    while True:
        if GPIO.input(SENSOR1) == GPIO.LOW and GPIO.input(SENSOR2) == GPIO.LOW:
            # 直進
            print("両方のセンサーでラインが検出されました")
            # ロボットの動作を制御するためのコードを追加する

        elif GPIO.input(SENSOR1) == GPIO.LOW:
            # 左右のどちらかに旋回
            print("センサー1でラインが検出されました")
            # ロボットの動作を制御するためのコードを追加する

        elif GPIO.input(SENSOR2) == GPIO.LOW:
            # 左右のどちらかに旋回
            print("センサー2でラインが検出されました")
            # ロボットの動作を制御するためのコードを追加する

        else:
            # 停止 手動操縦でラインまで復帰できるようにするのもアリ
            print("ラインが検出されませんでした")
            # ロボットの動作を制御するためのコードを追加する

        time.sleep(0.1)  # 安定のための遅延

# 実行
# linetrace()

# GPIOピンのクリーンアップ
GPIO.cleanup()
