import simplegui
import random
pos=[[70,10],[60,10],[50,10],[40,10],[30,10],[20,10],[10,10]]
px,py=random.randint(1,49),random.randint(1,49)
px*=10
py*=10
def over():
    global pos
    t=False
    for i in range(0,len(pos)):
        for j in range(i+1,len(pos)):
            if(pos[i]==pos[j]):
                timer.stop()
                frame.stop()
        
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

def shift(pos0):
    global pos
    n=len(pos)
    temp=pos[0:n]
    temp[0]=pos0
    for i in range(0,n-1):
        pos[i+1]=temp[i]
    print(pos)

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
def check():
    global pos
    n=len(pos)
    if (pos[0][0]==490 and pos[1][0]!=490):
        temp=[pos[0][0],pos[0][1]]
        pos[0]=[490,temp[1]+10]
        shift(temp)
    if (pos[0][0]==10 and pos[1][0]!=10):
        temp=[pos[0][0],pos[0][1]]
        pos[0]=[10,temp[1]-10]
        shift(temp)
    if (pos[0][1]==490 and pos[1][1]!=490):
        temp=[pos[0][0],pos[0][1]]
        pos[0]=[temp[0]-10,490]
        shift(temp)
    if (pos[0][1]==10 and pos[1][1]!=10):
        temp=[pos[0][0],pos[0][1]]
        pos[0]=[temp[0]+10,10]
        shift(temp)
def draw_handler(canvas):
    canvas.draw_polyline(pos, 10, 'Red')
    canvas.draw_line([px-5,py],[px+5,py], 10, 'Red')
    
frame = simplegui.create_frame('Testing', 500, 500)
frame.set_keydown_handler(moveon)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, moveon)
print(1)
timer.start()
frame.start()
