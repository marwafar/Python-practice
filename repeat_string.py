def repeat_str(A,B):
    m=len(B)
    arr=[0 for j in range(m)]
    i=0
    j=1
    while j<m:
        if B[i]==B[j]:
            i+=1
            arr[j]=i
            j+=1
        elif B[i]!=B[j] and i==0:
            arr[j]=0
            j+=1
        else:
            i=arr[i-1]
    
    repeat=1
    init=len(A)
    while len(A)<=10000:
        n=len(A)
        m=len(B)
        i=0
        j=0
        while i<n:
            if A[i]==B[j]:
                i+=1
                j+=1
            if j==m:
                print(A)
                return repeat
            else:
                if i<n and A[i]!=B[j]:
                    if j!=0:
                        j=arr[j-1]
                    else:
                        i+=1
        repeat+=1
        A=A[:init]*repeat
        
    return -1

A="abcd"
B="cdabcdab"
print(repeat_str(A,B))
