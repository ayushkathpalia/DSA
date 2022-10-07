class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        tmp = self.head
        while tmp:
            str = '{}-{}-{}-->'
            print(str.format(self.prev,self.data,self.next))
            tmp = tmp.next


            
llist = DoubleLinkedList()