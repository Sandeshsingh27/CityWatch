# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:47:30 2022

@author: vinit


31/03/2022  



Tuples

S=()

len() ---> length

Indexing & Sclicing

+,* -----> concainaiate

Comparing Two Tuples

T1=(1,2,3)
T2= (4)
T1+T2 ----->Not possible as T2 is not tuples

T2 = (4,) ------> this is a tuples 

T1+T2 ---------->works fine



MODIFING TWO Tuples
-------------------------------------------------------------------------------



Function
--------

tuple()--------> COnvert into tuple

Index() ---------> return index element
count() ------------> coutn how many times elelmetn occurs 
del() --------

*zip----> packs elemenrrrrrrrrrrrrrrrrrrrrrt 




A1=1,2,3
A2=4,5,6,7,8
print(list(zip(A1,A2)))

SETS 


X=[("A",1),("B",2)]
x,y=zip(*X)
print(x)
print(y)

Set1=set()
print(type(Set1))


Sett={1,2,3,4,5}
print(3 in Sett)
print(type(Sett))


add()---------> add
clear()
S1={1,2,3,4}
S2={1,2,3,4,5}

print(S1.issubset(S2))
print(S1.issuperset(S2))

print(S2.issuperset(S1))


----------------------------------------------------------------------------------------------
OOPS

<><><>><><><><><><><><><><>><><><><><><>><><><><><><><><><><><<><><><><><><><><><><><><><><><>
class Person:
    f_name="VINI"
    l_name="HIHI"
    age=21
eliz=Person()
    
print(eliz.f_name)
print(eliz.l_name)
print(eliz)

print("%s %s is %d" % (eliz.f_name,eliz.l_name,eliz.age))


"""


class ABC:
    x=2 #instance 
    def display(self):
        x=100 #local variable
        print(x)
        print(self.x)
        
a=ABC()
a.display()


























