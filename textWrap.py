import textwrap

def wrap(string, max_width):
    new_st =""
    l =[]
    print(round(len(string)/max_width))
    for ele in range (round(len(string)/max_width)+1):
        new_st = string[:max_width]
        string =string [max_width:]
        l.append(new_st)
    return l    
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for ele in result:
        print(ele)
