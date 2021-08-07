# 모듈

## 모듈이란

파이썬에서 모듈이란 하나의 기능 덩어리로, 여러 변수와 함수를 가지고 있는 집합체이다.  
일반적으로 파이썬에 기본 내장되어 있는 모듈들을 `표준 모듈`이라 부르고  
다른 사람들이 만들어 놓은 모듈을 `외부 모듈`이라고 부른다.

모듈을 가져오기 위한 구문은 다음과 같다.

```python
# 모듈 저체를 가져올때
import 모듈 이름

# 모듈 중에서 활용하고 싶은 모듈만 가져올때
from 모듈 이름 import 가져오고 싶은 변수 또는 함수

# 모듈이름 중복 방지를 위한 식별자 설정
import 모듈 as 사용하고 싶은 식별자

# 패키지내 모든 모듈 가져오기
from /패키지경로 import *
```

사용 예시는 다음과 같다. `ex) math 표준 모듈`

- `import 모듈 이름`
```python
import math

math.sin(1)
math.cos(1)
...
```

- `from 모듈 이름 import 가져오고 싶은 변수 또는 함수`
```python
from math import sin, cos

sin(1)
cos(1)
...
```

- `import 모듈 as 사용하고 싶은 식별자`
```python
from math as m
from math as m2 # 실제로 같은 모듈을 가지고 오진 않음, 예시일 뿐임

m.sin(1)
m2.sin(1)
...
```

## pip 란

pip는 파이썬(python)으로 작성된 패키지 소프트웨어를 설치 · 관리하는 패키지 관리 시스템이다.  
즉, 패키지 라이브러리 관리 시스템이다.  
[Python Package Index (PyPI)](https://pypi.org/)에서 많은 파이썬 패키지를 볼 수 있다.

## pip 커맨드

### 패키지 설치
```bash
$ pip install [패키지이름]
```

### 패키지 제거
```bash
$ pip uninstall [패키지이름]
```

### 패키지 버전 업그레이드
```bash
$ pip install --upgrade --user [패키지이름]
```

### 설치한 패키지 목록
```bash
$ pip list [패키지이름]
```

## 더 알아보기

### 📌 [표준 모듈](./standard_module.ipynb)
### 📌 [외부 모듈](./external_module.ipynb)
### 📌 [커스텀 모듈](./custom_module.ipynb)