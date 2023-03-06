
def elO ():
    
    lis = [1,2,2,2,3,3,4,44,4,5,5,5]
    set1 = set(lis)
    lis2=list(set1)
    for ele in lis2:
        count =0
        for el in lis:
            if(el == ele):
                count = count+1
        
        print('{} element present {} times in list'.format(ele,count))


elO()
