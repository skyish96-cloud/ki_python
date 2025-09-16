# 산술연산자
# +, -, *, /, //, %, **
num1 = 7
num2 = 5
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

# 관계연산자
# >, <, >=, <=, ==, !=
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

# 대입 연산자
# =

# 복합 대입 연산자
# +=, -=, *=, /=, //=, %=, **=
num1 = 7
num2 = 5
num1 += num2 # num1 = 7 + 5
print(num1)
num1 -= num2 # num1 = 12 - 5
print(num1)
num1 *= num2 # num1 = 7 * 5
print(num1)
num1 /= num2 # num1 = 35 / 5
print(num1)
num1 //= num2 # num1 = 7 / 5 (몫)
print(num1)
num1 %= num2 # num1 = 1 / 5 (나머지)
print(num1)
num1 **= num2 # num1 = 1 ** 5
print(num1)

# 논리 연산자
# and, or, not
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not(True))
print(not(False))

num = 5
# and 는 포함 범위에 사용된다.
print(num >= 0 and num <= 100)
# and 의 포함 범위는 함축적으로 사용할 수 있다.
print(0 >= num <= 100)
# or 는 제외 범위에 사용된다.
print(num < 0 or num > 100)




