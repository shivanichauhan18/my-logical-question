def swap_case(s):
    i=0
    b=""
    while i<len(s):
        if s[i] in s[i].lower() :
            y=s[i].upper()
            b=b+y
        else:
            y=s[i].lower()
            b=b+y
        i=i+1
    return b
string=raw_input("enter string ")
print (swap_case(string))