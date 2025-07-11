import groupcast

class Person:
    def __init__(self, name, isMale=True):
        self.name = name
        self.isMale = isMale

    def greet(self):
        connection = ""
        if self.isMale == False:
            connection = "not "
        print(f"Hello, I'm {self.name} and I am {connection}a male")

group = groupcast.Group(Person, inputs=[["Alice"], ["Bob"], ["Charlie"]], inputsKw=[{"isMale": False}, {"isMale": True}, {"isMale": False}])

# Broadcast method call
group.greet()      #< Broadcast method calling

print(group.name)  #< Broadcast attribute access