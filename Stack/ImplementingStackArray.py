class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [-1]*size
        self.top = -1
    
    def push(self,element):
        if self.size - self.top > 1 :
            self.top+=1
            self.arr[self.top] = element
        else:
            print('Stack Overflow')

    def pop(self):
        if self.top >= 0:
            self.top-=1
        else:
            print('Stack Underflow')
    
    def peek(self):
        if self.top >= 0  and self.top < self.size:
            print(self.arr[self.top])
        else:
            print('Stack is Empty')
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


obj = Stack(5)
obj.push(22)
obj.push(43)
obj.push(44)
obj.push(22)
obj.push(43)
obj.push(44)
obj.pop()
obj.pop()
obj.pop()
print(obj.isEmpty())