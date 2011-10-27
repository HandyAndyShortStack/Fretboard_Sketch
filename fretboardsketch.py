from Tkinter import *

class Fretboard:
    
    """draws a canvas w/ interactive fretboard in a window

    takes a Tkinter.Tk() instance as an argument"""
    
    def __init__(self, master):
        
        canvas = Canvas(master, bg='white', height=175, width=150)
        canvas.pack()
        
        def make_grid(canvas):
            for x in range(12, 150, 25):
                canvas.create_line(x, 0, x, 174)
            for y in range(12, 175, 30):
                canvas.create_line(12, y, 137, y)       
        make_grid(canvas)

        fieldCenters = [ (x, y) for x in range(12, 150, 25)
                            for y in range(28, 175, 30) ]

        def field(centerX, centerY):
            area = []
            for x in range((centerX - 5), (centerX + 5)):
                for y in range((centerY -7), (centerY +7)):
                    area.append((x, y))
            return tuple(area)

        points = {}
        for fieldCenter in fieldCenters:
            for point in field(fieldCenter[0], fieldCenter[1]):
                points[point] = fieldCenter

        circles = {}
        def make_circle(event):
            if (event.x, event.y) in points.keys():
                center = points[(event.x, event.y)]
                if center not in circles.keys():
                    box = (
                        ((center[0] - 8), (center[1] - 8)),
                        ((center[0] + 8), (center[1] + 8)))
                    circle = canvas.create_oval(box[0][0], box[0][1],
                                                box[1][0], box[1][1],
                                                fill='black')
                    circles[center] = str(circle)
                else:
                    canvas.delete(circles[center])
                    del circles[center]

        canvas.bind('<Button-1>', make_circle)
            
root = Tk()

fretboard = Fretboard(root)

root.mainloop()
