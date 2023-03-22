# 0322-python
# 클래스
## 클래스 객체
```python
class lol: 
    pass
a = lol()
b = lol()
```

## 객체 숫자 지정하기
```python
class fourcal:
    
    def setdata(self,first,second):
        self.first = first 
        self.second = second

a = fourcal()
a.setdata(4, 2)
print(a.first)
print(a.second)
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226783963-6e32fab2-02b4-4723-abe4-63c6d70804a5.png)

## 객체 2개 선언
```python
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
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784020-d015e80a-98d1-4dcd-a236-942d4dc7e945.png)

## 더하기 클래스
```python
class fourcal: 
    
    def setdata(self,first,second): 
        self.first = first 
        self.second = second
    def add(self):
        result = self.first + self.second
        return result


a = fourcal()
a.setdata(4,2)
print(a.add())
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784059-4623c215-f725-4735-b561-1468f1a51850.png)

## 곱하기 클래스
```python
class fourcal: 
    
    def setdata(self,first,second): 
        self.first = first 
        self.second = second
    def mul(self):
        result = self.first * self.second
        return result


a = fourcal()
a.setdata(4,2)
print(a.mul())
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784104-98ddc4a8-5655-45a1-b0a6-391056c88a5f.png)

## 빼기 클래스
```python
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
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784316-4de6c48a-5fcb-4e43-912d-b834911ac494.png)

## 나누기 클래스
```python
class fourcal: 
    
    def setdata(self,first,second): 
        self.first = first 
        self.second = second
    def div(self):
        result = self.first / self.second
        return result


a = fourcal()
a.setdata(4,2)
print(a.div())
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784348-1bb1d002-80ca-41cb-828c-633853089da0.png)

## 생성자
```python
class fourcal: 
    
    def __init__(self,first,second): 
        self.first = first 
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    
a = fourcal(3,4)
print(a.add())
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784368-33566e37-2225-45ff-8a8b-14c351b36c61.png)

## 클래스 상속
```python
class fourcal:
     def __init__(self, first, second):
        self.first = first
        self.second = second
     def setdata(self, first, second):
        self.first = first
        self.second = second
     def add(self):
        result = self.first + self.second
        return result
     def mul(self):
        result = self.first * self.second
        return result
     def sub(self):
        result = self.first - self.second
        return result
     def div(self):
        result = self.first / self.second
        return result

class morefourcal(fourcal):
    def pow(self): # 제곱 클래스
        result = self.first ** self.second
        return result
a = morefourcal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784420-54e78077-bd5f-42a5-80dd-1beef6216d2a.png)

## 오버라이딩
```python
class fourcal:
     def __init__(self, first, second):
        self.first = first
        self.second = second
     def setdata(self, first, second):
        self.first = first
        self.second = second
     def add(self):
        result = self.first + self.second
        return result
     def mul(self):
        result = self.first * self.second
        return result
     def sub(self):
        result = self.first - self.second
        return result
     def div(self):
        result = self.first / self.second
        return result
    
class safefourcal(fourcal):
    def div(self):
        if self.second==0:
            return 0 
        else:
            return self.first/self.second

a = safefourcal(4,0)
print(a.div())
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784488-7d2b4695-7c7d-42be-acba-65d5898099cf.png)

## 클래스 변수
```python
class family:
    firstname = "허"

print(family.firstname)
a = family()
print(a.firstname)

```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226784534-c5e32036-ef10-41c6-b4bb-8c1587cec2a1.png)
