import  numpy as np

print("*"*10,"1 D Array ","*"*10)

# 1 D Array
arr = np.array([1,2,3,4,5])
print(arr)
print('slicing array :', arr[1:3])
print('one position to end:', arr[2:])
print('one position to start:', arr[:-3])
print("step wise", arr[1::2])

print("*"*10,"2 D Array ","*"*10)

# 2 D Array     2 dimensional array means collection of 1 dimensional arrays
arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])
print(arr_2D)
print("2nd Row and 1 to 3 elements : ",arr_2D[1,1:])
print("3rd column : ",arr_2D[:,2])



print("*"*10,"3 D Array ","*"*10)

# 3 D Array    3 dimensional array means collection of 2 dimensional arrays
arr_3D = np.array([[[1,2,3],[5,6,3]],[[5,7,3],[3,4,7]],[[3,4,0],[3,7,9]]])
print(arr_3D)
print()

