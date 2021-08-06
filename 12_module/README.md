# 모듈

### 모듈이란

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

## 더 알아보기

### 📌 [표준 모듈](./standard_module.ipynb)
### 📌 [외부 모듈](./external_module.ipynb)
### 📌 [커스텀 모듈](./custom_module.ipynb)