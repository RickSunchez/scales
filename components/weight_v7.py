import os
from tkinter import S, CENTER, Canvas, PhotoImage

class Weight:
    def __init__(self, context=Canvas, value=5):
        self.ctx = context
        self.x = 50
        self.y = 150

        __dir = os.path.dirname(os.path.realpath(__file__))
        __imagePath = os.path.join(__dir, "src/weight.png")

        self.__image = PhotoImage(file=__imagePath).subsample(10, 10)

        self.width = self.__image.width()
        self.height = self.__image.height()

        self.__value = value
        
    def draw(self):
        self.ctx.create_image(
            self.x, self.y,
            anchor=S, image=self.__image
        )

        self.__label()

    def __label(self):
        w2 = self.width // 2
        frame = self.__atSource([
            [-w2+10, -15], 
            [w2-10, -45]])
        text = self.__atSource([[0, -30]])[0]

        self.ctx.create_rectangle(frame, outline=None, fill="white")
        self.ctx.create_text(
            text,
            justify=CENTER,
            font="Courier 22",
            text=self.__value,
            fill="black"
        )

    def __atSource(self, points, addX=0, addY=0):
        for i in range(len(points)):
            points[i][0] += self.x + addX
            points[i][1] += self.y + addY

        return points