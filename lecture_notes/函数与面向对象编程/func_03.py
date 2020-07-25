def test01():
    print("sxsx")
test01()
c = test01
c()

print(id(test01))
print(id(c))
print(type(c))