'''
6. 여러 개의 숫자 중에서 가장 긑 값과 작은 값 구하기

1.
2. 
'''

#!/usr/bin/python3

inlist = [12,42,32,51,23,25,22]
'''
1.가장 큰 값을 저장할 변수 하나를 0으로 초기화시켜 생성합니다.
2.for문에 생성한 리스트를 넣어주고 하나씩 max변수와 비교해서 max변수보다 클 경우 임의의 변수를
해당 리스트의 요소로 바꿔줍니다.
'''
def max_value():
    max = 0
    for i in inlist:
        if i > max:
            max = i
    print(max)
'''
1.가장 작은 값을 저장할 변수 하나를 0으로 초기화시켜 생성합니다.
2. for문에 생성한 리스트를 넣어주고 하나씩 min변수와 비교해서 min변수보다 작을 경우 임의의 변수를 
해당 리스트의 요소로 바꿔줍니다.
'''
def min_value():
    min = inlist[0]
    for i in inlist:
        if i < min:
            min = i
    print(min)

def main_menu():
    print('list value [12,42,32,51,23,25,22]')
   
    print('최대값')
    max_value()
    print('최소값')
    min_value()
    
main_menu()



    
