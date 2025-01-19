import numpy as np

x = np.array([2,3,4,5])
print(x)
print(x.ndim,"D Array")

# Two dimensional Array

y = np.array(
              [
                  [2,3,4,5],
                  [2,3,4,5]
              ]
           )

print(y)
print(y.ndim,"D Array")
# 3D Array

z = np.array([[[1,2],[2,3]],[[2,3],[3,9]]])
print(z)
print(z.ndim,"D Array")



# any other dimensional array convert to any dimensional array

n = np.array([1,2,3,4],ndmin=4)
print(n)
print(n.ndim)

