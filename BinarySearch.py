def binary_search(arr , value):
    low = 0             # setting the low pointer index to 0
    high = len(arr) - 1   # Setting the high pointer index to the max value
    arr.sort()             # You have to sort your list to make the binary search magic happends =)
    while low <= high:      # Trying to find the value until the pointers reach each other
        mid = (low+high) // 2 
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
                high = mid - 1
        else:
            low = mid + 1
    
    return None

given_list = list(map(int , input("Enter the list you want to find your specefic value.\n").split()))

val = int(input("Enter the number you want to find.\n"))

print(binary_search(given_list , val))
