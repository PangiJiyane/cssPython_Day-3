# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:06:09 2024

@author: ccm
"""
import numpy as np
#conventional python - for loop
print("using just python:")
for i in np.arange(1,11,0.5):
    print(i)

#squaring the numbers from 1 to 5
#using jus python
squares=[]
for i in range(1,6):
    squares.append(i**2)
    print(squares)
    
squares =np.arange(1,6)**2
print (squares)
import matplotlib.pyplot as plt
x=np.arange(1,6)
y=x**2
print ("shape of x:")
print(x.shape)
print("shape of y:")
print (y.shape)
print(x*y)
print ("calculating dot product")
print (x.dot(y))
print ("calculate cross product")
print (np.matmul(x,y))
plt.plot(x,y,"r*")
plt.show()
"""
    alist= [1,2,5,6,15,22]
    data=np.array (alist)
    print (data)
    data2=data.reshape([2,3])
    data3=data.reshape([2,3])
    print ("data2")
    print(data2)
    print("data3")
    print(data3)
    alist2 =[[1,2,5,],[6,15,22]]
    
    data4=np.matmul(data2.T[0,:],data3)
    """
    #cross product of matrices 
"""
print ("cross product")
crossdata=np.cross(data2[0,:],data3[1,:])
print(crossdata)
a=np.array([[1,2,3],[4,5,6],[7,8,-9]])
b=np.array([3,-4,2])
d=np.linalg.det(a)
if(d>0):
    print(f"d={d},so this matrix is solvable")
    sol =np.linag.solve(a.b)

import numpy as np
data=np.loadtxt("noisydata.csv",skiprows=1,delimiter=",")
data_avg=np.mean(data,0)
print("average")
pressure=data[:,0]
flowrate=data[:,1]

fit=np.polyfir(pressure,flowrate,1)
flowfit=np.polyval(fit,pressure)
plt.plot(pressure,flowrate,"go")
plt.plot(pressure,flowfit,"k-")
plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
n=10000
x = np. random. uniform (size=n)
y = np. random. uniform(size=n)
print(sum(x*x+y*y <=1)/n*4)
plt. plot (x[x*x+y*y<=1] ,y [x*x+y*y<=1], "bo" )
plt. plot (x[x*x+y*y>1], y [x*x+y*y>1], "ro")
plt. show      
 
          
    