import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    obj_module = obj.__module__

    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return result

class SampleClass:
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 2

    def method1(self):
        pass

    def method2(self):
        pass

sample_object = SampleClass()

sample_info = introspection_info(sample_object)
print(sample_info)
