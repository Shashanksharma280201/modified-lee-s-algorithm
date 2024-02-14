import matplotlib.pyplot as plt
import time
from collections import deque

def pathpoly(path):
  xaxis=[]
  yaxis=[]
  print(path)
  for [x,y] in path:
      arr[x][y][2]=1
      xaxis.append(x)
      yaxis.append(y)
  plt.plot(xaxis,yaxis,'b')

def pathmetal(path):
  xaxis=[]
  yaxis=[]
  for [x,y] in path:
      arr[x][y][3]=1
      xaxis.append(x)
      yaxis.append(y)
  plt.plot(xaxis,yaxis,'red')

def surroundcheckmetal(s_x,s_y,dx,dy,arr):
  if(dx==0):
     if((((s_x+2)<len(arr)) and (arr[s_x+2][s_y][3]+arr[s_x+2][s_y-dy][3]==2)) or (((s_x+1)<len(arr)) and (arr[s_x+1][s_y][3]+arr[s_x+1][s_y-dy][3]==2)) or (((s_x-1)>=0) and (arr[s_x-1][s_y][3]+arr[s_x-1][s_y-dy][3]==2)) or (((s_x-2)>=0) and (arr[s_x-2][s_y][3]+arr[s_x-2][s_y-dy][3]==2))):return 0
     return 1
  else:
     if((((s_y+2)<len(arr[0])) and((arr[s_x][s_y+2][3]+arr[s_x-dx][s_y+2][3])==2)) or (((s_y+1)<len(arr[0])) and((arr[s_x][s_y+1][3]+arr[s_x-dx][s_y+1][3])==2)) or (((s_y-1)>=0) and ((arr[s_x][s_y-1][3]+arr[s_x-dx][s_y-1][3])==2)) or (((s_y-2)>=0) and ((arr[s_x][s_y-2][3]+arr[s_x-dx][s_y-2][3])==2))): return 0
     return 1

def surroundcheckpoly(s_x,s_y,dx,dy,arr):
  if(dx==0):
     if((((s_x+1)<len(arr)) and (arr[s_x+1][s_y][2]+arr[s_x+1][s_y-dy][2]==2)) or (((s_x-1)>=0) and (arr[s_x-1][s_y][2]+arr[s_x-1][s_y-dy][2]==2))):return 0
     return 1
  else:
     if((((s_y+1)<len(arr[0])) and((arr[s_x][s_y+1][2]+arr[s_x-dx][s_y+1][2])==2)) or (((s_y-1)>=0) and ((arr[s_x][s_y-1][2]+arr[s_x-dx][s_y-1][2])==2))): return 0
     return 1

def bfs_poly(arr, a, b):
    [x1, y1, _, _] = a
    [x2, y2, _, _] = b
    q = deque([(x1, y1, [])])
    visited = set()
    visited.add((x1, y1))
    path=[]
    while q:
        curr_x, curr_y, path = q.popleft()
        if [curr_x, curr_y] == [x2, y2]:
            return path + [[curr_x, curr_y]]
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            next_x, next_y = curr_x + dx, curr_y + dy
            if (
                0 <= next_x < len(arr)
                and 0 <= next_y < len(arr[0])
                and arr[next_x][next_y][2] == 0
                and (next_x, next_y) not in visited
                and surroundcheckpoly(next_x,next_y,dx,dy,arr)
            ):
                visited.add((next_x, next_y))
                q.append((next_x, next_y, path + [[curr_x, curr_y]]))
    #print(path)
    return path

def bfs_metal(arr, a, b):
    [x1, y1, _, _] = a
    [x2, y2, _, _] = b
    q = deque([(x1, y1, [])])
    visited = set()
    visited.add((x1, y1))
    path=[]
    while q:
        curr_x, curr_y, path = q.popleft()
        if [curr_x, curr_y] == [x2, y2]:
            return path + [[curr_x, curr_y]]
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            next_x, next_y = curr_x + dx, curr_y + dy
            if (
                0 <= next_x < len(arr)
                and 0 <= next_y < len(arr[0])
                and arr[next_x][next_y][3] == 0
                and (next_x, next_y) not in visited
                and surroundcheckmetal(next_x,next_y,dx,dy,arr)
            ):
                visited.add((next_x, next_y))
                q.append((next_x, next_y, path + [[curr_x, curr_y]]))
    # print(path)
    return path

def bfs_add_existing_poly(arr, a, b):
    [x1, y1, _, _] = a
    [x2, y2, _, _] = b
    q = deque([(x1, y1, [])])
    visited = set()
    visited.add((x1, y1))
    path=[]
    while q:
        curr_x, curr_y, path = q.popleft()
        if [curr_x, curr_y] == [x2, y2]:
            return path + [[curr_x, curr_y]]
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            next_x, next_y = curr_x + dx, curr_y + dy
            if [next_x, next_y] == [x2, y2]:
                return path +[[curr_x, curr_y]]+ [[next_x, next_y]]
            if (
                0 <= next_x < len(arr)
                and 0 <= next_y < len(arr[0])
                and arr[next_x][next_y][2] == 0
                and (next_x, next_y) not in visited
                and surroundcheckpoly(next_x,next_y,dx,dy,arr)
            ):
                visited.add((next_x, next_y))
                q.append((next_x, next_y, path + [[curr_x, curr_y]]))
    # print(path)
    print("Error connecting [",x1,",",y1,"] and [",x2,",",y2,"] try to check if the destination is reachable manually" )
    return []

