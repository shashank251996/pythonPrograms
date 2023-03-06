def fun(l):
    phone_list = []
    phone_list.append(l)
    
        
    for  i in phone_list:
        
        fist_three_phone_no=i[0:3]
        if len(i)>= 10:
            if fist_three_phone_no[0:3] == "+91":
                print("+91 "+i[-10:])
            elif fist_three_phone_no[0] == "0":
                print("+91 "+i[-10:])

            elif(fist_three_phone_no[0:2] == "91"):
                print("+91 "+i[-10:])
        
        # complete the function
    return fun

   
#phone_list =[919875641230,07895462130]

fun("919875641230")


