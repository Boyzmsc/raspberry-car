# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 메소드 임포트
import time

# Setup 모듈 임포트
# 구동체의 움직임을 위해 기본적으로 설정해주는 모듈로,
# 구동체의 좌측/우측 모터의 속도 조절과 전진/후진 설정을 해줌
import Setup


def pwm_setup():
    # 좌측/우측 모터 속도 초기값 설정
    Setup.LeftPwm.start(0)
    Setup.RightPwm.start(0)

def go_forward(speed, running_time):
    # 시간 running_time과 속도 speed를 파라미터로 받음
    # 구동체를 특정 시간동안 특정 속도로 전진하게끔 하는 함수임
    Setup.leftmotor(Setup.forward)
    Setup.GPIO.output(Setup.MotorLeft_PWM, Setup.GPIO.HIGH)
    Setup.rightmotor(Setup.forward)
    Setup.GPIO.output(Setup.MotorRight_PWM, Setup.GPIO.HIGH)
    Setup.LeftPwm.ChangeDutyCycle(speed)
    Setup.RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)

def stop():
    # 구동체의 정지하게 하는 코드
    # 모터의 속도를 GPIO.LOW로 설정하고 속도를 0으로 설정함으로써 정지하게끔 함
    GPIO.output(Setup.MotorLeft_PWM, GPIO.LOW)
    GPIO.output(Setup.MotorRight_PWM, GPIO.LOW)
    Setup.LeftPwm.ChangeDutyCycle(0)
    Setup.RightPwm.ChangeDutyCycle(0)

def pwm_low():
    # 구동체의 동작을 완전히 멈추는 코드 (대부분 강제 정지 때 사용)
    # 모터의 속도를 GPIO.LOW로 설정하고 속도를 0으로 설정함으로써 정지하게끔 함
    # GPIO에 있는 cleanup() 메서드를 이용해 구동체의 동작을 멈춤
    GPIO.output(Setup.MotorLeft_PWM, GPIO.LOW)
    GPIO.output(Setup.MotorRight_PWM, GPIO.LOW)
    Setup.LeftPwm.ChangeDutyCycle(0)
    Setup.RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

def rightPointTurn(speed, running_time):
    # speed와 running_time을 파라미터로 가져옴
    # 각 바퀴의 방향을 반대로 해서 턴하는 유형
    # 좌측 모터를 전진으로, 우측 모터를 후진으로 설정
    Setup.leftmotor(Setup.forward)
    Setup.rightmotor(Setup.backward)

    Setup.LeftPwm.ChangeDutyCycle(speed)
    Setup.RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)

def leftPointTurn(speed, running_time):
    # speed와 running_time을 파라미터로 가져옴
    # 각 바퀴의 방향을 반대로 해서 턴하는 유형
    # 우측 모터를 전진으로, 좌측 모터를 후진으로 설정
    Setup.leftmotor(Setup.backward)
    Setup.rightmotor(Setup.forward)

    Setup.LeftPwm.ChangeDutyCycle(speed)
    Setup.RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)

def go(leftspeed, rightspeed):
    # 이 함수는 구동체의 오른쪽바퀴와 왼쪽바퀴의 속도를 일일이 입력값으로 받아와,
    # start라는 메서드를 이용해 바퀴를 전진하게 하게끔 만든 함수임 (+ 전진을 go_any에 내재된 메서드를 이용하지 않음)
    # leftspeed는 좌측 바퀴의 속도를, rightspeed는 우측 바퀴의 속도를 받아오는 입력값임
    Setup.leftmotor(Setup.forward)
    Setup.rightmotor(Setup.forward)
    Setup.LeftPwm.start(leftspeed)
    Setup.RightPwm.start(rightspeed)