def power_sum(x,n):

    l='123456789'
    data_set=set()
    data_set.add('1')
    start=1
    while start<=len(l):
        for i in range(len(l)):
            for j in range(i,len(l)):
                if l[j] not in l[i:start]:
                    data_set.add(l[i:start]+l[j])
        start+=1

    print(sorted(data_set),len(data_set))
    count=0
    for num in data_set:
        num_length=len(num)
        sum=0
        for i in range(num_length):
            sum+=int(num[i])**2
        if sum==x:
            count+=1

    return count

#---------
x=100
n=2
print(power_sum(100,2))
