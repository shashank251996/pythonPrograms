#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = s.split(" ")
    full_name=""
    for n in range (0,len(name)):
        if name[n].isalpha():
            name[n]= name[n].replace(name[n],name[n].capitalize())
        
    full_name =' '.join(name)
    return full_name
    


if __name__ == '__main__':
    

    s = input()
    print(solve(s))

    
