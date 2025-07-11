import groupcast

class Box:
    def __init__(self, value):
        self.value = value
    def multiply(self, factor):
        return(self.value * factor)

group = groupcast.Group(Box, inputs=[[1], [2], [3]])

group.append(Box, inputs=[4])
print(group.get("value"))  # [1, 2, 3, 4]

removed = group.pop()
print(removed.value)       # 4
print(group.get("value"))  # [1, 2, 3]
