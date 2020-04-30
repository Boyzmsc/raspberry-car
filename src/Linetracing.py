# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# GPIO 모드를 BOARD 모드로 설정
GPIO.setmode(GPIO.BOARD)

# GPIO 경고 메세지를 나타나지 않게 설정
GPIO.setwarnings(False)

leftmostled = 16    # OTD(16)는 가장 왼쪽에 있는 LED로 16번 핀과 연결되어 있고, 가장 왼쪽에 있어서 leftmostled라고 함
leftlessled = 18    # OTB(18) 두 번째 왼쪽에 있는 LED로 18번 핀과 연결되어 있고, leftlessled라고 함
centerled = 22      # OTA(22)는 중앙에 있는 LED로 22번 핀과 연결되어 있고, centerled라고 함
rightlessled = 40   # OTC(40)는 두 번째 오른쪽에 있는 LED로 40번 핀과 연결되어 있고, rightlessled라고 함
rightmostled = 32   # OTE(32)는 가장 오른쪽에 있는 LED로 32번 핀과 연결되어 있고, 가장 오른쪽에 있어서 rightmostled라고 함

# 5방향 센서의 출력 데이터가 라즈베리 파이로 입력되기 때문에,
# 라즈베리 파이의 16, 18, 22, 40, 32번 핀은 Input 핀으로 설정됨
GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled,   GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)


def getLine():
    # 5방향 센서가 라인을 읽을 때 받아오는 값들을 각각의 특정 변수이름에 할당
    # 그 변수를 하나의 리스트에 순서대로 입력시켜 리턴시킴
    # 다른 코드에서 이 함수를 통해 현재 라인 상태를 알 수 있음
    l1 = (GPIO.input(leftmostled))
    l2 = (GPIO.input(leftlessled))
    c = (GPIO.input(centerled))
    r2 = (GPIO.input(rightlessled))
    r1 = (GPIO.input(rightmostled))

    sensor_list = [l1,l2,c,r2,r1]

    return sensor_list