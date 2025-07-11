import groupcast

class Box:
    def __init__(self, value):
        self.value = value
    def multiply(self, factor):
        return(self.value * factor)

group = groupcast.Group(inputs=[1, 2, 3], class_=Box)

# Using apply() directly
print(group.apply("multiply", 10))  # [10, 20, 30]

# Using get() directly
print(group.get("value"))  # [1, 2, 3]
