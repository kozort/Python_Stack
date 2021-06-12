arr = [6,5,3,1,8,7,2,4,3,5,7,8,6,5,4,2,9,12,7,9,5,11,0]
print(arr)
def insertSort(arr):
    for index in range(1, len(arr), 1):
        if arr[index] < arr[index-1]:
            for i in range(index, 0, -1):
                arr[i], arr[i-1] = arr[i-1], arr[i]
                if arr[i-1] > arr[i-2]:
                    break
    return arr
print(insertSort(arr))