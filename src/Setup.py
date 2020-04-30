# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# GPIO 모드를 BOARD 모드로 설정
GPIO.setmode(GPIO.BOARD)

# GPIO 경고 메세지를 나타나지 않게 설정
GPIO.setwarnings(False)

# 전진하기 위한 변수 forward와 backward에 각각 True, False값 할당
forward = True
backward = not(forward)

# =======================================================================
# 라즈베리파이에 있는 12, 11, 35번 핀 선언
# 좌측모터를 컨트롤하기 위해 필요한 세개의 핀
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# 라즈베리파이에 있는 15, 13, 37번 핀 선언
# 우측모터를 컨트롤하기 위해 필요한 세개의 핀
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

# =======================================================================
# GPIO 핀을 통해 라즈베리파이가 OUT으로 설정
# 좌측 모터의 출력 내보냄
# =======================================================================

# 좌측 모터 핀을 Output으로 설정
GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# GPIO 핀을 통해 라즈베리파이가 OUT으로 설정
# 우측 모터의 출력 내보냄
# =======================================================================

# 우측 모터 핀을 Output으로 설정
GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# 좌측/우측 모터 속도를 작동시키게 설정
GPIO.output(MotorLeft_PWM, GPIO.HIGH)
GPIO.output(MotorRight_PWM, GPIO.HIGH)

# =======================================================================
# 좌측 모터 속도 제어할 변수 생성
# 우측 모터 속도 제어할 변수 생성
# =======================================================================

# 속도 제어 (100 제한)
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)

def leftmotor(x):
    # 왼쪽 모터의 Red 전원선이 위에 있을 때 leftmotor(x)함수의 x= True로 하고, 아래에 있을 때는 x= False로 사용
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)      # x=True를 선택하면, 12번 핀에 High 값(1), 11번 핀에 Low 값(0)이 할당되어 전진할 수 있게 한다.

    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)     # x=False를 선택하면, 12번 핀에 Low 값(0), 11번 핀에 High 값(1)이 할당되어 전진할 수 있게 한다.
    else:
        print('Config Error')


def rightmotor(x):
    # 오른쪽 모터의 Red 전원선이 위에 있을 때 leftmotor(x)함수의 x= True로 하고, 아래에 있을 때는 x= False로 사용
    if x == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)    # x=True를 선택하면, 15번 핀에 Low 값(0), 13번 핀에 High 값(1) 이 할당되어 전진할 수 있게 한다.
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)     # x=False를 선택하면, 15번 핀에 High 값(1), 13번 핀에 Low 값(0)이 할당되어 전진할 수 있게 한다.
    else:
        print('Config Error')