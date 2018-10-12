'''
定义一个学生类,用来形容学生
'''
#定义一个空的类：
class Student():
    #一个空类，pass跳过，不能省略
    pass
mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    couser = "Python"

    def doHomework(self):
        print("我在做作业")
        

        return None
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()



class Person():
    name = "liuying"
    __age= 18