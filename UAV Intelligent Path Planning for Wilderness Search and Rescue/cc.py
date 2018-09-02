import math
import operator
import matplotlib.pyplot as plt

file = open("C:\\Users\\Anirudh Shaktawat\\Downloads\\heatmap_2.txt", "rU")

probab = [[0 for x in range(100)] for y in range(100)]
cost = [[0 for x in range(200)] for y in range(200)]
visited = [[0 for x in range(200)] for y in range(200)]

for line in file:
    x,y,p  = map(float, line.split(' '))
    x = int(x)
    y = int(y)
    probab[x][y] = p
    if p!=0:
        cost[x][y] = 1

corner = []
distance = {}
flag = 0
cover=[]

for x in range(0,100,1):
    for y in range(0,100,1):
        if (probab[x][y] != 0.0):
            corner1 = [x,y]
            corner.append(corner1)
            flag = 1
            break
    if flag==1:
        flag=0
        break

for x in range(99, -1, -1):
    for y in range(99,-1,-1):
        if (probab[x][y] != 0.0):
            corner2 = [x,y]
            corner.append(corner2)
            flag = 1
            break
    if flag==1:
        flag=0
        break    
    
for y in range(0,100,1):
    for x in range(99,-1,-1):
        if (probab[x][y] != 0.0):
            corner3 = [x,y]
            corner.append(corner3)
            flag = 1
            break
    if flag==1:
        flag=0
        break

for y in range(99, -1, -1):
    for x in range(0,100,1):
        if (probab[x][y] != 0.0):
            corner4 = [x,y]
            corner.append(corner4)
            flag = 1
            break
    if flag==1:
        flag=0
        break


xs = [corner[0][0], corner[1][0], corner[2][0], corner[3][0]]
ys = [corner[0][1], corner[1][1], corner[2][1], corner[3][1]]
x_min = min(xs)
x_max = max(xs)
y_min = min(ys)
y_max = max(ys)

print(y_max)
cover.append((0,0))
visited[0][0]=1
   
k=y_min  
while visited[x_min][y_max]==0 or visited[x_max][y_max]==0:
  if k<=y_max:  
    for i in range(x_min, x_max+1, 1):
        cover.append((i,k))
        visited[i][k]=1
  if k<=y_max-1:      
    for i in range(x_max, x_min-1, -1):
        cover.append((i,k+1))
        visited[i][k+1]=1

  k=k+2    


if cover[len(cover)-1][0] < 50:
    x=0
    while x<=99:
        for y in range(99, -1, -1):
            if visited[x][y]!=1:
                cover.append((x,y))
                visited[x][y]=1
        for y in range(0,100,1):
            if visited[x+1][y]!=1:
                cover.append((x+1,y))
                visited[x+1][y]=1
        x=x+2        
elif cover[len(cover)-1][0] > 50:
    x=99
    while x>=0:
        for y in range(99, -1, -1):
            if visited[x][y]!=1:
                cover.append((x,y))
                visited[x][y]=1
        for y in range(0,100,1):
            if visited[x-1][y]!=1:
                cover.append((x-1,y))
                visited[x-1][y]=1
        x=x-2        


time = []
cdp = []
counter=0
pro = 0


f = open("output_cc_heatmap2.txt", "w")
for i in range(10000):
    x = str(cover[i])
    f.write(x)
    f.write("\n")

f.close()


for i in range(len(cover)):
    counter=counter+1
    pro = pro + probab[cover[i][0]][cover[i][1]]
    time.append(counter)
    cdp.append(pro)

plt.plot(time,cdp)
plt.xlabel('time')
plt.ylabel('CDP')
plt.show()


file.close()
