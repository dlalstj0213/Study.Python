# 힌트와 어노테이션

파이썬은 인터프리터가 코드를 실행하면서 타입을 추론하여 체크하기 때문에 매우 유연하게 프로그래밍을 할 수 있다.
하지만 타입이 유연하다는 것은 곧, 개발할때 매우 혼동을 줄 수 있다는 말과 같다. 

그래서 파이썬은 버전 3.5부터 **타입 어노테이션** 또는 **타입 힌드**를 제공한다.

간단한 파이썬 코드를 통해 예시를 들어보자.

```python
x = 10
print(type(x))
# <class 'int'>
x = "10"
print(type(x))
# <class 'str'>
```

위의 코드와 같이 해당 x 라는 변수에 어떤 타입의 값이 대입/선언 되느냐에따라 x 의 타입이 바뀐다.  
간단한 코드를 작성할시 크게 헤깔릴 일이 없지만, 긴 코드 작성이나, 복잡한 프로그래밍 설계, 대규모 어플리케이션 개발 등에서는 개발자가 변수의 타입을 추론하기 어려워지고 오류 발생시 디버깅하기도 쉽지 않다.

그래서 타입 힌트는 파이썬 코드를 작성할 때 타입에 대한 메타 정보를 제공한다. 타입 힌트가 없었을 당시 그저 주석을 다는 방식으로 해결해 나갔지만 주석은 표준화가 되어있지 않기 때문에 오히려 코드 가독성만 떨어뜨리는 경우도 있다.

즉, 타입 힌트는 파이썬 코드의 타입 표시를 표준화 하고 코드편집기(IDE)에서 해석할 수 있도록 고안되었으며, 코드 자동 완성이나 정적 타입 채킹에도 활용되고 있다.

### 주의점

타입 힌트는 오로지 타입에 대한 메타 정보를 공유하면서 개발을 보다 더 수월하게 해줄뿐 자바와 같이 실제로 추가한 타입 어노테이션이 부적합하다고 오류나 경고를 발생시키는 것이 아니다.

## 변수 타입 어노테이션

```python
name: str = "MinSeo"
age: int = 25
email: list = ["abc@mail.com", "def@email.com"]
address: dict = {"A": "a", "B": "b"}
```

## 함수 타입 어노테이션

콜론(`:`)과 화살표(`->`)를 사용할 때는 파이썬의 관행을 따라 콜론은 뒤에만 한 칸을 뛰우고, 화살표는 앞뒤로 한 칸을 띄운다.

    def 함수명( <필수 인자>: <인자 타입> ) -> <반환 타입>:
      ... 

```python
def func1(num: int) -> str:
  return str(num)

def func2(num1: int, num2: float = 3.5) -> float:
  return num1 + num2

def func3(name: str) -> None:
  print("Hi!")

def func4(value: str, times: int = 2) -> list:
  return [value] * times
```

## typing 모듈

내장 타입을 이용해서 좀 더 복잡한 타입 어노테이션을 추가할 때는 스탠다드 라이브러리의 typing 모듈을 사용할 수 있다.

```python
from typing import List, Set, Dict, Tuple

nums: List[int] = [1]

unique_nums: Set[int] = {6, 7}

vision: Dict[str, float] = {'left': 1.0, 'right': 0.9}

john: Tuple[int, str, List[float]] = (25, "John Doe", [1.0, 0.9])
```

## 사용자 정의 타입 힌팅

```python
class Student:
  ...

def func1(id: str) -> Student:
  ...

def func2(student: Student) -> Student:
  ...
```

## 타입 어노테이션 검사

작성한 타입 어노테이션을 검사하고 싶을 때는 `__annotations__` 내장 사전 객체를 사용할 수 있다.

```python
def func(name:str, age: int, address: str) -> None:
  ...

print(func.__annotations__)
# {'name': <class 'str'>, 'age': <class 'int'>, 'address': <class 'str'>, 'return': None}
```

## 더 알아보기

- [예시 코드](./main.py)