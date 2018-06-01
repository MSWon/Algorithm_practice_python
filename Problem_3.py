# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:51:29 2018

@author: jbk48
"""

def solution(param1):
    
    param1.sort(reverse = True)
    answer = 0
    for i in range(0,len(param1)):
        sqrt = param1[i]**(0.5)
        ## 제곱근이 정수일때
        if(sqrt.is_integer()):
            j = -1
            while(param1[j] <= sqrt):
                if(param1[j] == sqrt):
                    answer = answer + 1
                j = j - 1


    return answer