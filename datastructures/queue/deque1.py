from collections import deque

q = deque(maxlen=3)
print("Empty queue: ", q)
# append method always appends from the right
q.append(1)
q.append(2)
q.append(3)
print("Queue is full now: ", q)

q.append(4)
print("1 is thrown out to make space for 4: ", q)

q.append(5)
print("2 is thrown out to make space for 5: ", q)

"""
Although you could manually perform such operations
on a list (e.g., appending, deleting, etc.), the
queue solution is far more elegant and runs a lot
faster.

A deque can be used whenever you need a simple
queue structure. If you don’t give it a maximum size,
you get an unbounded queue that lets you append
and pop items on either end.
A deque is also Heterogenous.
"""
print("-"*20, "Unbounded dequeue", "-"*20)
q1 = deque()
q1.appendleft([1, 2, 3])
print("Unbounded dequeue: ", q1)

q1.appendleft(4)
q1.appendleft([1, 2, 3])
q1.appendleft((5, 6))
print("Adding elements from the left side: ", q1)

print("Popping elements from right: ", q1.pop())

print("Popping elements from left: ", q1.popleft())

print("What's left in the queue: ", q1)
