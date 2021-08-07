import test_module as test

print("main.py __name__ : ", __name__)

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
