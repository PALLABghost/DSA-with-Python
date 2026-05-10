class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Empty")
            return None
        data = self.front
        self.front= self.front.next
        if self.front is None:
            self.rear = None
        return data

    def traverse(self):
        temp = self.front
        result = []
        while temp is not None:
            result.append(str(temp.data))
            temp = temp.next
        return "->".join(result)

    def is_empty(self):
        return self.front is None

    def size(self):
        temp = self.front
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def front_item(self):
        if self.front is None:
            print("Empty")
            return
        else:
            print(self.front.data)

    def rear_item(self):
        if self.front is None:
            print("Empty")
            return
        else:
            print(self.rear.data)

q = Queue()
q.enqueue(4)
q.enqueue(5)
print(q.traverse())
q.dequeue()
print(q.traverse())
print(q.is_empty())
q.rear_item()