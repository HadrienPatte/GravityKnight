import numpy as np

gy = -9.81

x = [0,0]
vx = [0,0]
ax = 0

y = [0,0]
vy = [0,0]
ay = 0
dt = 0.00001

Fx = 0
Fy = 0
m = 1

def PFD(x,y,vx,vy,ax,ay,dt):
    ax = Fx/m
    ay = gy + Fy/m
    vx[1] = ax*dt + vx[0]
    vy[1] = ay*dt + vy[0]
    x[1] = 0.5*ax*(dt**2) + vx[0]*dt + x[0]
    y[1] = 0.5*ay*(dt**2) + vy[0]*dt + y[0]
    vx[0]=vx[1]
    x[0]=x[1]
    vy[0]=vy[1]
    y[0]=y[1]
    return(x[1],y[1],vx[1],vy[1])
