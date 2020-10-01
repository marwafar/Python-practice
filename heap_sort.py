def heap_sort(arr):
    size=len(arr)

    for i in range(size//2-1,-1,-1):
        max_heapify(arr,size,i)
    
    for k in range(size-1,0,-1):
        arr[0],arr[k]=arr[k],arr[0]
        max_heapify(arr,k,0)
    

def max_heapify(arr,size,i):
    parent=i
    left=2*i+1
    right=2*i+2

    if left<size and arr[parent]<arr[left]:
        parent=left
    if right<size and arr[parent]<arr[right]:
        parent=right
    
    if parent!=i:
        arr[parent],arr[i]=arr[i],arr[parent]
        max_heapify(arr,size,parent)

nums2=[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,\
    15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]

heap_sort(nums2)
print(nums2)