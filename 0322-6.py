# 빼기 클래스

class fourcal: 
    
    def setdata(self,first,second): 
        self.first = first 
        self.second = second
    def sub(self):
        result = self.first - self.second
        return result


a = fourcal()
a.setdata(4,2)
print(a.sub())