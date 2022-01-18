# Create a class Student with attributes name and roll no 
# and a method dataprint() for displaying the same. Create two instances of the class and call the method for each instance 
class student:
  def __init__(self,name,roll):
    self.name=name
    self.roll=roll

  def printdata(self):
    print("name:",self.name)
    print("roll no:",self.roll)

s1=student("ethan",5)
s2=student("jack",6)

s1.printdata()
s2.printdata()