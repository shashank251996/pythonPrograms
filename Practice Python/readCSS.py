import re

def swap_case(s):
    stri = s
    print(stri)
    new_op =[]
    new_string=""
    for char in stri:
        if re.search("[A-Z]",char):
            new_string +=(char.lower())
        elif re.search("[a-z]",char):
            new_string +=(char.upper())
        else:
            new_string +=(char)
   # res = "".join([str(item) for item in new_op])
    return new_string 
     

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
