import groupcast

class Box:
    def __init__(self, value):
        self.value = value
    def multiply(self, factor):
        return(self.value * factor)

group = groupcast.Group(inputs=[1, 2, 3], class_=Box)

group.append(input=4, class_=Box)
print(group.get("value"))  # [1, 2, 3, 4]

removed = group.pop()
print(removed.value)       # 4
print(group.get("value"))  # [1, 2, 3]
