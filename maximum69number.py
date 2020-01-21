def maximum_69_number (num):
        """
        :type num: int
        :rtype: int
        """
        
        string = str(num)
        new_list=[]
        length=len(string)
        count=0
        for index in range(length):
            if string[index]=='6' and count < 1:
                count+=1
                new_list.append('9')
            else:
                new_list.append(string[index])
                
        return int(''.join(new_list))

print(maximum_69_number(9669))
