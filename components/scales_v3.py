import tkinter

class Scales:
    def __init__(self, context:tkinter.Canvas, scale:int=1):
        self.ctx = context
        self.x = 50
        self.y = 100
        self.width = 400
        self.height = 400

    def draw(self):
        self.__frame()
        self.__base()
        self.__arm()
        self.__cup()

    def __base(self):
        points = self.__reCalc([
            [198, 20],
            [190, 300],
            [150, 300],
            [150, 315],

            [250, 315],
            [250, 300],
            [210, 300],
            [202, 20]
        ], addY=80)

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )
        
    def __arm(self):
        points = self.__reCalc([
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
        ], addY=80)

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )

    def __cup(self):
        oval1 = self.__reCalc([[5, 250], [145, 270]], addY=80)
        line1 = self.__reCalc([[5, 260], [5, 100]], addY=80)
        arc = self.__reCalc([[5, 30], [145, 170]], addY=80)
        line2 = self.__reCalc([[145, 100], [145, 260]], addY=80)
        line3 = self.__reCalc([[75, 20], [75, 35]], addY=80)

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
        points = self.__reCalc([[3, 3], [self.width-3, self.height-3]])
        
        self.ctx.create_rectangle(
            points,
            outline="#f00", fill=None
        )

    def __reCalc(self, points, addX=0, addY=0):
        for i in range(len(points)):
            points[i][0] += self.x + addX
            points[i][1] += self.y + addY

        return points