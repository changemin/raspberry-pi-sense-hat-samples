from sense_hat import SenseHat
import time

sense = SenseHat()

# 숨쉬는 효과를 위한 색상 정의 (부드러운 파란색)
color = (70, 130, 180)

# 밝기를 조절하기 위한 함수
def breathing_effect(color, duration, steps):
    r, g, b = color
    for i in range(steps):
        # 밝기를 서서히 증가
        adjusted_color = (int(r * i / steps), int(g * i / steps), int(b * i / steps))
        sense.clear(adjusted_color)
        time.sleep(duration / steps / 2)
    for i in range(steps, -1, -1):
        # 밝기를 서서히 감소
        adjusted_color = (int(r * i / steps), int(g * i / steps), int(b * i / steps))
        sense.clear(adjusted_color)
        time.sleep(duration / steps / 2)

# 숨쉬는 효과를 무한 반복
while True:
    breathing_effect(color, duration=5.0, steps=100)
