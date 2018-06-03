# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 23:22:15 2018

@author: jbk48
"""

def solution(values):

    n = len(values)

    f = [0]

    if(n == 1):
        return values[0]

    elif(n == 2):
        return values[0] + values[1]

    else:

        f.append(values[0])
        f.append(values[0] + values[1])

        comp1 = f[0] + values[1] + values[2]
        comp2 = f[1] + values[2]

        for i in range(3,n+1):

            comp1 = f[i-3] + values[i-2] + values[i-1]
            comp2 = f[i-2] + values[i-1]

            if(comp1 > comp2):
                f.append(comp1)
            else:
                f.append(comp2)

        return f[n]
