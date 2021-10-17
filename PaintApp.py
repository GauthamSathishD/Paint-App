from tkinter import *

cur_x, cur_y = 0,0
color = 'black'

def find_xy(event):
    global cur_x, cur_y
    cur_x, cur_y = event.x, event.y

def newLine(event):
    global cur_x, cur_y
    canvas.create_line((cur_x,cur_y,event.x,event.y),fill = color)
    cur_x, cur_y = event.x, event.y
    
def reveal_colour(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()
    
window = Tk()

window.title('Gauthams Paint App')

window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

menubar = Menu(window)
window.config(menu = menubar)
submenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)

canvas= Canvas(window,background='white') 
canvas.grid(row=0,column=0,sticky='nsew')

canvas.bind('<Button-1>', find_xy)
canvas.bind('<B1-Motion>',newLine)

def display_pallete():
    id = canvas.create_rectangle((10,10,30,30),fill='black')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('black'))

    id = canvas.create_rectangle((10,40,30,60),fill='gray')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('gray'))

    id = canvas.create_rectangle((10,70,30,90),fill='brown4')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('brown4'))

    id = canvas.create_rectangle((10,100,30,120),fill='red')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('red'))

    id = canvas.create_rectangle((10,130,30,150),fill='orange')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('orange'))

    id = canvas.create_rectangle((10,160,30,180),fill='yellow')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('yellow'))

    id = canvas.create_rectangle((10,190,30,210),fill='green')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('green'))

    id = canvas.create_rectangle((10,220,30,240),fill='blue')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('blue'))

    id = canvas.create_rectangle((10,250,30,270),fill='purple')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('purple'))

    id = canvas.create_rectangle((10,280,30,300),fill='beige')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('beige'))

    id = canvas.create_rectangle((10,310,30,330),fill='teal')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('teal'))

    id = canvas.create_rectangle((10,340,30,360),fill='magenta')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('magenta'))

    id = canvas.create_rectangle((10,370,30,390),fill='pink')
    canvas.tag_bind(id, '<Button-1>', lambda x: reveal_colour('pink'))
    
display_pallete()

window.mainloop()
