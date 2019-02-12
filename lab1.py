
"""
@author: Yahir F. Rivas
80621641
Instructor: Olac Fuentes
Teaching Assistant: Nath, Anindita
Lab1
MW 1:30 - 2:50
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k') 
        center[0]=center[0]*w #changes the position of the center
        draw_circles(ax,n-1,center,radius*w,w) #decreases radius of the circle for next recursive call
fig, ax = plt.subplots()
draw_circles(ax, 50, [100,0], 100,.5) 
#draw_circles(ax, 50, [100,0], 100,.9)
#draw_circles(ax, 110, [100,0], 100,.92)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circle.png')
        
def draw_squares(ax, n, center, w):
    if n>0:
        #sq creates the values of the square for each recursive call
        sq = np.array(((center[0]-w, center[1]-w),(center[0]+w, center[1]-w),(center[0]+w, center[1]+w)
        ,(center[0]-w, center[1]+w),(center[0]-w, center[1]-w)))
        
        ax.plot(sq[:,0],sq[:,1], color ='k')#plots square

        #Square is drawn on +/+ axis using w
        draw_squares(ax,n-1,(center[0]+w,center[1]+w), w/2)
        #Square is drawn on +/- axis using w
        draw_squares(ax,n-1,(center[0]+w,center[1]-w), w/2)
        #Square is drawn on -/- axis using w
        draw_squares(ax,n-1,(center[0]-w,center[1]-w), w/2)
        #Square is drawn on -/+ axis using w
        draw_squares(ax,n-1,(center[0]-w,center[1]+w), w/2)

fig, ax = plt.subplots()
draw_squares(ax,2,[0,0],10)
#draw_squares(ax,3,[0,0],10)
#draw_squares(ax,4,[0,0],10)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
        

def bin_tree(ax,p,n,x,y):
    if n>0:
        #changes points of x and y
        ax.plot([p[0],p[0]-x],[p[1],p[1]-y], color='k') #Left branches are graphed
        ax.plot([p[0],p[0]+x],[p[1],p[1]-y], color='k') #Right branches are graphed
        
        bin_tree(ax,[p[0]-x,p[1]-y],n-1,x*.5,y*.9)  #Left side recursive call
        bin_tree(ax,[p[0]+x,p[1]-y],n-1,x*.5,y*.9)  #Right side recursive call

fig, ax = plt.subplots()
bin_tree(ax, [0,0],3 , 75, 75)
#bin_tree(ax, [0,0], 4, 75, 75)
#bin_tree(ax, [0,0], 7, 75, 75)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('binary.png')

def crossed_circles(ax,n,c,r):
    if n>0:       
        #initial circle
        x,y=circle(c,r)
        ax.plot(x,y,color = 'k')
        r2 = r/3 #radius of smaller circles
        
        x,y= circle([c[0]+r-r2,c[1]],r2)
        ax.plot(x,y,color='k')
        #Plots left circle
        crossed_circles(ax,n-1,[c[0]+r-r2,c[1]],r2)
        x,y= circle([c[0]-r+r2,c[1]],r2)
        ax.plot(x,y,color='k')
        #Plots central circle
        crossed_circles(ax,n-1,[c[0]-r+r2,c[1]],r2)
        x,y= circle(c,r2)
        ax.plot(x,y,color='k')
        #Plots top circle 
        crossed_circles(ax, n-1, c, r2)
        x,y= circle([c[0],c[1]+r-r2],r2)
        ax.plot(x,y,color='k')
        #Plots bottom circle
        crossed_circles(ax, n-1,[c[0],c[1]+r-r2], r2)
        x,y= circle([c[0],c[1]-r+r2],r2)
        ax.plot(x,y,color='k')

        crossed_circles(ax, n-1,[c[0],c[1]-r+r2], r2)
        
fig, ax = plt.subplots()       
crossed_circles(ax,2,[100,100],13)
#crossed_circles(ax,3,[100,100],20)
#crossed_circles(ax,4,[100,100],50)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
     

       
        
      


