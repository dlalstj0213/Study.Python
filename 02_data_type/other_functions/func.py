val = "{}".format(1234)
print(type(val), val)

val = "{} {} {}".format(100, 200, 300)
print(val)

format1 = "{:d}".format(123)
format2 = "{:5d}".format(123)
format3 = "{:10d}".format(123)
format4 = "{:05d}".format(123)
format5 = "{:05d}".format(-123)
format6 = "{:5d}".format(-123)

print(format1)
print(format2)
print(format3)
print(format4)
print(format5)
print(format6)

format7 = "{:+d}".format(123)
format8 = "{:+d}".format(-123)
format9 = "{: d}".format(123)
format10 = "{: d}".format(-123)

print(format7)
print(format8)
print(format9)
print(format10)

format11 = "{:=+5d}".format(123)
format12 = "{:=+05d}".format(-123)

print(format11)
print(format12)

format13 = "{:=+05d}".format(123)
format14 = "{:+=05d}".format(123)

print(format13)
print(format14)

format1 = "{:f}".format(12.345)
print(format1)

format2 = "{:15f}".format(12.345)
format3 = "{:+15f}".format(12.345)
format4 = "{:+015f}".format(12.345)

print(format2)
print(format3)
print(format4)

format5 = "{:15.3f}".format(12.345)
format6 = "{:15.2f}".format(12.345)
format7 = "{:15.1f}".format(12.345)

print(format5)
print(format6)
print(format7)

format8 = "{:g}".format(12.0)
print(format8)

v_str = "aBcDeFgHiJk"
print(v_str.lower())
print(v_str.upper())

v_str = "aBcDeFgHiJk"
print(v_str.upper())
print(v_str)
v_format = "{} {} {}"
print(v_format.format(12, 34, 56))
print(v_format)

v_str = " abcd "
print(v_str.strip())
print(v_str.lstrip())
print(v_str.rstrip())

v_find = "abcbcde"
print(v_find.find("bc"))
print(v_find.rfind("bc"))

print("bc" in "abcde")

print("bd" in "abcde")

v_split = "a,b,c,d,e"
print(v_split.split(","))