# program to create a class/structure node to represent a node in a single linked list
# each node should have two attributes : data and next
#program to creat a class/structure queue to represent the queue itself
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            return data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.data