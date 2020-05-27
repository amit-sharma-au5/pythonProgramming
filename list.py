class Node:
    def __init__(self,initial = None):
        self.value = initial
        self.next = None

    def isempty(self):
        return(self.value == None)
    
    def append(self,v):
        if self.isempty():
            self.value = v
            return()
        temp = self
        while temp.next != None:
            temp = temp.next
        newNode = Node(v)
        temp.next = newNode
        return()
    def insert(self,v):
        if self.isempty():
            self.value = value
            return()
        newNode = Node(v)
        (self.value,newNode.value) = (newNode.value,self.value)
        (self.next,newNode.next) = (newNode,self.next)
        return()
    def delete(self,v)



   
     

l1= Node()
l1.append(6)
l1.append(7)
l1.insert(2)

print(l1.value)
print(l1.next.value)