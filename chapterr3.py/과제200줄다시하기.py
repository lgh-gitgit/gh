china = "중국집"


china_menu = ["짜장면", "탕수육", "짬뽕"]
china_price = {"짜장면" : 5000, "탕수육" : 4000, "짬뽕" : 3000}


customer = input()

if customer == china:
    print("중국집을 선택하셨습니다.")

def order(k):
    for i in k:
        if i in china_menu:
            print(f"{i}, 이 메뉴들은 준비해드리겠습니다.")
        else:
            print("이 메뉴들은 준비되어 있지 않습니다 다시 주문 해주세요")
a = 0

if customer == china:
    print("메뉴를 보여드리겠습니다 :", end = ' ')
    for i in china_menu:
            print(i, end = ' ')
    b =input().split()
    while True:
        order(b)
        break
    for i in b:
        a += china_price[i]
    print(a)