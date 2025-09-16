cup = 0
running = True

# while running:
#     cup += 1
#     print(cup)
#     if cup == 10:
#         # running = False(기존의 방식)
#         break
#
# print('while문 종료')

for i in range(1,10):
    if i == 3:
        continue
    if i == 6:
        continue
    if i == 9:
        continue
    print(i)


# continue 대신 else 활용
for i in range(1,10):
    if i in[3, 6, 9]:
        pass
    else:
        print(i)

# 3의 배수는 빼는 방법
for i in range(1,10):
    if i % 3 == 0 :
        continue
    print(i)
