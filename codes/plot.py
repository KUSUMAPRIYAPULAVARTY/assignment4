import numpy as np
import matplotlib.pyplot as plt

#Plotting all lines
x = np.linspace(-10, 10, 80)
y1=(-x-9)/3
y2 =3*x+2
plt.plot(x,y1, label ='x+3y+9=0')
plt.plot(x,y2, label = '-3x+y-2=0')
plt.plot(-1.5, -2.5, 'ro', label = 'intersection point(-1.5,-2.5)')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() 
#plt.savefig('hw4plot.png')
plt.show()
