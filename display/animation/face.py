from sense_hat import SenseHat
import time

sense = SenseHat()

# 색상 정의
R = (255, 0, 0) # 빨간색
G = (0, 255, 0) # 초록색
B = (0, 0, 255) # 파란색
O = (0, 0, 0)   # LED 끄기

# 얼굴 표정 정의
smile = [
O, O, O, O, O, O, O, O,
O, O, R, O, O, R, O, O,
O, O, O, O, O, O, O, O,
O, R, O, O, O, O, R, O,
O, O, R, R, R, R, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

surprised = [
O, O, O, O, O, O, O, O,
O, O, R, O, O, R, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, R, R, R, R, R, O, O,
O, R, O, O, O, R, O, O,
O, O, R, R, R, O, O, O,
O, O, O, O, O, O, O, O
]

sad = [
O, O, O, O, O, O, O, O,
O, O, R, O, O, R, O, O,
O, O, O, O, O, O, O, O,
O, O, R, R, R, R, O, O,
O, R, O, O, O, O, R, O,
O, O, R, R, R, R, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

# 얼굴 표정을 순차적으로 표시하는 함수
def show_faces(faces, delay):
    for face in faces:
        sense.set_pixels(face)
        time.sleep(delay)

# 얼굴 표정 애니메이션을 무한 반복
while True:
    show_faces([smile, surprised, sad], 2.0)
