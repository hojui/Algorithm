a = [int(e) for e in input().split()]

def partition(a,l,h):
    temp = a[l]
    left = l+1
    right = h
    while left < right:
        while a[left] < temp:
            left+=1
        while a[right] >= temp:
            right-=1
        if left >= right:
            break
        a[left],a[right] = a[right],a[left]
    a[right],a[l] = a[l],a[right]
    return right

def partition2(a,l,h):
    left = l-1
    temp = a[h]
    for i in range(l,h):
        if a[i] <= temp:
            left+=1
            a[i],a[left] = a[left],a[i]
    a[h],a[left+1] = a[left+1],a[h]
    return left+1
def quickSort(a,l,h):
    if l < h:
        pivot = partition2(a,l,h)
        quickSort(a,l,pivot-1)
        quickSort(a,pivot+1,h)

quickSort(a,0,len(a)-1)
print(a)
