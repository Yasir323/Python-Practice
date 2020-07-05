# A Python program to demonstrate working of Generators
'''
Generates the background code for the next() and iter() methods.
Uses a special statement called yield which saves the state of
the generator and set a resume point for when next() is called again.
'''


def Reverse(data):
    # this is like counting from 100 to 1 by taking one(-1)
    # step backward.
    for index in range(len(data)-1, -1, -1):
        yield data[index]


def Main():
    rev = Reverse('Portgas D. Ace')
    for char in rev:
        print(char)


if __name__ == "__main__":
    Main()
