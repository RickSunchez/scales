from tkinter import ALL, CURRENT, Button, Canvas, Tk
from components.scales import Scales
from components.weight import Weight

root = Tk()

def selectElement(event): 
    itemTags = canvas.gettags(CURRENT)

    if "is_move" in itemTags:     
        canvas.addtag_withtag("active", CURRENT)
        canvas.bind("<Motion>", moveElement)

def deselectElement(event):
    if not canvas.coords("active"): return

    canvas.dtag("active")
    canvas.unbind("<Motion>")

def moveElement(event):
    x = event.x
    y = event.y

    canvas.coords("active", x, y)

canvas = Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=4)

canvas.bind("<Button-1>", selectElement)
canvas.bind("<ButtonRelease-1>", deselectElement)

sc = Scales(canvas)
w = Weight(canvas)

def lMinus(): 
    sc.setLeft(-1)
    canvas.delete(ALL)
    sc.draw()
    
def lPlus():
    sc.setLeft(1)
    canvas.delete(ALL)
    sc.draw()

def rMinus():
    sc.setRight(-1)
    canvas.delete(ALL)
    sc.draw()
def rPlus():
    sc.setRight(1)
    canvas.delete(ALL)
    sc.draw()

Button(root, text="-", command=lMinus).grid(row=1,column=0)
Button(root, text="+", command=lPlus).grid(row=1,column=1)

Button(root, text="-", command=rMinus).grid(row=1,column=2)
Button(root, text="+", command=rPlus).grid(row=1,column=3)

sc.draw()
w.draw()

root.mainloop()