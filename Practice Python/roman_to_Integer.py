def roman_to_integer(num):

    
    romman_array =list(num)
    number =0
    #print(romman_array)
    roman_num ={"I":1,    "V" :5,    "X":10,    "L":50,    "C":100,    "D":500,    "M":1000}
    for i in range (0,len(romman_array)):
        for n in romman_array:
            value =roman_num.get(n)
            i=i+1
            number = number+value
        if "IV" in num or "IX" in num:
            number = number-2  
        if "XL" in num or "XC" in num:
            number = number-20 
        if "CD" in num or "CM" in num:
            number = number-200 
        return number
        


    
roman_to_integer('MCDXCIV')
    
