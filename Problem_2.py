# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:50:55 2018

@author: jbk48
"""

def solution(s):
    answer = True
    p_dict = {"(" : 1 , ")" : -1}
    s_index = [p_dict[i] for i in s]

    i = 0
    while(i < len(s)):

        if(s[i] == ")"):
            answer = False
            break
        else:
            j = i
            while(1):
                if(sum(s_index[i:j+1]) == 0):
                    break
                elif(j >= len(s)):
                    answer = False
                    break
                j = j + 1
            i = j
            i = i + 1

    return answer