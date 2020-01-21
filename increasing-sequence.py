def almostIncreasingSequence(sequence):

    index=1
    count=0
        
    while index <= (len(sequence)-1):
        
        if index < len(sequence)-1:
            previous=sequence[index-1]
            current=sequence[index]
            next=sequence[index+1]          
            stop_here=index+1  
            
        if index == len(sequence)-1:
            previous=sequence[index-1]
            current=sequence[index]
            next = max(sequence)+200
            stop_here=index
                      
        if previous < current and current < next:
            index+=2
            if index <= len(sequence)-1:
                if next>sequence[index] and current>sequence[index]:
                    return False
        elif previous > current and current > next:
            return False
        elif previous==current==next:
            return False
        elif previous>current and current==next:
            return False
        elif previous==current and current>next:
            return False
        elif previous>current and current<next:
            count+=1
            index+=2
        elif previous==current and current<next:
            count+=1
            index+=2
        elif previous<current and current==next:
            count+=1
            index+=2
        elif previous<current and current>next and previous<next:
            count+=1
            index+=2
        elif previous<current and current>next and previous==next:
            count+=1
            
            if len(sequence)-1 >= index+3:
                if current<sequence[index+2]:
                    index+=3
                else:
                    return False
            elif len(sequence)-1 == index+2:
                if current>= sequence[len(sequence)-1]:
                    return False
                else:
                    return True   
                
        elif previous<current and current>next and previous>next:
            count+=1
            if len(sequence)-1 >= index+3:
                index+=3
            else:
                if current<= sequence[len(sequence)-1]:
                    return False
                else:
                    return True
        
        if count>1:
            return False
        
        if stop_here==len(sequence)-1:
            if count>1:
                return False
            else:
                return True
           
                     
    
    return True
