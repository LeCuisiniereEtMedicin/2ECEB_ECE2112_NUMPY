import numpy as np
#Lets create a 10x10 array of all the squares of numbers from 1 - 100
B = np.array([(1,2,3,4,5,6,7,8,9,10)])
x=11
while x <= 10**2:
    A = np.linspace(x,x+9,10)
    B = np.vstack((B,A))
    x = x+10
B = B**2
#LEts determine which elements are divisible by 3
C = B[B%3==0]