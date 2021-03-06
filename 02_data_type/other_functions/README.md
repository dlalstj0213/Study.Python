## 목차

- [숫자와 문자열의 함수](#숫자와-문자열의-함수)
  - [문자열의 `format()` 함수](#문자열의-format-함수)
    - [`format()` 사용법](#format-사용법)
      - [기본적인 괄호 사용법 알아보기](#기본적인-괄호-사용법-알아보기)
      - [정수를 특정 칸에 출력하기](#정수를-특정-칸에-출력하기)
      - [기호 붙여 출력하기](#기호-붙여-출력하기)
      - [기호 조합하기](#기호-조합하기)
      - [조합 순서 유의하기](#조합-순서-유의하기)
      - [부동 소수점 출력의 다양한 형태](#부동-소수점-출력의-다양한-형태)
      - [소수점 아래 자릿수 지정하기](#소수점-아래-자릿수-지정하기)
      - [의미없는 소수점 제거하기](#의미없는-소수점-제거하기)
    - [발생 가능 예외 `IndexError`](#발생-가능-예외-indexerror)
  - [대소문자 변환 `upper()` `lower()`](#대소문자-변환-upper-lower)
    - [upper() 함수](#upper-함수)
    - [lower() 함수](#lower-함수)
  - [파괴적 함수와 비파괴적 함수](#파괴적-함수와-비파괴적-함수)
  - [문자열 양옆의 공백 제거 `strip()`](#문자열-양옆의-공백-제거-strip)
    - [`strip()` 함수](#strip-함수)
    - [`lstrip()` 함수](#lstrip-함수)
    - [`rstrip()` 함수](#rstrip-함수)
  - [문자열 구성 파악](#문자열-구성-파악)
  - [문자열 찾기 `find()` `rfind()`](#문자열-찾기-find-rfind)
    - [`find()` 함수](#find-함수)
    - [`rfind()` 함수](#rfind-함수)
  - [문자열과 `in` 연산자](#문자열과-in-연산자)
  - [문자열 자르기 `split()`](#문자열-자르기-split)

# 숫자와 문자열의 함수

## 문자열의 `format()` 함수

### `format()` 사용법

#### 기본적인 괄호 사용법 알아보기

- `format()` 함수는 간단하게 문자열로 변환하는 기능이다.
- `format()` 함수는 `{}` 와 매개변수가 매핑되어 매개변수 값이 `{}` 에 대치된다.

```python
val = "{}".format(1234)
print(type(val), val)
# 결과 : 
# <class 'str'> 1234
```

- 다수의 `{}`가 작성될 수 있으며 작성된 개수 만큼 `format()` 함수의 파라미터 개수도 맞춰줘야한다.

```python
val = "{} {} {}".format(100, 200, 300)
# 결과 : 
# 100 200 300
```

#### 정수를 특정 칸에 출력하기

- `{}` 안에 특정 문자를 조합해서 다양한 문자열을 만들 수 있다.
- `:d` 는 int 자료형의 정수만을 받겠다고 직접적으로 지정한것이여서 매개변수로는 정수만 올 수 있다.
> 결과 가독성을 위해서 `print()` 함수는 생략하고 공백은 `^` 기호로 표현했다.

```python
format1 = "{:d}".format(123)
# 결과 : 기본
# 123
format2 = "{:5d}".format(123)
# 결과 : 5칸
# ^^123
format3 = "{:10d}".format(123)
# 결과 : 10칸
# ^^^^^^^123
format4 = "{:05d}".format(123)
# 결과 : 양수
# 00123
format5 = "{:05d}".format(-123)
# 결과 : 음수
# -0123
format6 = "{:5d}".format(-123)
# 결과 : 음수
# ^-123
```

- `:d` 형식은 길이 수에 맞춰 칸을 만들어 주고 뒤에서부터(오른쪽부터) 매개변수로 받은 정수를 채운다.
- 즉, `d` 앞에 작성된 숫자는 문자열의 총 길이를 나타내고 값이 없는 자리에는 공백으로 처리하거나 총 문자열 길이 앞에 `0`을 작성시 공백 대신 0으로 처리한다.
- ~~부호(+/-)는 제일 첫 자리에 대치된다.~~

#### 기호 붙여 출력하기

> 결과 가독성을 위해서 `print()` 함수는 생략하고 공백은 `^` 기호로 표현했다.

```python
format7 = "{:+d}".format(123)
# 결과 : 
# +123
format8 = "{:+d}".format(-123)
# 결과 : 
# -123
format9 = "{: d}".format(123)
# 결과 : 
# ^123
format10 = "{: d}".format(-123)
# 결과 : 
# -123
```

- 위의 코드에서 볼 수 있듯이 `+`를 붙였을 때는 파라미터로 들어온 정수를 알맞은 부호로 붙여준다.
- 반면에 빈공간이 존재하는 `{: d}`와 같은 형식은 기존의 부호를 없애고 공백을 채워준다. 그러나 음수였을때는 변화가 없다.
- **즉**, 쉽게 생각해서 `{:+d}`이 형식와 `{: d}`이러한 형식은 음수와는 상관없이 양수에만 적용되며 **`{:+d}` 이면 양수의 부호를 만들어주고, `{: d}`는 양수의 부호를 없애고 빈공간으로 채운다.**

#### 기호 조합하기

> 결과 가독성을 위해서 `print()` 함수는 생략하고 공백은 `^` 기호로 표현했다.

```python
format11 = "{:=+5d}".format(123)
# 결과 : 
# +^123
format12 = "{:=+05d}".format(-123)
# 결과 : 
# -^123
```

- `=` 기호를 조합하면 부호를 앞으로 밀어준다. 그리고 채워지지않은 칸은 공백이나 0으로 채운다.

#### 조합 순서 유의하기

> 결과 가독성을 위해서 `print()` 함수는 생략하고 공백은 `^` 기호로 표현했다.

- 괄호 안에 기호 조합은 조합 순서에 따라 결과가 다르게 나오니 주의해서 사용한다.

```python
format13 = "{:=+05d}".format(123)
# 결과 : 
# +0123
format14 = "{:+=05d}".format(123)
# 결과 : 
# ++123
```

#### 부동 소수점 출력의 다양한 형태

> 결과 가독성을 위해서 `print()` 함수는 생략하고 공백은 `^` 기호로 표현했다.

- `format()` 함수의 부동 소수점 사용은 `{:f}`를 활용하고 앞에서 설명했던 `{:d}`의 기호 조합 사용 방식이 다르지 않다.
- 다만, 정수가 아니기 때문에 ---

```python
format1 = "{:f}".format(12.345)
# 결과 :
# 12.345000
format2 = "{:15f}".format(12.345)
# 결과 :
# ^^^^^^12.345000
format3 = "{:+15f}".format(12.345)
# 결과 :
# ^^^^^+12.345000
format4 = "{:+015f}".format(12.345)
# 결과 :
# +0000012.345000
```

#### 소수점 아래 자릿수 지정하기

> 결과 가독성을 위해서 `print()` 함수는 생략하고 공백은 `^` 기호로 표현했다.

```python
format5 = "{:15.3f}".format(12.345)
# 결과 :
# ^^^^^^^^^12.345
format6 = "{:15.2f}".format(12.345)
# 결과 :
# ^^^^^^^^^^12.35
format7 = "{:15.1f}".format(12.345)
# 결과 :
# ^^^^^^^^^^^12.3
```

#### 의미없는 소수점 제거하기

```python
format8 = "{:g}".format(12.0)
# 결과 :
# 12
```

### 발생 가능 예외 `IndexError`

- 파라미터의 개수가 맞지 않으면 발생하는 오류

## 대소문자 변환 `upper()` `lower()`

### upper() 함수

- upper() 함수는 문자열의 알파벳을 모두 대문자로 만든다.

```python
v_str = "aBcDeFgHiJk"
print(v_str.upper())
# 결과 : 
# ABCDEFGHIJK
```

### lower() 함수

- lower() 함수는 문자열의 알파벳을 모두 소문자로 만든다.

```python
v_str = "aBcDeFgHiJk"
print(v_str.lower())
# 결과 : 
# abcdefghijk
```

## 파괴적 함수와 비파괴적 함수

- 비파괴적 함수는 원본 데이터가 변경되지 않는 함수를 뜻하고 그 반대는 파괴적 함수라 한다.

```python
v_str = "aBcDeFgHiJk"
print(v_str.upper())
print(v_str)
# 결과 : 
# ABCDEFGHIJK
# aBcDeFgHiJk
```

## 문자열 양옆의 공백 제거 `strip()`

> 결과 가독성을 공백은 `^` 기호로 표현했다.

### `strip()` 함수

- 문자열 양옆의 공백을 제거

```python
v_str = " abcd "
print(v_str.strip())
# 결과 : 
# abcd
```

### `lstrip()` 함수

- 문자열 왼쪽의 공백을 제거

```python
v_str = " abcd "
print(v_str.lstrip())
# 결과 :
# abcd^
```

### `rstrip()` 함수

- 문자열 오른쪽을 공백을 제거
 
```python
v_str = " abcd "
print(v_str.rstrip())
# 결과 : 
# ^abcd
```

## 문자열 구성 파악

- `isalnum()` : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
- `isalpha()` : 문자열이 알파벳으로만 구성되어 있는지 확인
- `isidentifier()` : 문자열이 식별자로 사용할 수 있는 것인지 확인
- `isdecimal()` : 문자열이 정수 형태인지 확인
- `isdigit()` : 문자열이 숫자로 인식될 수 있는 것인지 확인
- `isspace()` : 문자열이 공백으로만 구성되어 있는지 확인
- `islower()` : 문자열이 소문자로만 구성되어 있는지 확인
- `isupper()` : 문자열이 대문자로만 구성되어 있는지 확인

>boolean 자료형인 `True` / `False`를 반환한다.

## 문자열 찾기 `find()` `rfind()`

### `find()` 함수

- 왼쪽부터 찾아서 처음 등장하는 위치를 찾는다.

```python
v_find = "abcbcde"
print(v_find.find("bc"))
# 결과 :
# 1
```

### `rfind()` 함수

- 오른쪽부터 찾아서 처음 등장하는 위치를 찾는다.

```python
v_find = "abcbcde"
print(v_find.rfind("bc"))
# 결과 :
# 3
```

## 문자열과 `in` 연산자

- 문자열 내부에 어떤 문자열이 있는지 확인하기 위한 연산자
- 결과는 boolean 형태로 반환한다.

```python
print("bc" in "abcde")
# 결과 :
# True
print("bd" in "abcde")
# 결과 :
# False
```

## 문자열 자르기 `split()`

- 문자열을 자를때 사용하는 함수
- 결과는 리스트(list) 형태의 배열을 반환한다.

```python
v_split = "a,b,c,d,e"
print(v_split.split(","))
# 결과 :
# ['a', 'b', 'c', 'd', 'e']
```