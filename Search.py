import  numpy as np
print("\n----------------------------------------------where()------------------------")
# 1 D Array
arr = np.array([1,2,3,4,5])
result=np.where(arr==4)
print(result)

even_number_positions=np.where(arr%2==0)
print("Even number positions :",even_number_positions)


# 2 D Array     2 dimensional array means collection of 1 dimensional arrays
arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])
result=np.where(arr_2D==4)
print(result)


print("\n----------------------------------------------searchsorted()------------------------")

# this method can apply only for ordered array

arr=np.array([1,3,5,7,8])
x=np.searchsorted(arr,4)
print(x)

x=np.searchsorted(arr,4,side='right') # default=left
print(x)

y=np.searchsorted(arr,3)
print(y)

z=np.searchsorted(arr,[67,5,9,1])
print(z)