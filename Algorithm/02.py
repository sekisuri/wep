#!/usr/bin/python3
number = int(input('1 이상의 숫자를 입력하세요: '))
divisors = []
t_num = int(number / 2)
while t_num > 1 :
    if number % t_num == 0 :
        t_num
        divisors.append(t_num)
    t_num -= 1

print(divisors)