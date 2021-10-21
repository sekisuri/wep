'''
피보나치 수열 구하기

1.사용자로부터 출력하고 싶은 값을 입력받고 변수에 저장합니다. 
2.피보나치 수열은 0과 1부터 시작하기 때문에 피보나치 수열을 저장할 리스트를 생성해서 미리 0과 1을 넣어둡니다. 
3.fibo리스트에 0과 1일 이미 들어있기 때문에 range함수의 시작을 2로 합니다. 
    0과 1을 더한 값을 시작으로 피보나치 수열을 구합니다.
4. 구해진 피보나치 수열이 저장된 리스트를 출력합니다.

예)
몇개의 피보나치 수열 항을 출력할까요? : 17
출력 :
0
1
1
2
3
5
'''

#!/usr/bin/python3

number = int(input('몇 개의 피보나치 수열 항을 출력할까요?'))
Fibonacci = [0,1]
for i in range(2,number):
    f1 = Fibonacci[i-2]
    f2 = Fibonacci[i-1]
    Fibonacci.append(f1 + f2)

for f in Fibonacci:
    print(f)