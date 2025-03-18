class Node:
    def __init__(self,value,next):

        self.value= value
        self.next= next

class LinkedList:
    def __init__(self):
        self.head= None
        self.count=0


    def to_string(self):
        if not self.head:
            return "\033[91m[Empty List]\033[0m"  # Red color for empty list
        
        current = self.head
        result = "\033[92mHEAD\033[0m → "  # Green color for HEAD
        while current:
            result += f"\033[94m[{current.value}]\033[0m"  # Blue color for node values
            if current.next:
                result += " → "
            current = current.next
        result += " → \033[91mNone\033[0m"  # Red color for None (end of list)
        return result
    

    def insert_start(self,data):
        self.count+= 1
        
        if self.head== None:
            self.head = Node(data,None)
            
        
        else:
            new_node= Node(data,self.head)
            self.head= new_node

        return self.head
    


newlinkedlist= LinkedList()
print(newlinkedlist.to_string())
newlinkedlist.insert_start(4)
newlinkedlist.insert_start(3)
newlinkedlist.insert_start(5)
print(newlinkedlist.to_string())
