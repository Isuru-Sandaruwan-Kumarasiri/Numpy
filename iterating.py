import  numpy as np

x=np.array([1,2,3,4,5])

for i in x:
    print(i,end=',')


print("\n","-"*50)
# 2 D Array     2 dimensional array means collection of 1 dimensional arrays
arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])

print(arr_2D)
for i in arr_2D:
    for j in i:
        print(j,end=',')


# nditer()
print("\n-----------------------------nditr()--------------------------")
arr_2D = np.array([[1,2,3],[1,6,8],[2,3,4]])

for i in np.nditer(arr_2D):
    print(i,end=',')

for i in np.nditer(arr_2D[:,::2]):
    print(i )

for i,j in np.ndenumerate(arr_2D):
    print(i,"-",j )
