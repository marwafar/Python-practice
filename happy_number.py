def is_happy(n):

    loop=0
    while (n!=1 and loop<1000):
        length=len(str(n))
        tot_sum=0
        for i in range(length):
            tot_sum+=(int(str(n)[i]))**2
        n=tot_sum
        if n==1:
            break
        loop+=1
    
    if n==1:
        return 'true'
    else:
        return 'false'

print(is_happy(55))


  
