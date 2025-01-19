print("\n----------------------------------------------concatenate()------------------------")


import  numpy as np

arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])

new_arr=np.concatenate((arr_1,arr_2))
print(new_arr)


arr_2D_1= np.array([[1,2,3],[1,6,8],[2,3,4]])
arr_2D_2= np.array([[5,2,8],[9,2,7],[2,2,1]])

new_arr=np.concatenate((arr_2D_1,arr_2D_2))
new_arr_1=np.concatenate((arr_2D_1,arr_2D_2),axis=1)
print(new_arr)
print(new_arr_1)


print("\n----------------------------------------------array_split()------------------------")

arr = np.array([1,2,3,4,5])

new_arr=np.array_split(arr,3)
print(new_arr)


arr_2D= np.array([[1,2,3],[1,6,8],[2,3,4]])
new_arr=np.array_split(arr_2D,2)
print(new_arr)