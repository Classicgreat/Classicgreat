from random import randint
import time
def draw_screen(s):
    ss="_"*(len(s[0])+2)
    for i in range(len(s)):
        ss=ss+"\n|"
        for j in range(len(s[i])):
            ss=ss+s[i][j]
        ss=ss+"|"
    return ss+"\n"+"-"*(len(s[0])+2)
def sosed(y,x):
    col=0
    for k in range(-1,2):
        for l in range(-1,2):
            if k==0 and l==0:pass
            elif x+l>=len(data[y]) and y+k>=len(data):
                if data[0][0]==block:col+=1
            elif x+l>=len(data[y]):
                if data[y+k][0]==block:col+=1
            elif y+k>=len(data):
                if data[0][x+l]==block:col+=1
            elif data[y+k][x+l]==block:col+=1
    return col
def update():
    change=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            s=sosed(i,j)
            if data[i][j]==block:
                if s<2 or s>3:change.append([i,j])
            else:
                if s==3:change.append([i,j])
    if len(change)!=0:
        for i in range(len(change)):
            if data[change[i][0]][change[i][1]]==air:data[change[i][0]][change[i][1]]=block
            else:data[change[i][0]][change[i][1]]=air
        return 1
    else:return 0
def generate():
    data=[]
    for j in range(fov):
        dat=[]
        for i in range(fov*4):
            if randint(0,2)==0:dat.append(block)
            else:dat.append(air)
        data.append(dat)
    return data

air=" "
block="█"
fov=int(input("Enter fov:\n>>"))
data=generate()
i=1
while i:
    print("\n"*100)
    print(draw_screen(data))
    i=update()
    time.sleep(1.0)