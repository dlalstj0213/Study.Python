class Student:
    # 클래스 변수 선언
    count = 0
    students = []

    # 클래스 함수 정의
    @classmethod
    def print(cls):
        print("====== 학생목록 ======")
        print("이름\t총점\t평균\t")
        for student in cls.students:
            print(str(student))
        print("====== ======== ======")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self) -> str:
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())


#########################################################################################

Student("김길동", 80, 81, 82, 83)
Student("이길동", 85, 86, 87, 88)
Student("박길동", 75, 76, 77, 78)
Student("최길동", 90, 91, 92, 93)
Student("방길동", 95, 96, 97, 98)
Student("정길동", 70, 71, 72, 73)

Student.print()
