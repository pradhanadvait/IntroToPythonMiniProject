def moveon(key='0'):
    global pos
    check()
    over()
    print(pos)
    if(pos[0]==[px,py]):
        size()
    if(key=='0'):
        if(pos[0][0]>pos[1][0] and pos[0][1]==pos[1][1]):
            temp=[pos[0][0],pos[0][1]]
            pos[0][0]=pos[0][0]+10
            shift(temp)
        if(pos[0][0]<pos[1][0] and pos[0][1]==pos[1][1]):
            temp=[pos[0][0],pos[0][1]]
            pos[0][0]=pos[0][0]-10
            shift(temp)
        if(pos[0][1]>pos[1][1] and pos[0][0]==pos[1][0]):
            temp=[pos[0][0],pos[0][1]]
            pos[0][1]=pos[0][1]+10
            shift(temp)
        if(pos[0][1]<pos[1][1] and pos[0][0]==pos[1][0]):
            temp=[pos[0][0],pos[0][1]]
            pos[0][1]=pos[0][1]-10
            shift(temp)
    if(key!='0'):
        print(key)
        if(str(key)=='38'and pos[0][1]==pos[1][1] and pos[0][1]!=10):
            temp=[pos[0][0],pos[0][1]]
            pos[0][1]-=10
            print(key)
            shift(temp)
        if(str(key)=='39'and pos[0][1]!=pos[1][1] and pos[0][0]!=490):
            temp=[pos[0][0],pos[0][1]]
            pos[0][0]+=10
            print(key)
            shift(temp) 
        if(str(key)=='40'and pos[0][1]==pos[1][1] and pos[0][1]!=490):
            temp=[pos[0][0],pos[0][1]]
            pos[0][1]+=10
            print(key)
            shift(temp)
        if(str(key)=='37'and pos[0][1]!=pos[1][1] and pos[0][0]!=0):
            temp=[pos[0][0],pos[0][1]]
            pos[0][0]-=10
            print(key)
            shift(temp)
def size():
    global pos,px,py
    n=len(pos)
    if(pos[n-2][0]==pos[n-1][0]):
        pos.append([pos[n-1][0],pos[n-1][1]+10])
    elif(pos[n-2][1]==pos[n-1][1]):  
        pos.append([pos[n-1][0]+10,pos[n-1][1]])
    px,py=random.randint(1,49),random.randint(1,49)
    px*=10
    py*=10
