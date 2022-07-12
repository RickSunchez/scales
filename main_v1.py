from tkinter import ALL, Button, Canvas, Tk
from components.scales_v1 import Scales

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=4)

sc = Scales(canvas)

sc.draw()
root.mainloop()