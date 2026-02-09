'''
- 다음의 요구사항을 만족하면 됩니다.
    1. 사용자로부터 연산자(+, -, *, /)를 입력받는다. 
    만약 '종료'라는 문자열을 입력받으면 프로그램이 종료되어야 한다.
    2. 사용자로부터 두 개의 숫자를 입력받는다.
    3. 입력받은 연산자에 따라 두 숫자에 대한 연산을 수행하고 그 결과를 출력한다.
    4. 만약 사용자가 0으로 나누는 연산을 시도하면, "0으로 나눌 수 없습니다."
    라는 메시지를 출력하고 다시 연산자와 숫자를 입력받는다.
    5. 사용자가 지원하지 않는 연산자를 입력하면, "지원하지 않는 연산자입니다."
    라는 메시지를 출력하고 다시 연산자와 숫자를 입력받는다.



'''
def calculator(m, k, p):
        if m == "+":
            print(k+p)
        elif m == "-":
            print(k-p)
        elif m == "*":
            print(k*p)
        elif m == "/":
            if p == 0:
                print("0으로 나눌 수 없습니다.")
            else:
                print(k/p)

def git(m):
    if m != "+" and m != "*" and m!= "/" and m != "-":
        if m == "종료":
            sys.exit()
        else:
            print("사용할 수 없는 연산자입니다.")

    
            
    

while True:
    c = input()
    if c != "+" and c != "*" and c!= "/" and c != "-":
       if c == "종료":
           break
       else:
           print("사용할 수 없는 연산자입니다.")
    a, b  = input().split()
    a = int(a)
    b = int(b)
    calculator(c , a, b)

