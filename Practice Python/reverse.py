def reverse(s):
    rev =""
    for ele in s:
              
        rev = ele+rev
    return rev    
             


print(reverse("string"))
        
