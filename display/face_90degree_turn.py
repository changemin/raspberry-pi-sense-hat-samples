from sense_hat import SenseHat
import time

sense = SenseHat()

# 색상 정의
R = (0, 255, 0) # 빨간색
G = (0, 255, 0) # 초록색
B = (0, 0, 255) # 파란색
O = (0, 0, 0)   # LED 끄기
bg = (0,0,0)

def rotate_matrix_90_clockwise(matrix):
    # 8x8 매트릭스를 전제로 함
    size = 8
    rotated_matrix = [0] * (size * size)

    for row in range(size):
        for col in range(size):
            # 시계 방향으로 90도 회전
            rotated_matrix[col * size + (size - 1 - row)] = matrix[row * size + col]

    return rotated_matrix

# 사용 예시


# 얼굴 표정 정의
smile = [
bg, bg, bg, bg, bg, bg, bg, bg,
bg, bg, R, bg, bg, R, bg, bg,
bg, bg, R, bg, bg, R, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg,
bg, R, bg, bg, bg, bg, R, bg,
bg, bg, R, R, R, R, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg
]

surprised = [
bg, bg, bg, bg, bg, bg, bg, bg,
bg, bg, R, bg, bg, R, bg, bg,
bg, bg, R, bg, bg, R, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg,
bg, R, R, R, R, R, R, bg,
bg, R, bg, bg, bg, bg, R, bg,
bg, bg, R, R, R, R, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg
]

sad = [
bg, bg, bg, bg, bg, bg, bg, bg,
bg, bg, R, bg, bg, R, bg, bg,
bg, bg, R, bg, bg, R, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg,
bg, bg, R, R, R, R, bg, bg,
bg, R, bg, bg, bg, bg, R, bg,
bg, bg, R, R, R, R, bg, bg,
bg, bg, bg, bg, bg, bg, bg, bg,
]

rotated_smile = rotate_matrix_90_clockwise(smile)
rotated_surprised = rotate_matrix_90_clockwise(surprised)
rotated_sad = rotate_matrix_90_clockwise(sad)


# 얼굴 표정을 순차적으로 표시하는 함수
def show_faces(faces, delay):
    for face in faces:
        sense.set_pixels(face)
        time.sleep(delay)

# 얼굴 표정 애니메이션을 무한 반복
while True:
    show_faces([rotated_smile, rotated_surprised], 2.0)
