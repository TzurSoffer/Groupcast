from concurrent.futures import ThreadPoolExecutor, as_completed

class Group:
    def __init__(self, inputs=None, class_=None, objects=None, parallel=False, maxWorkers=None):
        self.changeExecutionMode(parallel, maxWorkers)

        if objects is not None:
            self.objects = objects
        elif inputs == None or class_ == None:
            raise TypeError("Must set either 'objects' or both 'inputs' and 'class_'")
        else:
            self.objects = [class_(i) for i in inputs]
    
    def changeExecutionMode(self, parallel=False, maxWorkers=None):
        self.parallel = parallel
        self.maxWorkers = maxWorkers
    
    def append(self, input=None, class_=None, object=None):
        if object is not None:
            self.objects.append(object)
        elif input == None or class_ == None:
            raise TypeError("Must set either 'object' or both 'input' and 'class_'")
        else:
            self.objects.append(class_(input))
    
    def pop(self, index=-1):
        return(self.objects.pop(index))

    def apply(self, funcName, *args, **kwargs):
        if not self.objects:
            raise AttributeError(f"No objects in group to apply '{funcName}'")

        def call(obj):
            func = getattr(obj, funcName)
            if not callable(func):
                raise TypeError(f"Attribute '{funcName}' is not callable on object {obj}")
            return func(*args, **kwargs)

        if not self.parallel:
            return [call(obj) for obj in self.objects]
        else:
            with ThreadPoolExecutor(max_workers=self.maxWorkers) as executor:
                futures = [executor.submit(call, obj) for obj in self.objects]
                return [future.result() for future in futures]

    def get(self, attrName):
        if not self.objects:
            raise AttributeError(f"No objects in group to get attribute '{attrName}'")

        attr = getattr(self.objects[0], attrName)
        if callable(attr):
            raise TypeError(f"Attribute '{attrName}' is callable; use apply instead of get")

        return [getattr(obj, attrName) for obj in self.objects]

    def __getattr__(self, name):
        if not self.objects:
            raise AttributeError(f"No objects in group to access '{name}'")

        sampleAttr = getattr(self.objects[0], name)

        if callable(sampleAttr):
            def broadcastedMethod(*args, **kwargs):
                return self.apply(name, *args, **kwargs)
            return broadcastedMethod
        else:
            return self.get(name)

    def __iter__(self):
        return(iter(self.objects))

    def __len__(self):
        return(len(self.objects))

    def __getitem__(self, index):
        return(self.objects[index])
