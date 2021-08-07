PI = 3.141592


def number_input():
    output = input("숫자 입력> ")
    return float(output)


def get_circumference(radius):
    """원의 둘레 구하기

    Args:
        radius (float): [반지름]

    Returns:
        float: 원의 둘레
    """
    return 2 * PI * radius


def get_circle_area(radius):
    """원의 넓이 구하기

    Args:
        radius (float): 반지름

    Returns:
        float: 원의 넓이
    """
    return PI * radius * radius


# 활용 예
if __name__ == "__main__":
    print("example: get_circumference(10) ?", get_circumference(10))
    print("example: get_circle_area(10) ?", get_circle_area(10))
