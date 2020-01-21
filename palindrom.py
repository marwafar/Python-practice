def is_Palindrome(x):
        string_x=str(x)
        bindex=-1
        for findex in range(len(string_x)):
            if string_x[findex]!=string_x[bindex]:
                return False
            else:
                bindex-=1
        return True

print(is_Palindrome(10))
