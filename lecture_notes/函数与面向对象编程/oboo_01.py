class Student:
    school = "JDFZ" #类属性
    count = 0 #类属性
    def __init__(self,name,score):
        self.name = name
        self.score = score
        Student.count = Student.count + 1
    def say_score(self):
        print("我的学校是：",Student.school)
        print(self.name,"的分数是：",self.score)

s1 = Student("sx",80)
