from tkinter import ALL, Button, Canvas, Tk
from components.scales import Scales
from components.weight_v7 import Weight

root = Tk()

canvas = Canvas(root, width=800, height=800)
canvas.grid(row=0, column=0, columnspan=4)

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