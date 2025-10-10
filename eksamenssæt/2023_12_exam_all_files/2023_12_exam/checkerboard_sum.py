import numpy as np

def checkerboard_sum(A):
    
    summen = 0
  
    for i in A[::2]:
        for n in i[::2]:
            summen += n

    for i in A[1::2]:
        for n in i[1::2]:
            summen += n
    
    return summen











A = np.array([[ 1.42, 4.0, 55.56, 63.0],
[ 2.22, 2.22, 33.73, 40.11],
[12.1, 17.24, 18.0, 33.5],
[21.15, 14.76, 17.3, 22.1],
[ 5.34, 6.0, 9.8, 8.18]])

print(checkerboard_sum(A))