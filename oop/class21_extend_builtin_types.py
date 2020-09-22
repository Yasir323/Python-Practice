class Text(str):    # Inheriting from string class
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):   # Overriding append method
        print("Append called.")
        super().append(object)  # Calling original method for lists


text = Text("Python")
print(text.lower())
print(text.duplicate())

list = TrackableList()
list.append("hi")
