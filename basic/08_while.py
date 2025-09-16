cup = 0

""" 조건이 무조건 참이 될 경우 영원히 실행 되므로 멈출 수 없다.
while True:
    cup = cup + 1
    print(cup)
"""

while cup < 10:
    print(cup)
    # 컵이 0이라서 10이 되기 위해서 계속 돌아간다.
    # cup의 변수를 증가시키는 부분이 없음 그래서 무한루프에 빠지게 된다.
    # cup = 0 이라면, 조건 cup < 10은 항상 참(true)이라서 print(cup)만 무한히 실행된다.
while cup < 10:
    cup = cup + 1
    print(cup)
    # 컵이 1씩 추가되는 동작이 생긴다
    # cup이 10에 도달하면 반복이 종료된다.