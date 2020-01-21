def reverse(x) :
        string=str(x)
        
        if x<0:
            new_string="-"+string[-1]
        else:
            new_string=string[-1]

        reverse_num=[new_string] 
        
        length=len(string)
        index=-2
        while index>= -length:
            if string[index]!= '-':
                reverse_num.append(string[index])
                index-=1
            else:
                break
        x = int(''.join(reverse_num))
        
        if abs(x) > 0x7FFFFFFF:
            return 0
        else:
            return x

print(reverse(123))
