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
def draw_handler(canvas):
    canvas.draw_polyline(pos, 10, 'Red')
    canvas.draw_line([px-5,py],[px+5,py], 10, 'Green')
    
frame = simplegui.create_frame('Testing', 500, 500)
frame.set_keydown_handler(moveon)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, moveon)
print(1)
timer.start()
frame.start()
