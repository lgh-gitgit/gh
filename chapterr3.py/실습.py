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


for a in range(2, 10):
    print(f'"""""{a}단"""""')
    for i in range(1, 10):
        print(f"{a} * {i} =", a*i)
        
    