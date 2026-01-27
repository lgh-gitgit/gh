#n = [-32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2]
#print(n[1: : 2])



#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(a[::-1])




#date = "20251231"
#print(f"{date[0:4]}년 {date[4:6]}월 {date[6:]}일")


#nums = [1, 2, 3, 4, 5]
#print( (nums[0]+nums[1]+nums[2]+nums[3]+nums[4])/len(nums))


#a = [1, 2, ['a', 'b', ['Life', 'is']]]
#print(a[2][2][0])



#string = "삼성전자/naver/포스코"
#a = [string[0:4], string[5:10], string[11:]]
#print(a)




#movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
#movie_rank.insert(1, "슈퍼맨")
#print(movie_rank)




#A, B = input().split()
#print(int(A)+int(B))
#print(int(A)-int(B))
#print(int(A)*int(B))
#print(int(A)//int(B))
#print(int(A)%int(B))





#t = ('A', 'b', 'c')
#t = ('a', 'b', 'c')
#print(t)




#t = ('1등 오펜하이머', '2등 콘크리트', '3등 달짝지근해')
#print(t)



#key = {'메로나': [1000, 5], '돼지바': [800, 7], '월드콘': [1500, 4]}
#print(key['메로나'][1])





#print(28%4==0)

#print(28%7==0)
#print(28%4==0 and 28%7==0)

#a, b = input().split()
#a = int(a)
#b = int(b)
#print((a%2==0 and b%2==1) or (a%2==1 and b%2==0))
# 
# 
# 


# a = int(input())
# for _ in range(a):
#     print(a)



# a = int(input())
# for i in range(1, a+1):
#     print(i**2)







# a = 0
# for i in range(1, 101, 2):
#     a += i
# print(a)
# a=0
# for i in range(1, 101):
#     if i % 2== 0:
#         continue
#     a += i
# print(a)


# for a in range(2, 10):
#     print(f'"""""{a}단"""""')
#     for i in range(1, 10):
#         print(f"{a} * {i} =", a*i)


# a, b = input().split()
# a = int(a)
# b = int(b)
# def c():
#     if a>b:
#         return a
#     elif a<b:
#         return b
# print(c())

'''
입력을 받은 문자열의 문자의 수만큼 반복문을 돌려서 한 변수에 돌린 수를 저장
이 변수의 값을 출력
'''

# a = input()
# def len(k):
#     n=0
#     for _ in k:
    
#         n += 1 
#     return n
# print(len(a))




# a=50
# def g(k):
#     while k > 0:
#         k -= 1
#         print("파이썬")
# g(a)





# a = input()
# def k(n):
#     b =0
#     while b <51:
#         b += 1
#         print(n)
# k(a)








# a = input()
# def g(k):
#     u=0
#     while u<51:
#         u += 1
#         print(k)
#     return k[0]

# g(a)
# print(g(a))


# def multi(k):
#     for i  in range(1, 10):
#         print(f"{k} * {i} = {k*i}")




# def mmulti():
#     for i  in range(1, 10):
#         multi(i)

# mmulti()

# def df(*m):
#     b=0
#     for c in m:
#         b += c
#     print(b)

# df(1, 2, 3, 4, 5)



# a = input().split()
# c =input()
# def add():
#     b=0
#     for i in range(0,len(a)):
#         b += int(a[i])
#     print(b)

# def mul():
#     b=1
#     for i in range(0, len(a)):
#         b *= int(a[i])
#     print(b)
# if c == "add":
#     add()
# if c == "mul":
#     mul()

'''
객체지향:
음료수객체 
    특성: 가격, 이름
    기능: 선택하기, 음료수 수령하기
음료수 소개 객체
    특성: 음료수의 정보 z
    기능: 음료수의 정보 소개하기
주문객체
    특성: 음료수, 총 금액, 
    기능: 주문버튼 누르기, 선택한 음료수 보여주기, 가격 계산하기,
결제객체
    특성: 결제방식,
    기능: 결제방식 선택하기, 결제방식에 맞는 결제하기

상호작용: 음료수를 소개하는 객체를 통해 음료수 객체를 보여주기. 
        주문객체에서 주문버튼을 누를시 음료수 객체의 선택하기 기능을 통해
        선택한음료수를 주문객체의 선택한 음료수 보여주기 기능을 통해 보여준다
        음료수 객채의 가격 특성을 이용하여 주문객체의 가격 계산하기를 한다.
        결제 객체의 결제 방식 선택하기 기능을 통해 결제방식을 선택하고
        결제객테의 결제방식에 맞는 결제하기의 기능을 활용하여 결제방식에
        결제를 한다. 음료수객체의 음료수 수령하기 기능을 통해 음료수를 수령한다.
        
절차 지향:
1. 음료수 보여주기
2. 선태한 음료수 입력받기
3. 선택한 음료수를 저장한 변수에 입력된 음료수의 이름을 보여주고
    음료수의 가격을 더하여 보여준다.
4. 결제 방식의 종류를 보여주고 결제방식을 입력받는다.
5. 결제 방식에 맞게 결제 후 음료수를 수령한다.
'''

