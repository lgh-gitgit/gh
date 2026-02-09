'''
카트 특성
1. 바퀴의 모양
2. 엔진의 소리
3. 카트의 크기
4. 최대속도
5. 제동거리
6. 엔진 종류
7. 카트의 가격
8. 카트의 사용기간
9. 카트의 구매기간
10. 카트의 부스터 이팩트
11. 카트의 가능한 색(list)
12. 카트의 색(str)
13. 카트의 종류
14. 카트의 가속도
15. 카트의 x좌표
16. 카트의 y좌표 
카트의 기능
1. 속력의 조절(앞으로 가기, 뒤로가기, 양옆으로 이동)
2. 멈추기
3. 부스터 쓰기
4. 위치가 변화한다.
'''








class cart:
    def __init__(self, max, color, accel, x=0,y=0):
        self.max=max
        self.color=color
        self.accel=accel
        self.x=x
        self.y=y
    def direction(self, k):
        return k
    def accel_(self):
            
    # def boost_(self, b):
    #     a = self.accel
    #     a += b
    #     self.x += a
    #     self.y += a
    #     print(self.x, self.y)
    # def 
cart_1 = cart(100, "빨간색", 10)
a= input().split()
cart_1.direction(a)