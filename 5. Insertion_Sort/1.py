def insertion_sort(arr):
    n = len(arr)
    
    for current in range(1,n):
        currentCard = arr[current]
        correctPosition =current -1
        
        while correctPosition >=0:
            if arr[correctPosition]<currentCard:
                break
            else:
                arr[correctPosition +1] = arr[correctPosition]
                correctPosition-=1
            arr[correctPosition +1] = currentCard
            
    return arr 


my_list = [11,25,12,34,90,22]
print(my_list)
print("sorted Element",insertion_sort(my_list))