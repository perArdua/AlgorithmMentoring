import code
import string
import sys
import re
from collections import deque
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = MIS()

str = input().rstrip()

number = re.findall('[0-9]+', str)
number = deque(map(int, number))
# print(number)

oper = re.findall('[A-Z]',str)
oper = deque(oper)

if 'C' not in str:
    print("NO OUTPUT")
    exit()

if oper[-1] != 'C':
    try:
        a = int(str[-1])
        # print(a)
    except:
        print("NO OUTPUT")
        exit()


while oper:
    operator_symbol = oper.popleft()
    # print("현재 연산자 :", operator_symbol)
    if operator_symbol != 'C':
        num1 = number.popleft()
        num2 = number.popleft()
        
        # print("숫자1: ",num1, "숫자2: ",num2)
    if operator_symbol == 'S':
        temp = num1 - num2
        number.appendleft(temp)

    elif operator_symbol == 'M':
        temp = num1 * num2
        number.appendleft(temp)

    elif operator_symbol == 'U':
        if num1 < 0 and num2 > 0:
            num1 *= -1
            temp = (num1 // num2) * -1
        else:
            temp = num1 // num2
        number.appendleft(temp)
    
    elif operator_symbol == 'P':
        temp = num1 + num2
        number.appendleft(temp)
    
    else:
        if oper:
            print(number[0], end=" ")
        else:
            print(number[0], end="")