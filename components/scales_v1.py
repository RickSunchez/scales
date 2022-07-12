import tkinter

class Scales:
    def __init__(self, context:tkinter.Canvas, scale:int=1):
        self.ctx = context
        self.x = 0
        self.y = 0
        self.width = 400
        self.height = 400

    def draw(self):
        self.__frame()
        self.__base()
        self.__arm()
        self.__cup()

    def __base(self):
        self.ctx.create_polygon(
            198, 20,
            190, 300,
            150, 300,
            150, 315,

            250, 315,
            250, 300,
            210, 300,
            202, 20,
        )
        
    def __arm(self):
        self.ctx.create_polygon(
            70,25,
            80,25,
            95,15,
            195,15,
            200,40,
            205,15,
            305,15,
            320,25,
            330,25,

            330,20,
            320,15,
            305,5,
            95, 5,
            80,15,
            70,20,
            70,25,
            fill="white",
            outline="grey"
        )

    def __cup(self):
        self.ctx.create_oval(5, 250, 145, 270)
        self.ctx.create_line(5, 260, 5, 100)
        self.ctx.create_arc(
            5, 30, 145, 170,
            start=0, extent=180,
            style=tkinter.ARC
        )
        self.ctx.create_line(145, 100, 145, 260)

        self.ctx.create_line(75, 20, 75, 35)

    def __frame(self):
        self.ctx.create_rectangle(
            3, 3,
            self.width-3, self.height-3,
            outline="#f00", fill=None
        )