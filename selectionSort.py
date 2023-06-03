def smallest_in_arr(arr):
    smallest = arr[0]
    smallest_index = 0
    for j in range(1 , len(arr)):
        if arr[j] < smallest:
            smallest = arr[j]
            smallest_index = j
    
    return smallest_index


def selectionSort(arr , reversed = False):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(smallest_in_arr(arr)))
        
    if reversed:
        new_arr.reverse()
        return new_arr
    
    return new_arr


print(selectionSort([2,1,3,4,5,72,2,2,2,2,6,8,943,434]))