
#Insert node at head, tail and at position
#Delete at position
#Traverse


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data,tmp.next)
            tmp = tmp.next
        
    def insertnodehead(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertnodeTail(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        
        tail.next = new_node
    
    def insertnodeMid(self,data,position):
        if position == 1:
            self.insertnodehead(data)
            return
        new_node = Node(data)
        count = 1
        tmp = self.head 
        while count < position-1:
            tmp = tmp.next
            count+=1
        new_node.next = tmp.next
        tmp.next = new_node
    
    def deletenode(self,position):
        if position == 1:
            tmp = self.head
            self.head = self.head.next
            del tmp
        else:
            curr = self.head
            prev = None

            counter = 1
            while counter < position:
                prev = curr
                curr = curr.next
                counter+=1
            
            prev.next = curr.next
            curr.next = None
            del curr

        

llist = LinkedList()
llist.insertnodeTail(2)
llist.insertnodeTail(5)
llist.insertnodeTail(15)
llist.insertnodeMid(17,3)
llist.insertnodeMid(19,1)
llist.deletenode(5)
llist.printlist()


# llist = LinkedList()
# llist.insertnodehead(2)
# llist.insertnodehead(5)
# llist.insertnodehead(15)
# llist.printlist()