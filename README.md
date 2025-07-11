

Groupcast
============

The `Groupcast` library provides a simple interface for managing and interacting with a group of objects as if they were a single entity. It supports method broadcasting, property access, and basic list-like behavior (indexing, iteration, and length).

Features
--------

*   Broadcast method calls to all objects in the group.
    
*   Aggregate attribute/property access from all objects.
    
*   Behaves like a list: supports `len()`, indexing (`[]`), and iteration.
    
*   Flexible construction: either provide a list of objects directly, or provide input data and a constructor class.

Usage
-----

```python
class Example:
    def __init__(self, x):
        self.x = x
        def double(self):
            return self.x * 2
inputs = [1, 2, 3]
group = Group(inputs=inputs, class_=Example) 
print(group.x)
# should result in [1, 2, 3]

print(group.double())
# should result in [2, 4, 6]

print(obj.x)

print(group[0].x)    #< to only print the value for the first object
```

Constructor
-----------

`Group(inputs=None, class_=None, objects=None)`

You can initialize a `Group` in two ways:

1.  **Using `inputs` and `class_`**:
    
    *   Creates a list of objects by passing each element of `inputs` to the `class_` constructor.
        
2.  **Using `objects` directly**:
    
    *   Pass in a list of pre-created objects.
        

If neither `objects` nor both `inputs` and `class_` are provided, a `TypeError` is raised.

Attribute Access
----------------

When accessing an attribute or method:

*   If it's a **non-callable** (e.g., a property or attribute), a list of values is returned from all objects.
    
*   If it's a **method**, a new function is returned that will call the method on all objects with the provided arguments and return a list of results.
    

Example Use Cases
-----------------

*   Managing multiple similar sensor or device objects.
    
*   Group operations on widgets, models, or entities in simulations/games.
    
*   Synchronous control of multiple instances for testing or broadcasting commands.
    

License
-------

MIT License (see LICENSE file for more information)
