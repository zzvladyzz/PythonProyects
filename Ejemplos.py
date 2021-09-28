from matplotlib.pyplot import show,plot,xlim,ylim 
from random import randint
from numpy import linspace,pi,sin
x=linspace(-pi,pi,256)
y=sin(x)

plot(x,y)
ylim(-2,2)
show()


