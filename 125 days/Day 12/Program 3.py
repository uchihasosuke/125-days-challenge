#Create a Python class for a basic linked list ADT with methods to insert, delete, and traverse the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

            while temp is not None:
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next

            if temp is None:
                return

            prev.next = temp.next
            temp = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
          
