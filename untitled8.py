# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:24:39 2022

@author: vinit
"""

def remove(string):
    st = ""
    for i in range(len(string)):
        if i % 2 ==0:
            st=st+string[i]
    return st

string=input("Enter the String: ")
print("New String is : "+remove(string))