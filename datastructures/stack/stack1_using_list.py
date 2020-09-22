my_stack = [1, 2, 3, 4, 5]

def push(stack, element):
    stack.append(element)

def pop(stack):
    stack.pop()

def empty(stack):
    if stack:
        return False
    else:
        return True

def size(stack):
    return len(stack)

def top(stack):
    return stack[-1]

push(my_stack, 6)
print(my_stack)
pop(my_stack)
print(my_stack)
print(size(my_stack))
print(top(my_stack))
print(empty(my_stack))
