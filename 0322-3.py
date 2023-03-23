# 객체 2개 선언

class fourcal:
    def setdata(self,first,second):
        self.first = first
        self.second = second


a = fourcal()
b = fourcal()
a.setdata(4,2)
print(a.first)
b.setdata(3,7)
print(b.first)