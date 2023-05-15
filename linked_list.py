#Singly linked Lists
class SLLNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None 
    
    def __repr__(self):
        return "SLLNode Object: data={}".format(self.data)
        
    def get_data(self):
        return self.data 
    
    def set_data(self, new_data):
        self.data = new_data
        
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
        
    
        
# node1 = SLLNode('apple')
# node2 = SLLNode(2)
# node1.set_next(node2)
# print(node1.get_next())


#Doubly Linked Lists
# class DLLNode:
    
#     def __init__(self, data):
#         self.data = data
#         self.next = None 
#         self.previous = None
    
#     def __repr__(self):
#         return "SLLNode Object: data={}".format(self.data)
        
#     def get_data(self):
#         return self.data 
    
#     def set_data(self, new_data):
#         self.data = new_data
        
#     def get_next(self):
#         return self.next
    
#     def set_next(self, new_next):
#         self.next = new_next
        
#     def get_previous(self):
#         return self.previous
    
#     def set_previous(self, new_previous):
#         self.previous = new_previous
        

# node1 = DLLNode(1)
# node2 = DLLNode(2)

# node2.set_previous(node1)
# print(node2.get_previous())


class SLL:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        return "SLL object: head={}".format(self.head)
    
    def is_empty(self):
        return self.head == None
    
    
    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        size = 0
        if self.head == None:
            return size
        
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
            
        return size
    
    def search(self, data):
        if self.head is None:
            return "Empty Linked List"
        current = self.head
        while current is not None:
            # The Node's data matches what we are looking for
            if current.get_data() == data:
                return True
            # The Node's data does not match
            else:
                current = current.get_next()
                
        return False 
    
    def remove(self, data):
        if self.head is None:
            return "Empty Linked List"
        current = self.head
        previous = None
        found = False 
        
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_data() == None:
                    return "Data not found"
                else:
                    previous = current 
                    current = current.get_next()
        
        if previous is None:
            self.head = current.get(next)
        else:
            previous.set_next(current.get_next())
            
            
    
# sll = SLL()
# print(sll.is_empty())
# node = SLLNode(5)
# sll.head = node
# print(sll.is_empty())
    
# sll = SLL()
# sll.add_front('berry')
# print(sll.head)
    
# sll = SLL()
# print(sll.size())   
# sll.add_front(1)
# sll.add_front(2)
# sll.add_front(3)
# print(sll.size())

# sll = SLL()
# sll.add_front(1)
# sll.add_front(2)
# sll.add_front(3)
# print(sll.search(2))

sll = SLL()
print(sll.remove(15))
sll.add_front(27)
sll.remove(15)
