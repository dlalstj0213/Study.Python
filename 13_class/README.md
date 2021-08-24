# 클래스

파이썬 또한 객체 지향 프로그래밍 언어이다.  

## 클래스 선언

    class 클래스 이름:
        클래스 내용

## 클래스 생성자 호출

    인스턴스 이름(변수 이름) = 클래스이름()

## 생성자 함수 정의 : `__init__()`

생성자(constructor)는 클래스 내부에 __init__이라는 함수를 만든다.  
생성자는 반드시 self 라는 매개변수를 받는다.

    class 클래스 이름:
        def __init__(self, 추가적인 매개변수):
            pass

- `self` : 자기 자신을 나타내는 딕셔너리
  - self가 가지고 있는 기능에 접근할 때는 `self.<식별자>` 형태로 접근한다.

> self는 키워드가 아니라 단순한 식별자로서 변수 이름으로 활용해도 정상 작동 한다.   
> 하지만 관례적으로 self를 사용하는 기본 관례를 지켜주는게 좋다.

- 클래스 생성자 예제 ([constructor_example/student.py](./constructor_example/student.py))  
- 클래스 생성자 호출 예제 ([constructor_example/main.py](./constructor_example/main.py))

> **소멸자** :
> 생성자와 반대로 인스턴스가 소멸될 때 호출되는 함수, 소멸자(destructor)  
> 많이 사용되는 기능은 아니지만 알아두자!  
> 소멸자는 클래스 내부에 `__del__(self)` 형태로 선언됨.  
> 클래스 생성자 예제에 소멸자 포함 ([constructor_example/student.py](./constructor_example/student.py))

## 멤버 함수 선언

메소드(method)란 클래스가 가지고 있는 함수를 뜻한다.  
파이썬은 클래스 메소드를 멤버 함수 또는 인스턴스 함수 등 용어로 주로 사용된다.

    class 클래스 이름:
        def 메소드 이름(self, 추가적인 변수):
            pass

- 메소드 예제 ([method_example/circle.py](./method_example/circle.py))

## 클래스 변수와 메소드

인스턴스가 속성과 기능을 가질 수도 있지만, 클래스가 속성(변수)과 기능(함수)을 가질 수 있다.

- 클래스 변수와 메소드 예제 ([class_val_func_example/student.py](./class_val_func_example/student.py))

### 클래스 변수 정의

    class 클래스 이름:
        클래스 변수 = 값

### 클래스 변수 접근

    클래스 이름.변수이름

### 클래스 함수 정의

    class 클래스 이름:
        @classmethod
        def 클래스 함수(cls, 매개변수):
            pass

### 클래스 함수 호출

    클래스 이름.함수 이름(매개변수)

## 가비지 컬렉터

가비지 컬렉터(garbage collector)란 더 사용할 가능성이 없는 데이터를 메모리에서 제거하는 약할을 한다.  
자바에도 가비지 컬렉터가 있드시 파이썬에도 가비지 컬렉터가 존재하여  
프로그래밍 언어의 내부에서 일어나는 일을 개발자가 크게 신경 쓰지 않아도 프로그램을 만들 수 있다.

## 더 알아보기

### 📌 [클래스 사용](./class.ipynb)
### 📌 [심화: 메타 클래스](./meta_clazz.ipynb)
### 📌 [활용: dataclasses](./dataclazzes.ipynb)
### 📌 [활용: Enum](./e_n_u_m.ipynb)