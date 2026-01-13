'''
상황에 맞게 200줄 코드 만들기
-지역의 음식점에서 배달을 시키는 상황
 지역에는 중식점, 양식점, 한식점, 일식점있다
 중식점에는 짜장면 짬뽕 간짜장 탕수육 군만두 
 세트메뉴: 세트 A: 짜장 + 짬뽕 + 군만두(군만두는 
 탕수육으로 변경 가능)
          세트 B: 간짜장 + 짬뽕 + 탕수육
 양식점에는 파스타 스파게티 감바스 스테이크
 (미디움, 레어, 웰던)
 한식점에는 비빔밥 된장찌개(공기밥) 김치찌개
 (공기밥) 함박 스테이크 
 추가메뉴: 공기밥
 일식점에는 초밥 라멘 오니기리 차완무시
 추가: 라멘 맵기 조절 가능 (1단계, 2단계, 3단계)
- 모든 음식점은 주문 완료하기 전에 일회용 숟가락을
 받는지의 여부 확인
 모든 주문을 받을 때 그 메뉴가 있는지 확인
'''
china = "중국집"
west = "양식집"
korea = "한식집"
japan = "일식집"

china_menu = ["짜장면", "짬뽕", "간짜장", "탕수육", "군만두", "세트메뉴A", "세트메뉴B"]
west_menu = ["파스타", "스파게티", "감바스", "스테이크"]
korea_menu = ["비빔밥", "된장찌개", "김치찌개", "함박스테이크", "공기밥"]
japan_menu = ["초밥", "라멘", "오니기리", "차완무시"]

customer = input()

if customer == china:
    print("중국집을 선택하셨습니다.")
elif customer == west:
    print("양식집을 선택하셨습니다.")
elif customer == korea:
    print("한식집을 선택하셨습니다.")
elif customer == japan:
    print("일식집을 선택하셨습니다.")

if customer == china:
    print("메뉴를 보여드리겠습니다 :", end = ' ')
    for i in china_menu:
         print(i, end = ' ')

china_pick = input()
if china_pick in china_menu:
    print(f"{china_pick}, 이 메뉴들을 준비해 드리겠습니다.")
else:
    print(f"{china_pick}같은 메뉴는 준비되어 있지 않습니다.")
    print("다른 메뉴를 주문해 주세요")
    b = input()
    if b in china_menu:
        print(f"{b}, 이 메뉴들을 준비해드리겠습니다.")
    else:
        print("다른 음식점에서 주문해주시길 바랍니다.")
        
