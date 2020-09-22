from queue import Queue

my_stack = Queue(maxsize=4)

def push(stack, element):
    stack.put(element)

def pop(stack):
    stack.get()

for x in range(4):
    push(my_stack, x)
my_stack.get()
while not my_stack.empty():
    print(my_stack.get(), end=" ")
print()
print(my_stack.qsize())
print(my_stack.empty())
while not my_stack.empty():
    print(my_stack.get(), end=" ")
