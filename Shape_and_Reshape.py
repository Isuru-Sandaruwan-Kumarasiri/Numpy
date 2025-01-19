import numpy as np

arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])
print(arr_2D)

print(arr_2D.shape) # return the number of elemnts in array



arr_3D = np.array([[[1,2,3],[5,6,3]],[[5,7,3],[3,4,7]],[[3,4,0],[3,7,9]]])
print(arr_3D)
print(arr_3D.shape)


# How to edite the array as Owen dimensional

arr = np.array([1,2,3,5,6,7,8,9,4])
new_arr = arr.reshape(3,3) # we can edit only exist dimensional according to the given array
new_arr_2=arr.reshape(1,9)
new_arr_3=arr.reshape(9,1)
print(new_arr)
print(new_arr_2)
print(new_arr_3)


## conver to 3D array
arr = np.array([1,2,3,5,6,7,8,9])
# arr_3D=arr.reshape(2,2,2)
arr_3D=arr.reshape(2,2,2) # we must 2 dimensional
print(arr_3D)


print('\n---------------------------------------------------')

# 2D array to 1D array

arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])
new_arr=arr.reshape(-1) # any other array convert to 1D array
print(new_arr)