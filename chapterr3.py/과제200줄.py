'''
상황에 맞게 200줄 코드 만들기
-지역의 음식점에서 배달을 시키는 상황
 지역에는 중식점, 양식점, 한식점, 일식점이 있다
 중식점에는 짜장면 짬뽕 간짜장 탕수육 군만두 
 세트메뉴: 세트 A: 짜장 + 짬뽕 + 군만두(군만두는 
 탕수육으로 변경 가능)
          세트 B: 간짜장(짜장) + 짬뽕 + 탕수육
 양식점에는 파스타 스파게티 감바스 스테이크
 (미디움, 레어, 웰던)
 한식점에는 비빔밥 된장찌개(공기밥) 김치찌개
 (공기밥) 함박 스테이크 
 추가메뉴: 공기밥, 계란찜, 콜라, 사이다.
 일식점에는 초밥 라멘 오니기리 차완무시
 추가: 라멘 맵기 조절 가능 (1단계, 2단계, 3단계)
 초밥 종류: 연어초밥 참치초밥 새우초밥
- 모든 음식점은 주문 완료하기 전에 일회용 숟가락을
 받는지의 여부 확인
 모든 주문을 받을 때 그 메뉴가 있는지 확인
 각각의 음식점에 대한 평가 별점 1~5개
'''
china = "중국집"
west = "양식집"
korea = "한식집"
japan = "일식집"

china_menu = ["짜장면", "짬뽕", "간짜장", "탕수육", "군만두", "세트메뉴A", "세트메뉴B"]
west_menu = ["파스타", "스파게티", "감바스", "스테이크",]
korea_menu = ["비빔밥", "된장찌개", "김치찌개", "함박스테이크",]
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
        if china_pick == "세트메뉴A":
            print("세트메뉴A의 군만두를 탕수육으로 변경할 수 있습니다. 변경 하시겠습니까?, y or x", end = ' ')
            a = input()
            if a == "y":
                print("군만두를 탕수육으로 변경하겠습니다.", end = ' ')
            elif a == "x":
                print("변경하지 않겠습니다.", end = ' ')
        elif china_pick == "세트메뉴B":
            print("세트메뉴B의 간짜장을 짜장으로 변경할 수 있습니다. 변경 하시겠습니까?, y or x", end = ' ')
            c = input()
            if c == "y":
                print("간짜장을 짜장으로 변경하겠습니다.", end = ' ')
            elif c == "x":
                print("변경하지 않겠습니다.", end = ' ')   
        print("일회용 숟가락을 받으시겠습니까?, y or x", end = ' ')
        f = input()
        if f == "y":
            print("일회용 숟가락을 넣어드리겠습니다. 음식을 만들고 있습니다.", end = ' ')
        elif f == "x":
            print("일회용 숟가락을 빼드리겠습니다. 음식을 만들고 있습니다.", end = ' ') 
    else:
        print(f"{china_pick}같은 메뉴는 준비되어 있지 않습니다.", end = '')
        print("다른 메뉴를 주문해 주세요")
        b = input()
        if b in china_menu:
            print(f"{b}, 이 메뉴들을 준비해드리겠습니다.", end = ' ')
        else:
            while True:
                print(f"{china_pick}같은 메뉴는 준비되어 있지 않습니다.", end = '')

if customer == west:
    print("메뉴를 보여드리겠습니다 :", end = ' ')
    for i in west_menu:
         print(i, end = ' ')
    west_pick = input()
    if west_pick in west_menu:
        print(f"{west_pick}, 이 메뉴들을 준비해 드리겠습니다.")
        if west_pick == "스테이크":
            print("스테이크의 굽기를 선택해주세요, 스테이크는 레어, 미디움레어, 미디움, 미디움웰던, 웰던이 있습니다.", end = ' ')
            d = input()
            if d == "레어":
                print("스테이크를 레어로 굽겠습니다.", end = ' ')
            elif d == "미디움레어":
                print("스테이크를 미디움레어로 굽겠습니다.", end = ' ')
            elif d == "미디움":
                print("스테이크를 미디움으로 굽겠습니다.", end = ' ')
            elif d == "미디움웰던":
                print("스테이크를 미디움웰던으로 굽겠습니다.", end = ' ')
            elif d == "웰던":
                print("스테이크를 웰던으로 굽겠습니다.", end = ' ') 
        print("일회용 숟가락을 받으시겠습니까?, y or x", end = ' ')
        f = input()
        if f == "y":
            print("일회용 숟가락을 넣어드리겠습니다. 음식을 만들고 있습니다.", end = ' ')
        elif f == "x":
            print("일회용 숟가락을 빼드리겠습니다. 음식을 만들고 있습니다.", end = ' ')    
    else:
        print(f"{west_pick}같은 메뉴는 준비되어 있지 않습니다.", end = '')
        print("다른 메뉴를 주문해 주세요")
        e = input()
        if e in west_menu:
            print(f"{e}, 이 메뉴들을 준비해드리겠습니다.")
        else:
            print("다른 음식점에서 주문해주시길 바랍니다.")
