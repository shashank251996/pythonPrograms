# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
if __name__ =='__main__':
    inp = input().split(" ")
    s= inp[0]
    print(s)
    i = int(inp[1])
    out = list(permutations(s,i))
    out = sorted(out)
    for ele in out:
        print(''.join(ele))
