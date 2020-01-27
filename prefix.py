def longestCommonPrefix(strs):
        
        prefix=""
        
        if len(strs) == 0:
            return prefix
        
        min_string = min(len(string) for string in strs)                
        index=0
        
        for char in strs[0][:min_string]:
            count=0
            for word in strs:
                if word[index]==char:
                    count+=1
                    
            if count != len(strs) and index==0:
                return prefix            
            elif count == len(strs) and index>=0:
                prefix+=char
                index+=1
            else:
                return prefix
        
        return prefix

My_list=["flower","flow","flight"]
print(longestCommonPrefix(My_list))

