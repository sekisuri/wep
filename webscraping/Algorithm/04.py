'''
최소 공배수 구하기

1.사용자로부터 최소 공배수를 구할 두 수를 입력받아 변수에 저장
2.두 변수를 비교해서 더 큰 값을 찾고 그 값을 t_num 변수에 저장
3.t_num의 값을 하나씩 증가시키면서 입력받은 두 수와 딱 나누어쩔어지는 수를 찾습니다.
4. 딱 떨어지는 수를 찾으면 딱 떨어지는 수(최소공배수)를 출력하고, break를 이용해 반복문을 멈춤니다.

예)
첫번째 숫자를 입력하세요: 12
두번째 숫자를 입력하세요: 15

출력 :
두 수의 최소공배수는 60 입니다.
'''

#!/usr/bin/python3

number1 = int(input('첫번째 숫자를 입력하세요: '))
number2 = int(input('두번째 숫자를 입력하세요: '))

if number1 > number2:
    t_num = number2
else:
    t_num = number1

sumcheck = False; 
while t_num :
    if t_num % number1 == 0 and t_num % number2 == 0:
        print('두 수의 최소 공배수는 %d 입니다 '%t_num)
        sumcheck = True
        break
    t_num += 1

if sumcheck == False:
    print('두 수의 최소 공배수는 없습니다.')

