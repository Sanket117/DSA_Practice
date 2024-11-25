def sorted_element(arr):
    n =len(arr)
    
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
        

unsorted_arr = [12,34,42,1,44,3]
print("Unsorted element: ",unsorted_arr)
print("------------------------------------------")
print("Sorted Element : ",sorted_element(unsorted_arr))