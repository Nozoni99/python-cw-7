class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."


    def is_adult(self):
        if first_person.age > 18 :
            print("You have to much responsibilties")
        elif  first_person.age < 18 :
            print("You are lucky !")
        else:
            print("Just try anything else")


first_person = Person("Noor", 17 )
print(first_person.name)
print(first_person.age)
first_person.is_adult()
print(first_person)
   

###########################################################################




class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old"


first_person = Person("Jack", 22 )
print(first_person.name)
print(first_person.age)
print(first_person)