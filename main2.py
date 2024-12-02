# 문제1 무한 Generator

def Generator():
    num = 0
    while num <= 10:
        yield num
        num += 1

gen = Generator()
for number in gen:
    print(number)

# 문제 2 제너레이터와 코루틴 결합

# 무한히 숫자를 생성하는 제너레이터
def Generator():
    num = 0
    while True:
        yield num
        num += 1

# 값을 받아서 2를 곱하는 코루틴
def multiplier():
    while True:
        num = (yield)  # 값이 전달되기를 기다린다
        if num is not None:  # None 체크
            yield num * 2  # 전달받은 값에 2를 곱해 반환

# 제너레이터와 코루틴을 결합
gen = Generator()  # 숫자를 생성하는 제너레이터
co = multiplier()  # 값을 받아 처리하는 코루틴

next(co)  # 코루틴을 첫 번째 yield 지점까지 실행 (이후 값을 기다림)

# 제너레이터에서 값을 받아 코루틴으로 보내고 그 값을 처리하여 출력
for number in gen:
    result = co.send(number)  # 제너레이터에서 값을 받아 코루틴에 전달
    if result is not None:  # 결과가 None이 아닌 경우에만 출력
        print(result)  # 코루틴에서 처리된 값 출력
    if number >= 10:  # 숫자가 10 이상이면 종료
        brea

# 문제3 텍스트 처리 시스템

# 배경화면에 text01이라는 파일에 라는 python 글을 찾아 대문자로 출력

def trxt0(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip()  # 줄 끝의 공백을 제거하고 반환

# 코루틴: 텍스트에서 특정 키워드를 필터링하고 대문자로 변환하는 함수
def filter_and_uppercase(keyword):
    while True:
        line = (yield)  # 줄을 받는다
if keyword in line:  # 특정 키워드가 줄에 포함되어 있다면
yield line.upper()  # 대문자로 변환하여 반환

# 파일 경로
file_name = "C:/Users/knuser/Desktop/text01.txt"
keyword = "python"  # 필터링할 키워드

# 제너레이터와 코루틴 결합하여 처리
gen = trxt0(file_name)  # 텍스트 파일에서 한 줄씩 읽는 제너레이터
co = filter_and_uppercase(keyword)  # 키워드를 필터링하고 대문자 변환하는 코루틴

next(co)  # 코루틴을 첫 번째 yield 지점까지 실행 (값을 받을 준비)

# 제너레이터에서 한 줄씩 읽어 코루틴으로 전달하고 필터링된 결과 출력
for line in gen:
    result = co.send(line)  # 제너레이터에서 읽은 줄을 코루틴에 전달
if result is not None:  # 결과가 None이 아니면 출력
print(result)
