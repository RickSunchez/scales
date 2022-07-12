from tkinter import ALL, Button, Canvas, Tk
from components.scales_v2 import Scales

root = Tk()

canvas = Canvas(root, width=600, height=600)
canvas.grid(row=0, column=0, columnspan=4)

sc = Scales(canvas)

sc.draw()
root.mainloop()