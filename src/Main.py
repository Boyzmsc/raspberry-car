# Movement 모듈 임포트
# 구동체의 기본적인 움직임을 담당하는 모듈로,
# 전진, 포인트턴, 멈춤, 라인트레이싱 등의 움직임의 메서드를 포함하고 있음
import Movement

# Linetracing 모듈 임포트
# 5방향 센서가 라인을 읽을 때 받아오는 값들을 받아오기 위해 필요한 모듈로,
# 이 모듈의 메서드를 통해 현재 라인 상태를 알 수 있음
import Linetracing

# Maze 모듈 임포트
# 구동체가 미로 속에서 주행할 때, 수행해야할 움직임을 담당하는 모듈로,
# 우회전, 좌회전, 유턴 움직임의 메서드를 포함하고 있음
import Maze

# 속도를 6개의 단계로 나누어 변수에 지정해줌
# 여기서 veryhighspeed는 구동체가 직진할 때의 가장 보편적인 속도를 입력함
veryhighspeed = 40
highspeed = 28
midspeed = 18
lowspeed = 10
verylowspeed = 3
zero = 0

# 이중리스트 형태이며, 첫번째 인덱스에 해당되는 부분은 5개의 센서가 받아오는 센서의 결과값을 예측한 부분임
# 두번째 인덱스에 해당되는 부분은 이 코드에 자체적으로 생성한 go()함수에 좌측 바퀴 속도로 입력하는 값임
# 세번째 인덱스에 해당되는 부분은 이 코드에 자체적으로 생성한 go()함수에 우측 바퀴 속도로 입력하는 값임
linetracing_list = [
    [[0,1,1,1,1], verylowspeed, veryhighspeed],
    [[0,0,1,1,1], lowspeed, veryhighspeed],
    [[1,0,1,1,1], midspeed, veryhighspeed],
    [[1,0,0,1,1], highspeed, veryhighspeed],
    [[1,1,1,1,0], veryhighspeed, verylowspeed],
    [[1,1,1,0,0], veryhighspeed, lowspeed],
    [[1,1,1,0,1], veryhighspeed, midspeed],
    [[1,1,0,0,1], veryhighspeed, highspeed],
    [[1,1,0,1,1], veryhighspeed, veryhighspeed],
    [[1,0,0,0,1], veryhighspeed, veryhighspeed]
]

# 오른쪽/왼쪽 그리고 유턴으로 포인트턴할때의 센서 상태를 이중리스트 형태로 만들어줌
right_list = [[0,0,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]
left_list = [[0,0,0,1,1]]
uturn_list = [[1,1,1,1,1]]

if __name__ == "__main__":
    try:
        while True:
            # Linetracing 모듈에 getLine() 메서드를 이용해서,
            # 현재 라인 상태를 리스트 형태로 받아옴
            line = Linetracing.getLine()

            # 위에 선언해준 linetracing_list의 길이만큼 for문을 반복함
            # 이중 리스트인 linetracing_list의 첫번째 인덱스 값이 5방향 센서의 데이터와 같으면,
            # 두번재 인덱스와 세번째 인덱스 값을 Movement 모듈에 있는 go()함수의 파라미터로 입력시켜 go()함수를 구동시킴
            for i in range(len(linetracing_list)):
                if line == linetracing_list[i][0]:
                    Movement.go(linetracing_list[i][2], linetracing_list[i][1])
                    break

            # 5방향 센서에서 읽어오는 데이터가 오른쪽으로 턴할때의 센서 상태를 저장한
            # 이중리스트 안에 해당 값이 있으면 Maze 모듈에 있는 isright() 메서드를 실행시킴
            if line in right_list:
                print('right')
                Maze.isright()
            # 5방향 센서에서 읽어오는 데이터가 왼쪽으로 턴할때의 센서 상태를 저장한
            # 이중리스트 안에 해당 값이 있으면 Maze 모듈에 있는 isleft() 메서드를 실행시킴
            elif line in left_list:
                print('left')
                Maze.isleft()
            # 5방향 센서에서 읽어오는 데이터가 유턴으로 턴할때의 센서 상태를 저장한
            # 이중리스트 안에 해당 값이 있으면 Maze 모듈에 있는 uturn() 메서드를 실행시킴
            elif line in uturn_list:
                print('uturn')
                Maze.uturn()

    except KeyboardInterrupt:
        # Ctrl+C키를 누를시,
        # 움직이는 구동체 작동 멈춤
        # 이 경우 Movement 모듈에 있는 pwm_low() 메서드 실행시킴
        Movement.pwm_low()