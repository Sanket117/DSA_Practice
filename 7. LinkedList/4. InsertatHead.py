from common import Node,printLL,take_input_better

head = take_input_better()

def insert_at_head(head ,data):
    newNode = Node(data)
    newNode.next = head
    head =newNode
    return head

head = insert_at_head(head,100)
print(printLL(head))


def insert_at_tail(tail,data):
    newNode = Node(data)
    if(head is None):
        return newNode
    temp = head
    while(temp.next != None):
        temp = temp.next
    temp.next = newNode
    
    return head



head = insert_at_tail(head,100)
print("after inserting at tail")
print(printLL(head))