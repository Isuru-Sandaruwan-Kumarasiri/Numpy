# Data types in Numpy Library
'''
   Integer : i
   Boolean : b
   Flot    : f
   complex : c
   Unicode : U
   string

   Time    : m
   delta

   Date    : M
   Time

   Object  : O


'''

import numpy as np

x=np.array([1,2,3,4,5])
print(x)
print(x.dtype)

x=np.array(['isuru','kumara','nimal'])
print(x)
print(x.dtype)

# Change the type

# y=np.array([1,2,3,4,5],dtype='f')
y=np.array([1,2,3,4,5],dtype='U')
print(y)
print(y.dtype)

# n=np.array(['isuru','kumara','nimal'],dtype='i')
# print(n)
# print(n.dtype)
# can not do this

# convert another data type (astype())

x=np.array([1,2,0,4,5])
print(x)
print(x.dtype)

y=x.astype('f')
print(y)
print(y.dtype)

z=x.astype('bool')
print(z)
# 0 return False and any other value is return True
