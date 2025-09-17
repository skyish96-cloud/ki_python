# indexing
# - 연속적인 객체 (list, tuple, 문자열)에 부여된 번호를 이용해서 값을 가져오는데 사용하는 것을 의미 한다.
ls = [1,2,3,]
print(ls[0])
print(ls[1])
print(ls[2])

str = 'hello python!!'
print(str[4])
# 특정 값을 가져오는 것 - 첨자를 이용하여 특정 위치의 값을 가져온다.

# slicing
# - 연속된 객체 (list, tuple, 문자열)에 부여된 번호를 이용하여 범위의 값을 추출하는 것을 의미한다.
ls =[1,2,3,4,5,6,7,8,9]

#list[start:end:step] 의 형식
# - start : 범위의 시작 위치 값, 스타트위치에 아무것도 없으면 처음부터
# - end : 범위의 끝 위치 값 -1, 엔드위치에 아무것도 없으면 끝까지
# - step : 기본값은 1이고 생략 가능
print(ls[0:4]) # 1, 2, 3, 4, (index : 0~3)
print(ls[0:4:1])
print(ls[::]) # 처음부터 끝까지 1씩 인덱스 값을 이동하여 가져오기
print(ls[::2])
print(ls[::3])
print(ls[::-1])  # 역순으로 가져오기, start 는 마지막 인덱스
print(ls[6::-1]) # end는 처음 인덱스