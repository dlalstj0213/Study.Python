class Student:
    def __init__(self, kor_name, eng_name, age, clazz, grade) -> None:
        self.kor_name = kor_name
        self.eng_name = eng_name
        self.age = age
        self.clazz = clazz
        self.grade = grade

    def __del__(self):
        print("Student 인스턴스가 소멸 되었습니다.")