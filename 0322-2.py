# 객체의 숫자 지정하기

class fourcal: # pass말고 setdata가 들어갔다. 클래스 안에서 구현된 함수는 메서드
    
    def setdata(self,first,second): # 메서드 매개변수, self는 메서드에서 호출한 객체 a가 자동 전달 되어있음
        self.first = first # 메서드 수행문
        self.second = second

a = fourcal()
a.setdata(4, 2)
print(a.first)
print(a.second)