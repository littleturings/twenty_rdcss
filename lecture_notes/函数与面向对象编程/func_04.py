a = 3
def test01():
    b = 4
    print(b * 10)
    global a
    print(a)
    a = 400
    print(a)
test01()

#print(a)
#print(b)