if customer == korea:
    print("메뉴를 보여드리겠습니다 :", end = ' ')
    for i in korea_menu:
         print(i, end = ' ')
    korea_pick = input()
    if korea_pick in korea_menu:
        print(f"{korea_pick}, 이 메뉴들을 준비해 드리겠습니다.")
        print("추가메뉴가 있습니다. 주문하시겠습니까?, y or x", end = ' ')
        h = input() 
        if h == "y":
            print("추가메뉴를 선택하셨습니다. 추가메뉴에는 공기밥 계란찜 콜라 사이다가 있습니다. 무엇을 선택하시겠습니까?",end = ' ')
            u = input()
            if u == "공기밥":
                print("공기밥을 추가 주문하셨습니다.")
            elif u == "계란찜":
                print("계란찜을 추가 주문하셨습니다.")
            elif u == "콜라":
                print("콜라를 추가 주문하셨습니다.")
            elif u == "사이다":
                print("사이다를 추가 주문하셨습니다.")
        elif h == "x":
            print("추가메뉴를 주문하지 않으셨습니다.", end = ' ')
        print("일회용 숟가락을 받으시겠습니까?, y or x", end = ' ')
        f = input()
        if f == "y":
            print("일회용 숟가락을 넣어드리겠습니다. 음식을 만들고 있습니다.", end = ' ')
        elif f == "x":
            print("일회용 숟가락을 빼드리겠습니다. 음식을 만들고 있습니다.", end = ' ')    
    else:
        print(f"{korea_pick}같은 메뉴는 준비되어 있지 않습니다.", end = ' ')
        print("다른 메뉴를 주문해 주세요")
        z = input()
        if z in korea_menu:
            print(f"{z}, 이 메뉴들을 준비해드리겠습니다.")
        else:
            print("다른 음식점에서 주문해주시길 바랍니다.")
if customer == japan:
    print("메뉴를 보여드리겠습니다 :", end = ' ')
    for i in japan_menu:
         print(i, end = ' ')
    japan_pick = input()
    if japan_pick in japan_menu:
        print(f"{japan_pick}, 이 메뉴들을 준비해 드리겠습니다.")
        print("추가메뉴가 있습니다. 주문하시겠습니까?, y or x", end = ' ')
        h = input()
        if h == "y":
            print("추가메뉴에는 라멘의 맵기 조절과 초밥의 종류 선택이 있습니다. 무엇을 선택하시겠습니까?", end = ' ')
            a = input()
            if a == "라멘의 맵기 조절":
                print("라멘의 맵기를 선택해주세요, 라멘은 1단계, 2단계, 3단계가 있습니다.", end = ' ')
                d = input()
                if d == "1단계":
                    print("라멘을 1단계로 준비하겠습니다.", end = ' ')
                elif d == "2단계":
                    print("라멘을 2단계로 준비하겠습니다.", end = ' ')
                elif d == "3단계":
                    print("라멘을 3단계로 준비하겠습니다.", end = ' ')
            elif a == "초밥의 종류":
                print("초밥의 종류를 선택해주세요, 초밥은 연어초밥, 참치초밥, 새우초밥이 있습니다.", end = ' ')
                k = input()
                if k == "연어초밥":
                    print("연어초밥으로 준비하겠습니다.", end = ' ')
                elif k == "참치초밥":
                    print("참치초밥으로 준비하겠습니다.", end = ' ')
                elif k == "새우초밥":
                    print("새우초밥으로 준비하겠습니다.", end = ' ')
        print("일회용 숟가락을 받으시겠습니까?, y or x", end = ' ')
        f = input()
        if f == "y":
            print("일회용 숟가락을 넣어드리겠습니다. 음식을 만들고 있습니다.", end = ' ')
        elif f == "x":
            print("일회용 숟가락을 빼드리겠습니다. 음식을 만들고 있습니다.", end = ' ')
    else:
        print(f"{japan_pick}같은 메뉴는 준비되어 있지 않습니다.", end = '')
        print("다른 메뉴를 주문해 주세요")
        z = input()
        if z in japan_menu:
            print(f"{z}, 이 메뉴들을 준비해드리겠습니다.")
        else:
            print("다른 음식점에서 주문해주시길 바랍니다.")
    
print("음식점에 대한 평가를 남겨주세요. 어떤 음식점에서 주문을 하셨나요?", end = ' ')
o = input()
if o == "중국집":
    print("중국집에 대한 평가를 별 1~5개로 평가해주세요.", end = ' ')
    t = input()
    if t == "1":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "2":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "3":
        print("저희 음식을 주문해주셔서 감사합니다.", end = ' ')
    elif t == "4":
        print("맛있게 드셔주셔서 감사합니다.")
    elif t == "5":
        print("감사합니다.")
if o == "양식집":
    print("양식집에 대한 평가를 별 1~5개로 평가해주세요.", end = ' ')
    t = input()
    if t == "1":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "2":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "3":
        print("저희 음식을 주문해주셔서 감사합니다.", end = ' ')
    elif t == "4":
        print("맛있게 드셔주셔서 감사합니다.")
    elif t == "5":
        print("감사합니다.")
if o == "한식집":
    print("한식집에 대한 평가를 별 1~5개로 평가해주세요.", end = ' ')
    t = input()
    if t == "1":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "2":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "3":
        print("저희 음식을 주문해주셔서 감사합니다.", end = ' ')
    elif t == "4":
        print("맛있게 드셔주셔서 감사합니다.")
    elif t == "5":
        print("감사합니다.")
if o == "일식집":
    print("일식집에 대한 평가를 별 1~5개로 평가해주세요.", end = ' ')
    t = input()
    if t == "1":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "2":
        print("죄송합니다. 앞으로 더 노력하겠습니다.", end = ' ')
    elif t == "3":
        print("저희 음식을 주문해주셔서 감사합니다.", end = ' ')
    elif t == "4":
        print("맛있게 드셔주셔서 감사합니다.")
    elif t == "5":
        print("감사합니다.")
    










        
