import numpy as np

x=np.array([1,2,3,4,5])



y=x.copy()

x[0]=9
print(x)
print(y) # not update the future updates


print("-"*40)

x=np.array([1,2,3,4,5])
y=x.view()

x[0]=9
print(x)
print(y) # update the future updates


print("-"*40)
                # Check original data in the array

x=np.array([1,2,3,4,5])

y=x.view()
z=x.copy()

print(y.base) # original data
print(z.base) # copy data