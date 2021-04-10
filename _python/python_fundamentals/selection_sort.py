arr = [9,6,7,0,8,8,3,2,4,1,5,9,2,5]
print(arr)
def selSort(a):
    n = len(a)
    for i in range(n):
        minLoc = i
        for j in range(i,n):
            if a[minLoc] > a[j]:
                minLoc = j
        a[i], a[minLoc] = a[minLoc], a[i]
    return a
print(selSort(arr))