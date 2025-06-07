from DebugVisualizer import LinkedListVisualizer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at(self, index, data):
        new_node = Node(data)

        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                print("Index out of bounds.")
                return
            temp = temp.next

        if temp is None:
            print("Index out of bounds.")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_at(self, index):
        if self.head is None:
            print("List is empty.")
            return

        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        for _ in range(index - 1):
            if temp.next is None:
                print("Index out of bounds.")
                return
            temp = temp.next

        if temp.next is None:
            print("Index out of bounds.")
            return

        temp.next = temp.next.next


l1 = LinkedList()               # List1

l2 = LinkedList()               # List2

viz = LinkedListVisualizer()    # LinkedListVisualizer instance

l1.insert_at(0, 10)             # List1: 10
viz.visualize(l1.head)          

l2.insert_at(0, 11)             # List2: 11
viz.visualize(l2.head)

l1.insert_at(1, 20)             # List1: 10 -> 20
viz.visualize(l1.head)

l1.insert_at(1, 15)             # List1: 10 -> 15 -> 20
viz.visualize(l1.head)

l2.insert_at(1, 22)             # List2: 10 -> 22
viz.visualize(l2.head)

l1.insert_at(3, 25)             # List1: 10 -> 15 -> 20 -> 25
viz.visualize(l1.head)

l2.insert_at(2, 33)             # List2: 11 -> 22 -> 33
viz.visualize(l2.head)          

l1.delete_at(1)                 # List1: 10 -> 20 -> 25
viz.visualize(l1.head)

l2.delete_at(0)                 # List2: 22 -> 33
viz.visualize(l2.head)
