'''
A Python script can find out about the type, class, attributes and methods of an object.
This is referred to as reflection or introspection.
Reflection-enabling functions include type(), isinstance(), callable(), dir() and getattr().
'''
class ClassName(object):
    x = 4

print(getattr(ClassName, "x"))
print(callable(ClassName))
