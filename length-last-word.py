def length_of_last_word(s):
        
        if len(s) == 0:
            return 0
        
        list_s=s.split()
        if len(list_s) >1:
            return len(list_s[-1])
        elif len(list_s) == 1:
            return len(list_s[0])
        else:
            return 0

s = "Hello World"
print(length_of_last_word(s))
