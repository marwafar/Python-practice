def romanToInt(s):
        
        roman_int={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        if len(s) == 1:
            sum_int = roman_int[s[0]]
            return sum_int
        
        sum_int=0
        index=0
        
        while index <= len(s)-1:
            
            if s[index] in ["I","X","C"] and index+1 <= len(s)-1:
                if s[index+1] not in ["V", "X", "L", "C", "D", "M"]:
                    sum_int += roman_int[s[index]]
                    index+=1
                else:
                    if s[index]=="I" and s[index+1] in ["V", "X"]:
                        sum_int += (roman_int[s[index+1]] - roman_int[s[index]])
                        index+=2
                    elif s[index]=="X" and s[index+1] in ["L","C"]:
                        sum_int += (roman_int[s[index+1]] - roman_int[s[index]])
                        index+=2
                    elif s[index]=="C" and s[index+1] in ["D","M"]:
                        sum_int += (roman_int[s[index+1]] - roman_int[s[index]])
                        index+=2
                    else:
                        sum_int += roman_int[s[index]]
                        index+=1
            else:
                sum_int += roman_int[s[index]]
                index+=1
            
                
        return sum_int

print (romanToInt("III"))
