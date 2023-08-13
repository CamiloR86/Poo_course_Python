class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def study(self):
        print("studying...") 


name = input("Whats your name?: ")
age = input("How old are you?: ")
grade = input("Which grade do you belong to?: ")

student1 = Student(name, age, grade)

print(f"""
        INFORMATION STUDENT: \n
        Name: {student1.name}
        Age: {student1.age}Ca
        Grade: {student1.grade}

""")

while True: #Loop, user put the correct word.  
    study = input("What do you do? ") #Method is equal to one input.
    if (study.lower() == "study"):
        student1.study() #Execute the method
