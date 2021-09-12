from dataclasses import dataclass
from enum import Enum, auto


class BasicClass:
    def __init__(self, a: str, b: int) -> None:
        """기본클래스 __init__메소드 설명

        Args:
            a (str): a값, 문자열
            b (int): b값, 숫자
        """
        self.a = a
        self.b = b


class Color(Enum):
    """
    색상 열거형 클래스
    Args:
        Enum ([type]): 열거
    """

    BLACK = auto()
    BLUE = auto()
    WHITE = auto()


@dataclass
class Test:
    """TEST 클래스 설명"""

    name: str
    age: int
    color: Color

    def move(self):
        """move() 메소드 설명"""
        print(self.__annotations__)
        print(self.color == Color.BLACK)
        print("MOVING")


def main(obj: Test):
    """main() 메소드 설명

    Args:
        obj (Test): Test 클래스 객체
    """

    print(main.__annotations__)
    print(f"{obj.name}  {obj.age}")
    obj.move()
    pass


if __name__ == "__main__":
    main(Test("Minseo", 28, Color.BLACK))
    BasicClass("1", 2)
