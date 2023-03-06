#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    s= sorted(s)
    p=Counter(s).most_common(3)
    for i in range(0,3):
        print(p[i][0],p[i][1])
              
    
    

    
        
