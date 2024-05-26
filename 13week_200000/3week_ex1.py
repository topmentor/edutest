a = 123
b = 15.556

print("a:{0} b:{1}".format(a, b))
print(f"a:{a} b:{b}")
print(f"a:{a:05d} b:{b:2f}")

print("a:%05d b:%.2f" % (a, b))


b = 5

if b < 5:
    print("Small")
elif b > 5:
    print("Big")
else:
    print("5")

b = 15
if b < 5:
    print("Small")
else:
    if b > 5:
        print("Big")
    else:
        print("5")


a = 5
i = 1

while i <= 9:
    print(f"{a} X {i} = {a*i}")
    i += 1


a = 5
for i in range(1, 10):
    print(f"{a} X {i} = {a*i}")
