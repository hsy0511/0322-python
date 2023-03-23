# 생성자

class fourcal: 
    
    def __init__(self,first,second): 
        self.first = first 
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    
a = fourcal(3,4)
print(a.add())