# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:45:57 2018

@author: jbk48
"""

def solution(s):

    length_list = []

    for i in range(0,len(s)):
        for j in range(0,i):
            chunk = s[j:i+1]
            if(chunk == chunk[::-1]):
                length_list.append(len(chunk))
    if(len(length_list)==0):
        answer = 0
    else:
        answer = max(length_list)

    return answer