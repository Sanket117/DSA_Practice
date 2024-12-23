from common import Node,printLL, take_input_better

def lengthOfLL(head):
    temp = head
    ans =0
    while(temp != None):
        temp =temp.next
        ans = ans + 1
    return ans
        
newnode = take_input_better()

#find length using recursion 
def findlenOfLLusingRecursion(head):
    
    if(head == None):  #base case
        return 0
    
    
    recursionAns = findlenOfLLusingRecursion(head.next)
    return 1+ recursionAns
        
length = findlenOfLLusingRecursion(newnode)
print(lengthOfLL(newnode))