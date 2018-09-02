import math
import operator
import matplotlib.pyplot as plt

file = open("C:\\Users\\Anirudh Shaktawat\\Downloads\\heatmap_2.txt", "rU")

probab = [[0 for x in range(200)] for y in range(200)]
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

    
for i in range(0,4,1):
    dist = float(math.sqrt(corner[i][0]**2 + corner[i][1]**2))    
    distance[(corner[i][0],corner[i][1])] = dist



#sorted_d= sorted(distance.items(), key = operator.itemgetter(1))
#xrect = sorted_d[0][0][0] 
#yrect = sorted_d[0][0][1]

cover = [(0,0)]
visited[0][0] = 1

if distance[(corner[2][0], corner[2][1])] < distance[(corner[3][0], corner[3][1])]:
    x_start = corner[2][0]
    y_start = corner[2][1]
    x_end = corner[3][0]
    y_end = corner[3][1]
else:
    x_start = corner[3][0]
    y_start = corner[3][1]
    x_end = corner[2][0]
    y_end = corner[2][1]

x = x_start
y = y_start
cover.append((x,y))
visited[x][y]=1
  
right = 1
while(visited[x_end][y_end]==0):
        if (right==1) and (visited[x+1][y]==0) and (cost[x+1][y] or cost[x][y] or cost[x+2][y] or cost[x+3][y] or cost[x+4][y] or cost[x+5][y]==1): 
            x = x+1
            cover.append((x,y))
            visited[x][y] = 1
        elif (right==0) and (visited[x-1][y]==0) and (cost[x][y] or cost[x-1][y] or cost[x-2][y] or cost[x-3][y] or cost[x-4][y] or cost[x-5][y]==1):
             x = x-1
             cover.append((x,y))
             visited[x][y] = 1
        else:
            for i in range(2):
                if right==1:
                    x=x+1
                    cover.append((x,y))
                    visited[x][y]=1                  
                    
                elif right==0:
                    x=x-1
                    cover.append((x,y))
                    visited[x][y]=1            
                    
            if y_start < y_end:
                y = y+1
                cover.append((x,y))
                visited[x][y]=1
            else:
                y = y-1
                cover.append((x,y))
                visited[x][y] = 1
            

            if(cost[x-1][y] or cost[x-2][y] or cost[x-3][y] or cost[x-4][y] or cost[x-5][y]==1) and (cost[x+1][y] or cost[x+2][y] or cost[x+3][y]==0):
                    right=0
            elif(cost[x-1][y] or cost[x-2][y] or cost[x-3][y] ==0) and (cost[x+1][y] or cost[x+2][y] or cost[x+3][y] or cost[x+4][y] or cost[x+5][y]==1):
                    right=1

for i in range(100):
    for j in range(100):
        if visited[i][j]!=1:
            cover.append((i,j))
            visited[i][j]=1

time = []
cdp = []
counter=0
pro = 0

f = open("output_cc_var_heatmap2.txt", "w+")
for i in range(len(cover)):
    counter=counter+1
    pro = pro + probab[cover[i][0]][cover[i][1]]
    time.append(counter)
    cdp.append(pro)
    x = str(cover[i])
    f.write(x)
    f.write("\n")
f.close()

plt.plot(time,cdp)
plt.xlabel('time')
plt.ylabel('CDP')
plt.show()

file.close()
