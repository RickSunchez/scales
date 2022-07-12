import tkinter

class Scales:
    def __init__(self, context:tkinter.Canvas, scale:int=1):
        self.ctx = context
        self.x = 50
        self.y = 0
        self.width = 400
        self.height = 400

    def draw(self):
        self.__frame()
        self.__base()
        self.__arm()
        self.__cup()

    def __base(self):
        points = [
            [198, 20],
            [190, 300],
            [150, 300],
            [150, 315],

            [250, 315],
            [250, 300],
            [210, 300],
            [202, 20]
        ]

        for i in range(len(points)):
            points[i][0] += self.x
            points[i][1] += self.y

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )
        
    def __arm(self):
        points = [
            [70,25],
            [80,25],
            [95,15],
            [195,15],
            [200,40],
            [205,15],
            [305,15],
            [320,25],
            [330,25],

            [330,20],
            [320,15],
            [305,5],
            [95, 5],
            [80,15],
            [70,20],
            [70,25],
        ]

        for i in range(len(points)):
            points[i][0] += self.x
            points[i][1] += self.y

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )

    def __cup(self):
        oval1 = [[5, 250], [145, 270]]
        line1 = [[5, 260], [5, 100]]
        arc = [[5, 30], [145, 170]]
        line2 = [[145, 100], [145, 260]]
        line3 = [[75, 20], [75, 35]]

        for i in range(len(oval1)):
            oval1[i][0] += self.x
            oval1[i][1] += self.y

        for i in range(len(line1)):
            line1[i][0] += self.x
            line1[i][1] += self.y

        for i in range(len(arc)):
            arc[i][0] += self.x
            arc[i][1] += self.y

        for i in range(len(line2)):
            line2[i][0] += self.x
            line2[i][1] += self.y

        for i in range(len(line3)):
            line3[i][0] += self.x
            line3[i][1] += self.y

        self.ctx.create_oval(
            oval1,
            fill="white",
            outline="grey")
        self.ctx.create_line(line1, fill="grey")
        self.ctx.create_arc(
            arc,
            start=0, extent=180,
            style=tkinter.ARC,
            outline="grey",
            fill="grey"
        )
        self.ctx.create_line(line2, fill="grey")

        self.ctx.create_line(line3, fill="grey")

    def __frame(self):
        points = [[3, 3], [self.width-3, self.height-3]]
        for i in range(len(points)):
            points[i][0] += self.x
            points[i][1] += self.y
        
        self.ctx.create_rectangle(
            points,
            outline="#f00", fill=None
        )