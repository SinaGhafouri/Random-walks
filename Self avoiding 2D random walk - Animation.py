#Animation for self avoiding random walk.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

t1 = time.time()
r = [[0,0]] #Random walk
rejection = 0 #0 = not rejected, 1 = just rejected.
memory = 10
steps = 1000
i = 0 #step counter
c = 0 #counter
while i<steps:
    p = np.random.random()
    if rejection==0: r.append([])
    if p<.25 and [r[-2][0]+1,r[-2][1]] not in r[-1:-memory-1:-1]:
        r[-1].append(r[-2][0]+1)
        r[-1].append(r[-2][1])
        rejection = 0
    elif p>=.25 and p<.5 and [r[-2][0],r[-2][1]+1] not in r[-1:-memory-1:-1]:
        r[-1].append(r[-2][0])
        r[-1].append(r[-2][1]+1)
        rejection = 0
    elif p>=.5 and p<.75 and [r[-2][0]-1,r[-2][1]] not in r[-1:-memory-1:-1]:
        r[-1].append(r[-2][0]-1)
        r[-1].append(r[-2][1])
        rejection = 0
    elif p>=.75 and [r[-2][0],r[-2][1]-1] not in r[-1:-memory-1:-1]:
        r[-1].append(r[-2][0])
        r[-1].append(r[-2][1]-1)
        rejection = 0
    else:
        c += 1
        rejection = 1
        continue
    if [r[-1][0]-1,r[-1][1]] in r[-1:-memory-1:-1] and [r[-1][0]+1,r[-1][1]] in r[-1:-memory-1:-1] and [r[-1][0],r[-1][1]-1] in r[-1:-memory-1:-1] and [r[-1][0],r[-1][1]+1] in r[-1:-memory-1:-1]:
        print('rejected at {}th step'.format(len(r)-1))
        break
        
    i += 1
    c += 1
  
#print(i/c)
r = np.array(r)  
t2 = time.time()
print('Duration: {:.4} sec.'.format(t2-t1))

fig = plt.figure(facecolor='black')
plt.style.use('dark_background')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
plt.plot(0,0,'bo', label='starting point')
plt.legend(loc='upper right', framealpha=.5)
plt.plot(r[:,0][-1],r[:,1][-1],'ro', label='finishing point')
plt.legend(loc='upper right', framealpha=.5)
plt.plot(r[:,0],r[:,1])
plt.title('2D Random Walk')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""Animation"""
print('The memory here is {}.'.format(memory))
print('Loading ...')
fig = plt.figure()
ax = fig.add_subplot(111,xlim=(min(r[:,0])-.5,max(r[:,0])+.5),ylim=(min(r[:,1])-.5,max(r[:,1])+.5))
ax.set_aspect('equal')
line1, = ax.plot([],[])
line2, = ax.plot([],[],',')
line3, = ax.plot([],[],'bo') #Start point
line4, = ax.plot([],[],'r*') #End point - rejected
line5, = ax.plot([],[],'g*') #End point - successfully finished to the end point

X,Y = [],[]
def animate(i):
    X.append(r[:,0][i])
    Y.append(r[:,1][i])
    line1.set_data(X[-1:-memory-1:-1],Y[-1:-memory-1:-1])
    line2.set_data(X[:-memory:1],Y[:-memory:1])
    if i==0: line3.set_data(X[0],Y[0])
    if i==len(r[:,0])-1 and i!=steps:
        #print('Naaay Lost =[.')
        line4.set_data(X[-1],Y[-1])
    elif i==steps:
        line5.set_data(X[-1],Y[-1])
        #print('Yaaaay Won =].')
    return line1, line2, line3, line4, line5

anim = animation.FuncAnimation(fig,animate,len(r),interval=50,repeat=False)
plt.show()
