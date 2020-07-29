class Student:
    school = "JDFZ"

    @classmethod
    def printSchool(cls):
        print(cls.school)

Student.printSchool()