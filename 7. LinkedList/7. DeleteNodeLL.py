from common import Node,take_input_better,printLL

head = take_input_better()


def delete_at_head():
    if(head == None):
        return None
    
    newHead = head.next
    return newHead

printLL(head)

head = delete_at_head(head)
print("After Deletion")
printLL(head)


def is_tail_node(node):
    if(node == None):
        return True
    if(node.next ==None):
        return True
    return False

def delete_at_tail(head):
    if(head is None or head.next is None):
        return None# if the list is empty or has one Node 
    
    temp = head
    
    while(temp.next.next is not None):
        temp =temp.next
        
    print("Data of node we have stopped", temp.data)
    temp.next = None
    return head

head = delete_at_head(head)
print("After deletion")
printLL