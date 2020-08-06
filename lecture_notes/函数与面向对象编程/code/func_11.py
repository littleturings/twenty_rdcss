def f1(a,b,*c):
    print(a,b,c)

f1(8,9,19,23)

def f2(a,b,**c):
    print(a,b,c)

f2(8,9,name = "sx",age = 18)

def f3(a,b,*c,**d):
    print(a,b,c,d)

f3(8,91233,23123,132,name = "sx",age=18)
