from student import Student

students = [
    Student("홍길동", "James", 25, "A반", 89.5),
    Student("김길동", "John", 30, "A반", 64.3),
    Student("이길동", "Jack", 21, "A반", 71.4),
    Student("최길동", "Ethen", 22, "B반", 98.5),
    Student("박길동", "Soo", 27, "B반", 80.9),
]

for student in students:
    print(dict(student.__dict__))
