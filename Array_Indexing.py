import  numpy as np

# 1 D Array
arr = np.array([1,2,3,4,5])
print(arr)
print(arr[2])



# 2 D Array     2 dimensional array means collection of 1 dimensional arrays
arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])
print(arr_2D)
print(arr_2D[1][2])


# 3 D Array    3 dimensional array means collection of 2 dimensional arrays
arr_3D = np.array([[[1,2,3],[5,6,3]],[[5,7,3],[3,4,7]],[[3,4,0],[3,7,9]]])
print(arr_3D)
print(arr_3D[2,1,2])