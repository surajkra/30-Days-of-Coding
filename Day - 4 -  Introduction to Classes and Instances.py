'''
Problem Statement:
Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter.
The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0..
In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:
If , print You are young..
If  and , print You are a teenager..
Otherwise, print You are old..
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method.
'''
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if(initialAge<0):
            self.Age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.Age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if(self.Age<13):
            print("You are young.")
        elif(self.Age>=13 and self.Age<18):
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.Age = self.Age + 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
