# 0322-python
# 클래스
변수와 함수를 많이 늘리지 않고 단순하게 쓰기 위해서 클래스를 사용한다.
## 클래스 객체
```python
class lol: 
    pass
a = lol()
b = lol()
```
class를 써서 클래스를 만들고 만든 클래스 밖에 객체를 만든다.

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

클래스 내부 함수를 사용하여 3개의 값을 받는다. 이때 첫번째 있는 값은 특별한 의미를 갖는다.(클래스 내부 함수는 메서드라고 한다)

객체를 통해 메서드를 호출할 때 도트(.) 연산자를 사용하고, 메서드에 첫번째 self 값은 메서드를 호출할 때 사용하는 a 객체에 자동으로 전달된다.

즉 a.first 값은 self.first 값과 같기 때문에 4가 출력되고, a.second는 2가 출력된다.
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

객체를 두개를 선언 할 때는 메서드 호출을 두번 하면 된다. 
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

add 메서드를 추가하여 result 값을 self.first와 self.second 값을 더한 값으로 리턴시켜 더해준다.
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

mul 메서드를 추가하여 result 값을 self.first과 self.second 값을 곱한 값으로 리턴시켜 더해준다.
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

sub 메서드를 추가하여 result 값을 self.first과 self.second 값을 뺀 값으로 리턴시켜 더해준다.
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

div 메서드를 추가하여 result 값을 self.first과 self.second 값을 나눈 값으로 리턴시켜 더해준다.
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

생성자라는 객체가 생성될때 자동으로 호출되는 메서드를 의미한다.
생성자 ( __ init __ )는 setdata와 동일하게 작용한다. 다른것은 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.
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

class 메소드()에 ()안에 상속할 클래스를 넣어주면 상속이 된다.
상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
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

객체 메서드()에 () 안에 값을 넣으면 오버라이딩이 된다.
오버라이딩은 부모클래스의 메서드 대신 오버라이딩 메서드를 입력받는 것이다.
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

클래스이름.클래스변수로 사용할 수 있다.
클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.

## super 함수
