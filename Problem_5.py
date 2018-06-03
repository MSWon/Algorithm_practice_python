# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 23:24:41 2018

@author: jbk48
"""

def solution(param):

    n = len(param)
    D = [[0 for x in range(n+1)] for y in range(n+1)]
    K = [[0 for x in range(n+1)] for y in range(n+1)]
    S = [0 for x in range(n+1)]

    for i in range(1,n+1):
        D[i-1][i] = 0
        K[i-1][i] = i
    for i in range(1,n+1):
        S[i] = S[i-1] + param[i-1]


    for d in range(2,n+1):
        for i in range(0,n-d+1):
            j = i + d
            D[i][j] = 10000000000
            for k in range(K[i][j-1],K[i+1][j]+1):
                v = D[i][k] + D[k][j] + S[j] - S[i]
                if(D[i][j] > v):
                    D[i][j] = v
                    K[i][j] = k

    return D[0][n]

 
