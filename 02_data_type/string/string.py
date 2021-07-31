from _typeshed import SupportsRead


print("문자열입니다.")
print("문자열입니다.")

print('"문자열"입니다.')
print("'문'자열입니다.")
print('"문자열입니다."')
print("'문자열입니다.'")

print("줄바꿈\n입니다.")
print("탭\t입니다.")
print("역슬래시 \\")

print(
    """\
여러줄1
여러줄2
여러줄3\
"""
)

print("문자" + "연결")
print("안녕" + "하세요" + " !")
print("안녕하세요" + 1)

print("문자열반복" * 3)

print("문자열선택하기")
print("문자열선택"[0])
print("문자열선택"[1])
print("문자열선택"[2])
print("문자열선택"[3])
print("문자열선택"[4])

print("문자열선택"[-1])
print("문자열선택"[-2])
print("문자열선택"[-3])
print("문자열선택"[-4])
print("문자열선택"[-5])

print("-----------")
print("문자열범위"[1:3])
print("문자열범위"[0:2])
print("문자열범위"[1:])
print("문자열범위"[:3])

# print("문자열선택"[10])

print(len("문자열길이"))
