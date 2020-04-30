# Movement 모듈 임포트
# 구동체의 기본적인 움직임을 담당하는 모듈로,
# 전진, 포인트턴, 멈춤, 라인트레이싱 등의 움직임의 메서드를 포함하고 있음
import Movement

# Linetracing 모듈 임포트
# 5방향 센서가 라인을 읽을 때 받아오는 값들을 받아오기 위해 필요한 모듈로,
# 이 모듈의 메서드를 통해 현재 라인 상태를 알 수 있음
import Linetracing

# 구동체가 특정 움직임을 수행하기 전에 전진함
# 그때의 전진 속도와 시간을 설정
forwardspeed = 40
forwardtime = 0.5

# 구동체가 우회전/좌회전이나 유턴을 행할 때,
# 처음 회전은 큰 회전으로, 회전 세기와 시간을 설정해줌
# 두번째 회전은 세밀한 회전으로, 회전 시간만 설정해줌
turnspeed = 27
turntime_bf = 0.4
turntime_af = 0.1
turntime_ut = 1


def isright():
    # 우회전을 행할 상황에서 수행되는 함수로,
    # 회전 수행 전, 위에서 정해준 속도와 시간으로 전진하고,
    # 우측으로 포인트턴을 수행함, 그리고 5방향 센서 중 가운데 센서가 검은색 라인에 올 때까지 진행함
    # 첫번째 회전은 큰 회전으로, 두번째 회전은 세밀한 회전으로 주행 속도를 높임
    Movement.go_forward(forwardspeed, forwardtime)
    Movement.rightPointTurn(turnspeed, turntime_bf)
    while True:
        line = Linetracing.getLine()
        Movement.rightPointTurn(turnspeed, turntime_af)
        print('go!right!')
        if line[2] == 0:
            break


def isleft():
    # 좌회전을 행할 상황에서 수행되는 함수로,
    # 회전 수행 전, 위에서 정해준 속도와 시간으로 전진하고,
    # 좌측으로 포인트턴을 수행함, 그리고 5방향 센서 중 가운데 센서가 검은색 라인에 올 때까지 진행함
    # 첫번째 회전은 큰 회전으로, 두번째 회전은 세밀한 회전으로 주행 속도를 높임
    Movement.go_forward(forwardspeed, forwardtime)
    Movement.rightPointTurn(turnspeed, turntime_bf)
    while True:
        line = Linetracing.getLine()
        print('go!left!')
        Movement.leftPointTurn(turnspeed, turntime_af)
        if line[2] == 0:
            break


def uturn():
    # 유턴을 행할 상황에서 수행되는 함수로,
    # 회전 수행 전, 위에서 정해준 속도와 시간으로 전진하고,
    # 우측으로 포인트턴을 수행함, 그리고 5방향 센서 중 가운데 센서가 검은색 라인에 올 때까지 진행함
    # 첫번째 회전은 큰 회전으로, 두번째 회전은 세밀한 회전으로 주행 속도를 높임
    Movement.go_forward(forwardspeed, forwardtime)
    Movement.rightPointTurn(turnspeed, turntime_ut)
    while True:
        line = Linetracing.getLine()
        print('go!uturn!')
        Movement.rightPointTurn(turnspeed + 3, turntime_af)
        if line[2] == 0:
            break

