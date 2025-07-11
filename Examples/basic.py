import groupcast

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, I'm {self.name}")

group = groupcast.Group(inputs=["Alice", "Bob", "Charlie"], class_=Person)

# Broadcast method call
group.greet()      #< Broadcast method calling

print(group.name)  #< Broadcast attribute access