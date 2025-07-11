class Group:
    def __init__(self, inputs=None, class_=None, objects=None):
        if objects is not None:
            self.objects = objects
        elif inputs == None or class_ == None:
            raise TypeError("Must set either 'objects' or both 'inputs' and 'class_'")
        else:
            self.objects = class_(inputs)

    def __getattr__(self, name):
        attrs = [getattr(obj, name) for obj in self.objects]

        if not callable(attrs[0]):                 #< If the first attribute is not callable, assume it's a property-like access
            return(attrs)
        
        def broadcastedMethod(*args, **kwargs):    #< If attributes are callable, define and return a broadcasting method
            results = [func(*args, **kwargs) for func in attrs]
            return(results)

        return(broadcastedMethod)

    def __iter__(self):
        return(iter(self.objects))

    def __len__(self):
        return(len(self.objects))

    def __getitem__(self, index):
        return(self.objects[index])
