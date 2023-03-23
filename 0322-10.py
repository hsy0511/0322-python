# 오버라이딩

class fourcal:
     
     def setdata(self, first, second):
        self.first = first
        self.second = second
     def add(self):
        result = self.first + self.second
        return result
     
    
class safefourcal(fourcal):
   def div(self):
      return self.first/self.second

a = safefourcal(3,5)
print(a.div())
