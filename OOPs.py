# class Student:
#     name = "Shahid"
#     def __init__(self,name):
#         print("Hi")
#         self.name= name
        
# s1 = Student("Kausar")
# print(s1.name) 
# print(s1.name)     

#Create Student Class that takes name and marks of three subjects as arguments in constructor. Then 
#creat  a method to print  the average.
class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    def  average(self):
        sum   =0
        for i in self.marks:
            sum +=i
        print("Hi,", self.name, " your average score is ",sum/3)
s1 = Student("Kausar",[23,45,76])
print(s1.average()) 

