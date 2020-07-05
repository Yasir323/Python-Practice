# A Program to create a linked list taking input from user

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


def printList():
    temp = nodes[0].head
    while temp:
        print(temp.data,'->', temp.next)
        temp = temp.next

# Code execution starts here
if __name__=='__main__':
    nodes = []
    # Start with the empty list
    ll_data = input("Enter data is sequence followed by spaces: ")
    ls = ll_data.split()
    for i in range(len(ls)):
        if i == 0:
            llist = LinkedList()
            nodes.append(llist)
            nodes[i].head = Node(ls[i])
        node = Node(ls[i])
        nodes.append(node)

    for i in range(len(ls) - 1):
        if i == 0:
            nodes[i].head.next = nodes[i + 1]
        nodes[i].next = nodes[i + 1]

    printList()
