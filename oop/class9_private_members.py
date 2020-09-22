# Buiding our own data container

class TagCloud:
    def __init__(self):
        self.__tags = {}  # Private member

    def add(self, tag):
        # To add an item to our container
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        # To retrieve an item from our container
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        # To add an item to our container
        self.__tags[tag.lower()] = count

    def __len__(self):
        # To get the number of elements in the container
        return len(self.__tags)

    def __iter__(self):
        # To iterate  over the container
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("python")

cloud["JS"] = 10    # setitem allows this

print(cloud["python"])  # getitem allows this
print(cloud["JS"])
# print(cloud.tags)
# By implementing data hiding we have made tags attribute
# inaccesssible (or harder to access) outside the class
# ------------------------------------------------------
# Let's try to access it:
print(cloud.__dict__)
print(cloud._TagCloud__tags)
