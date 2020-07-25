a = 100

def outer():
    b = 100
    def inner():
        nonlocal b
        print("inner b:",b)
        b=20

        global a
        a = 1000

    inner()
    print("outer b:",b)

outer()
print("a:",a)
