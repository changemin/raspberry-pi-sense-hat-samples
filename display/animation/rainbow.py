from sense_hat import SenseHat
import time

sense = SenseHat()

# 무지개 색상 정의
colors = [
    (148, 0, 211),  # 보라색
    (75, 0, 130),   # 인디고색
    (0, 0, 255),    # 파란색
    (0, 255, 0),    # 초록색
    (255, 255, 0),  # 노란색
    (255, 127, 0),  # 주황색
    (255, 0, 0),    # 빨간색
]

# 무지개 애니메이션을 표시하는 함수
def draw_rainbow():
    # 무지개의 각 색을 LED 매트릭스의 한 행에 표시
    for i, color in enumerate(colors):
        for j in range(8):
            sense.set_pixel(j, i, color)

# 무지개 애니메이션을 움직이게 하는 함수
def move_rainbow():
    global colors
    while True:
        # 무지개를 그림
        draw_rainbow()
        # 잠시 기다림
        time.sleep(0.5)
        # 색상 리스트를 회전시킴
        colors = colors[-1:] + colors[:-1]

# 애니메이션 시작
move_rainbow()
