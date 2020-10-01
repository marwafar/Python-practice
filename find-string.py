def findStrings(w, queries):
    #
    # Write your code here.
    #
    s=[]
    for char in w:
        l=len(char)
        a=set()
        for i in range(l):
            head=i
            tail=l
            while tail>0:
                c=char[i:tail]
                if c not in '':
                    a.add(char[i:tail])
                tail-=1

        s.append(a)
    
    union_set=set()
    for i in range(len(s)):
        union_set.update(s[i])
    
    sorted_set=sorted(union_set)
    #print(s)
    #print(union_set)
    print(sorted_set)

    q=[]
    for k in queries:
        #print(len(sorted_set))
        if k>=len(sorted_set)+1:
            q.append('INVALID')
        
        if k<=len(sorted_set):
            q.append(sorted_set[k-1])

    return q
                
#w=['abkqknbyvueeyvoivdscyhnr','xtluycgumnhkqrmrudownzgyixdhisfeafumj',\
#    'dchwkpdvnukiazdyegexqrjyfsazcsinpefuowvc','ahfujsyzfbvjrodipreaexlpavzenhaxwbkbwivb'\
#        'gwcramroeazzeeavaawpkmwunllqofjbeobblijq','esulzirsfjeomgqjxxuogqpklvjwlqzortcpnsxy'\
#            'tejhdvkakphhstdagqnlvlqolbvefjlnppqvxaag','mcfyjzpymyoufdayjmxljpeboxt'\
#                'fozgxbasodqgavgxanpmbbtvwfqfpretwnltvsnp','oxzkcxpmjndwjlhngmjyjjlqusbifrahkurobpn']
w=['apple']
queries=[1,3,5]

result=findStrings(w, queries)

print(result)