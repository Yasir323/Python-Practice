# Program will reverse the string
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    '''
    Python uses the __iter__() method to return an iterator
    object of the class.
    '''

    def __iter__(self):
        return self

    '''
    The iterator object then uses the __next__() method to
    get the next item.
    '''

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def Main():
    rev = Reverse('Monkey D. Luffy')
    for char in rev:
        print(char)


if __name__ == '__main__':
    Main()
