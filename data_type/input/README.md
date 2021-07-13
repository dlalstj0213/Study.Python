## 목차

- [사용자 입력 `input()`](#사용자-입력-input)
  - [`input()` 함수로 입력 받기](#input-함수로-입력-받기)
  - [`input()` 입력 결과의 자료형](#input-입력-결과의-자료형)
  - [자료형변환 (타입 캐스팅, Type Casting)](#자료형변환-타입-캐스팅-type-casting)
    - [문자열을 숫자로 변환하기](#문자열을-숫자로-변환하기)
    - [`ValueError` 예외](#valueerror-예외)
    - [숫자를 문자로 변환하기](#숫자를-문자로-변환하기)

# 사용자 입력 `input()`

- 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 `input()` 함수를 사용한다.

## `input()` 함수로 입력 받기

```python
result = input("아무거나 입력해주세요 > ")
print("typed result : " + result)
# 결과 :
# 아무거나 입력해주세요 > 1일2이3삼
# typed result : 1일2이3삼
```

- `input()` 함수를 사용할시 입력 대기를 알려주는 커서가 생기면서 사용자가 입력을 완료할 때까지 프로그램이 잠시 멈춰있는다.
- 사용자가 입력을 완료하면 나머지 코드를 실행한다.

## `input()` 입력 결과의 자료형

```python
result = input("아무거나 입력해주세요 > ")
print("type of result :", result)
# 결과 : 문자 입력시
# tpye of result : <class 'str'>
# 결과 : 1234 입력시
# tpye of result : <class 'str'>
# 결과 : True 입력시
# tpye of result : <class 'str'>
```

- 위의 코드를 통해 `input()` 함수로 입력 받은 데이터의 자료형이 모두 문자열임을 알 수 있다.
- 즉, 입력 받은 자료로 연산이 필요한 로직을 구현할시 형변환(캐스팅, Casting)이 팔요하다.

## 자료형변환 (타입 캐스팅, Type Casting)

### 문자열을 숫자로 변환하기

- `int()` : 문자열을 int 자료형으로 변환한다.
- `float()` : 문자열을 float 자료형을 변환한다.

```python
intVal = int("1234")
print(type(intVal), intVal)
# 결과 :
# <class 'int'> 1234
floatVal = float("12.34")
print(type(floatVal), floatVal)
# 결과 :
# <class 'float'> 12.34
```

### `ValueError` 예외

- 변환할 자료가 변환할 자료형과 맞지 않을시 이것을 '변환 할 수 없는 것' 이라 말하고 `ValueError` 오류가 발생한다.
- `ValueError` 가 발생하는 원인 두 가지
  1. 숫자가 아닌 것을 숫자로 변환하려고 할때 ex) `int("일이삼")`
  2. 소수점이 있는 숫자 형식의 문자열을 `int()` 함수로 변환하려고 할때 ex) `int("12.34")`

### 숫자를 문자로 변환하기

- `str()` : 다른 자료형을 문자열로 변환한다.

```python
strVal = str(1234)
print(type(strVal), strVal)
# 결과 :
# <class 'str'> 1234
strVal = str(12.34)
print(type(strVal), strVal)
# 결과 :
# <class 'str'> 12.34
```