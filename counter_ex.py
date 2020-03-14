def minimumSwaps(arr):
    count = 0
    i = 0
    while i <len(arr)-1:
        if arr[i] != i+1 :
            arr[i], arr[i-1] = arr[i-1], arr[i]
            count+=1
        else:
            i+=1
    return count


