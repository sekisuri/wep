'''
최대 공약수 구하기
1.사용자로부터 최대 공약수를 구할 두 수를 입력받아 변수에 저장
2.두 변수를 비교하여 더 작은 값을 찾고 그 값을 t_num변수에 저장
3.tm_num의 값을 하나씩 감소시키면서 입력받은 두 수와 딱 나누어 떨어지는 수를 찾는다.
4.딱 떨어지는 수를 찾으면 딱 떨어지는 수(최대공약수)를 출력하고,break를 이용해 반복문을 멈춘다.

예)
첫번째 숫자를 입력하세요: 99
두번째 숫자를 입력하세요: 66

출력 :
두 수의 최대공약수는 33 입니다.
'''
#!/usr/bin/python3

number1 = int(input('첫번째 숫자를 입력하세요: '))
number2 = int(input('두번째 숫자를 입력하세요: '))

if number1 > number2:
    t_num = number2
else:
    t_num = number1

sumcheck = False; 
while t_num > 1 :
    if number1 % t_num == 0 and number2 % t_num == 0:
        print('두 수의 최대 공약수는 %d 입니다 '%t_num)
        sumcheck = True
        break
    t_num -= 1

if sumcheck == False:
    print('두 수의 최대 공약수는 없습니다.')


