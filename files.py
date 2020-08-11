class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __str__(self):
        return "name"+self.name+"rollno"+str(self.rollno)

s=student("Sanjay",1)
print(s)