def bfs_add_existing_metal(arr, a, b):
    [x1, y1, _, _] = a
    [x2, y2, _, _] = b
    q = deque([(x1, y1, [])])
    visited = set()
    visited.add((x1, y1))
    path=[]
    while q:
        curr_x, curr_y, path = q.popleft()
        if [curr_x, curr_y] == [x2, y2]:
            return path + [[curr_x, curr_y]]
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            next_x, next_y = curr_x + dx, curr_y + dy
            if [next_x, next_y] == [x2, y2]:
                return path +[[curr_x, curr_y]]+ [[next_x, next_y]]
            if (
                0 <= next_x < len(arr)
                and 0 <= next_y < len(arr[0])
                and arr[next_x][next_y][3] == 0
                and (next_x, next_y) not in visited
                and surroundcheckmetal(next_x,next_y,dx,dy,arr)
            ):
                visited.add((next_x, next_y))
                q.append((next_x, next_y, path + [[curr_x, curr_y]]))
    # print(path)
    print("Error connecting [",x1,",",y1,"] and [",x2,",",y2,"] try to check if the destination is reachable manually" )
    return []

arr=[]
for i in range(200):
    temp=[]
    for j in range(200):
        temp.append([i,j,0,0])
    arr.append(temp)

start = time.time()

#PMOS to Vdd
path=bfs_metal(arr,arr[12][165],arr[12][181])
pathmetal(path)

#PMOS to Vdd
path=bfs_metal(arr,arr[53][165],arr[53][181])
pathmetal(path)

#PMOS to Vdd
path=bfs_metal(arr,arr[95][170],arr[95][181])
pathmetal(path)

#PMOS to Vdd
path=bfs_metal(arr,arr[130][170],arr[130][181])
pathmetal(path)

#PMOS to Vdd
path=bfs_metal(arr,arr[162][157],arr[162][181])
pathmetal(path)

#PMOS to PMOS
path=bfs_metal(arr,arr[20][151],arr[20][124])
pathmetal(path)

#PMOS to PMOS
path=bfs_metal(arr,arr[60][151],arr[60][124])
pathmetal(path)

#NMOS to GND
path=bfs_metal(arr,arr[12][11],arr[12][0])
pathmetal(path)

#NMOS to GND
path=bfs_metal(arr,arr[53][11],arr[53][0])
pathmetal(path)

#NMOS to GND
path=bfs_metal(arr,arr[118][44],arr[118][0])
pathmetal(path)

#NMOS to GND
path=bfs_metal(arr,arr[162][98],arr[162][0])
pathmetal(path)

#NMOS to NMOS
path=bfs_metal(arr,arr[20][52],arr[20][25])
pathmetal(path)

#NMOS to NMOS
path=bfs_metal(arr,arr[60][52],arr[60][25])
pathmetal(path)

#NMOS to NMOS
path=bfs_metal(arr,arr[110][58],arr[110][85])
pathmetal(path)

#S
path=bfs_metal(arr,arr[12][110],arr[12][100])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[12][100],arr[52][100])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[52][100],arr[52][110])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[12][66],arr[12][70])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[12][70],arr[52][70])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[52][70],arr[52][66])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[32][100],arr[32][70])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[32][85],arr[85][0])
pathmetal(path)

#C
path=bfs_metal(arr,arr[170][143],arr[170][112])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[181][91],arr[170][127])
pathmetal(path)

#A
path=bfs_poly(arr,arr[0][117],arr[0][158])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][158],arr[16][158])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][117],arr[0][90])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][90],arr[16][59])
pathpoly(path)

#B
path=bfs_poly(arr,arr[0][82],arr[0][18])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][18],arr[16][18])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][18],arr[0][10])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][10],arr[40][10])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[40][10],arr[40][117])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[40][117],arr[56][117])
pathpoly(path)

#A'
path=bfs_poly(arr,arr[70][10],arr[70][158])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[70][158],arr[56][158])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[70][59],arr[56][59])
pathpoly(path)

#B'
path=bfs_poly(arr,arr[50][5],arr[50][18])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[50][18],arr[56][18])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[50][5],arr[78][5])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[78][5],arr[78][165])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[78][165],arr[30][165])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[30][165],arr[30][117])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[30][117],arr[16][117])
pathpoly(path)

#A to NAND
path=bfs_poly(arr,arr[0][158],arr[0][170])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[0][170],arr[99][170])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[99][170],arr[99][162])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[99][162],arr[114][92])
pathpoly(path)

#B to NAND
path=bfs_poly(arr,arr[40][10],arr[40][2])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[40][2],arr[100][2])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[100][2],arr[100][51])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[100][51],arr[114][51])
pathpoly(path)
path=bfs_add_existing_poly(arr,arr[114][51],arr[133][162])
pathpoly(path)

#NAND to INV
path=bfs_metal(arr,arr[103][155],arr[103][150])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[103][150],arr[137][150])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[137][150],arr[137][155])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[118][150],arr[118][99])
pathmetal(path)
path=bfs_add_existing_metal(arr,arr[118][127],arr[166][127])
pathmetal(path)
path=bfs_poly(arr,arr[166][150],arr[166][105])
pathpoly(path)

end = time.time()

print("The time of execution of above program is :",(end-start) * 10**3, "ms")
