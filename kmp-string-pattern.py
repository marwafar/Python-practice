def kmp_str(txt,pat):
    if not pat:
        return 
    
    m=len(pat)
    n=len(txt)

    arr=[0 for j in range(m)]
    i=0
    j=1
    while j<m:
        if i==0 and pat[i]!=pat[j]:
            arr[j]=0
            j+=1
        elif pat[i]==pat[j]:
            i+=1
            arr[j]=i
            j+=1
        else:
            i=arr[i-1]
    print(arr)

    i=0
    j=0
    while i<n:
        if txt[i]==pat[j]:
            i+=1
            j+=1
        if j==m:
            print("pattern found at index "+str(i-j))
            j=arr[j-1]
        elif i<n and txt[i]!=pat[j]:
            if j!=0:
                j=arr[j-1]
            else:
                i+=1

txt="abcabcabc"
pat="abaababaab"
kmp_str(txt,pat)