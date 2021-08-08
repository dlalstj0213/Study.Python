class Circle:
    def __init__(self, radius):
        self.PI = 3.141592
        self.radius = radius

    def get_circumference(self):
        """원의 둘레 구하기

        Args:
            radius (float): [반지름]

        Returns:
            float: 원의 둘레
        """
        return 2 * self.PI * self.radius

    def get_area(self):
        """원의 넓이 구하기

        Args:
            radius (float): 반지름

        Returns:
            float: 원의 넓이
        """
        return self.PI * self.radius * self.radius

    def to_string(self):
        return f"PI: {self.PI}, radius: {self.radius}, area: {self.get_area()}, circum: {self.get_circumference()}"


c = Circle(10)
print(c.get_area())
print(c.get_circumference())
print(c.to_string())
