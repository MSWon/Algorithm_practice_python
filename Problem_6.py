# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:30:44 2018

@author: jbk48
"""

def solution(N, t, M):

    M.sort(reverse = True)
    p = [0]

    for i in range(1,N):

        tmp = p[i-1] + (M[i-1]-M[i])*i
        p.append(tmp)
        if(tmp > t):
            break

    answer = (sum(M[0:i]) - t) // i
    return answer