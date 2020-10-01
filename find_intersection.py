def intersection(nums1, nums2):
        
        if not nums1 or not nums2:
            return
        if not nums1 and not nums2:
            return
        
        l1=len(nums1)
        l2=len(nums2)
        output=set()
        
        if l1<=l2:
            nums2=radix_sort(nums2)
            for i in range(l1):                                
                target=binary_search(nums2,nums1[i])
                if target != -1:
                    output.add(target)
                                    
        else:
            nums1=radix_sort(nums1)
            print(nums1)
            for i in range(l2):                
                target=binary_search(nums1,nums2[i])
                if target != -1:
                    output.add(target)
                    
        return list(output)
        
def binary_search(arr,target):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return target
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1
        
def radix_sort(arr):
    max_elem=max(arr)
    max_digit=len(str(max_elem))
    
    for d in range(max_digit):
        index=-(d+1)
        digits=[[] for i in range(10)]
        
        for elem in arr:
            digit_str=str(elem)
            try:
                digit=int(digit_str[index])
            except:
                digit=0
            digits[digit].append(elem)
    
        arr=[]
        for elem in digits:
            arr.extend(elem)
    return arr

nums1=[61,24,20,58,95,53,17,32,45,85,70,\
    20,83,62,35,89,5,95,12,86,58,77,30,64,\
        46,13,5,92,67,40,20,38,31,18,89,85,\
            7,30,67,34,62,35,47,98,3,41,53,\
                26,66,40,54,44,57,46,70,60,4,\
                    63,82,42,65,59,17,98,29,72,\
                        1,96,82,66,98,6,92,31,43,\
                            81,88,60,10,55,66,82,0,79,11,81]
nums2=[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,\
    15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]

print(intersection(nums1, nums2))