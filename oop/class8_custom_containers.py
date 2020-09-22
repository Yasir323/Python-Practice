# Buiding our own data container

class TagCloud:
    def __init__(self):
        self.tags = {}  # Empty dictionary

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        # To retrieve an item from dictionary
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        # To add an item to dictionary
        self.tags[tag.lower()] = count

    def __len__(self):
        # To get the number of elements in the dictionary
        return len(self.tags)

    def __iter__(self):
        # To iterate  over the list
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("python")

print(cloud.tags)
cloud["JS"] = 10    # setitem allows this

print(cloud["python"])  # getitem allows this
print(cloud["JS"])
print(cloud.tags)
print(len(cloud))

for item in cloud:
    print(item, cloud[item])
