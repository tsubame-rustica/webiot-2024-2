import time

def linetrace():
    while True:
        with open("./data/pos.txt", mode='w', encoding='utf-8') as f:
            f.write("112233")
                    
        time.sleep(1)  # 安定のための遅延

linetrace()