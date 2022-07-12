import math
import tkinter
from turtle import right

class Scales:
    def __init__(self, context:tkinter.Canvas, scale:int=1):
        self.ctx = context
        self.x = 50
        self.y = 100
        self.width = 400
        self.height = 400

        self.angle = -15

    def pivot(self):
        # pivot: 200 15
        return self.__atSource([[200, 15]], addY=80)[0]

    def lCupPivot(self):
        # 75, 25
        point = self.__atSource([[75, 25]], addY=80)
        return self.__atPivot(point, self.pivot(), self.angle)[0]
    
    def rCupPivot(self):
        # 325, 25
        point = self.__atSource([[325, 25]], addY=80)
        return self.__atPivot(point, self.pivot(), self.angle)[0]


    def draw(self):
        self.__base()
        self.__arm()
        self.__cup()

        self.__debug()

    def __base(self):
        points = self.__atSource([
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
        points = self.__atSource([
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

        points = self.__atPivot(
            points, 
            self.pivot(), 
            self.angle)

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )

    def __cup(self):
        oval1 = self.__atSource([[5, 250], [145, 270]], addY=80)
        line1 = self.__atSource([[5, 260], [5, 100]], addY=80)
        arc = self.__atSource([[5, 30], [145, 170]], addY=80)
        line2 = self.__atSource([[145, 100], [145, 260]], addY=80)
        line3 = self.__atSource([[75, 20], [75, 35]], addY=80)

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

    def __debug(self):
        frame = self.__atSource([[3, 3], [self.width-3, self.height-3]])
        # pivot = self.__atSource([[199, 14],[201, 16]], addY=80) # 200, 15

        # leftCup = self.__atSource([[74, 24], [76, 26]], addY=80) # 75, 25
        # rightCup = self.__atSource([[324, 24], [326, 26]], addY=80) # 325, 25

        self.ctx.create_rectangle(frame, outline="red", fill=None)

        self.__redPoint(self.lCupPivot())
        self.__redPoint(self.rCupPivot())
        self.__redPoint(self.pivot())

    def __redPoint(self, point):
        self.ctx.create_oval(
            point[0]-1, point[1]-1, point[0]+1, point[1]+1,
            outline="red", fill="red")

    def __atSource(self, points, addX=0, addY=0):
        for i in range(len(points)):
            points[i][0] += self.x + addX
            points[i][1] += self.y + addY

        return points

    def __atPivot(self, points, pivot=[0,0], angle=0):
        angle = angle * math.pi / 180

        for i in range(len(points)):
            dX = points[i][0] - pivot[0]
            dY = points[i][1] - pivot[1]
            shiftX = dX * math.cos(angle) - dY * math.sin(angle)
            shiftY = dX * math.sin(angle) + dY * math.cos(angle)

            points[i][0] = pivot[0] + shiftX
            points[i][1] = pivot[1] + shiftY

        return points