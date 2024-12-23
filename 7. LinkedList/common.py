class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
def printLL(head):
    temp = head
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next
    print()
    return
    
def take_input_better():
    value = int(input("Enter the no. of Node : "))
    head = None
    tail  =None
    
    while(value !=-1):
        NewNode = Node(value)
        if(head == None):
            head =NewNode
            tail = NewNode
        else:
            tail.next = NewNode
            tail = NewNode
            
        value = int(input("Enter the no. of Node : "))
            
    return head
newnode = take_input_better()
print(printLL(newnode))