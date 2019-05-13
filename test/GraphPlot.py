x=[1,3,3,5,7,9,10,11,49]
y=[3,2,5,5,8,10,12,34,20]

import numpy as numpy

x_axis=numpy.array(x)
y_axis=numpy.array(y)

x_mean=numpy.mean(x_axis)
y_mean=numpy.mean(y_axis)

print("mean at x axis", x_mean)
print("mean at x axis", y_mean)

x_axis=x_axis-x_mean
y_axis=y_axis-y_mean


xSquare=x_axis*x_axis
slope=numpy.sum(y_axis*x_axis)/numpy.sum(xSquare)

print(slope)

y_intercept=y_mean-slope*x_mean

input=100
print(slope*input+y_intercept)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
finaY=slope*x_axis+y_intercept
ax.plot(x_axis,y_axis,'-bo' )
ax.plot(x_axis, finaY, '-go')
fig.savefig('graph.png')


