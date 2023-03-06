def wrapper(f):
    def num(x,y):
        p= int(f(x,y))
        print("sum of numbers  are :"+str(f(x,y)))
        square =  p*p
        print("square of num :" +str(square))
    return num




@wrapper
def sum(x,y):
    return x+y

if __name__=='__main__':
    x = int(input())
    y = int(input())
    sum(x,y)
    
    
    
