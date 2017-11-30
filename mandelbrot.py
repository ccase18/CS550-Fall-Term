import tkinter
import colorsys
from tkinter import *
xmin = -0.1270275204
xmax = -0.1270275014
ymin = -0.8398592158
ymax = -0.8398591968
WIDTH = 640 
HEIGHT = 640
maxIt = 255 



def mandelbrot(z, c, count):
	z = (z * z) + c
	count = count + 1

	if abs(z) >= 2:
		return count
	elif count > 254:
		return count
	else:
		return mandelbrot(z,c,count)



window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex((((xmax - xmin)/WIDTH) * col + xmin), (((ymax - ymin)/HEIGHT) * row + ymin))
        z = complex(0,0)
        r = mandelbrot(z, c, 0)
        rd = hex(r)[2:].zfill(2)
        gr = hex(255 - r)[2:].zfill(2)
        bl = hex(254)[2:].zfill(2)  
        img.put("#" + rd + gr + bl, (col, row))

canvas.pack()
canvas.postscript(file="file_name.ps", colormode='color')



xmin = -0.7545
xmax = -0.7538
ymin = 0.0513
ymax = 0.0520

window2 = Toplevel()
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex((((xmax - xmin)/WIDTH) * col + xmin), (((ymax - ymin)/HEIGHT) * row + ymin))
        z = complex(0,0)
        r = mandelbrot(z, c, 0)
        rd = hex(255 - r)[2:].zfill(2)
        gr = hex(r)[2:].zfill(2)
        bl = hex(100)[2:].zfill(2)
        img2.put("#" + rd + gr + bl, (col, row))

canvas2.pack()
canvas2.postscript(file="file_name.ps", colormode='color')



xmin = 0.3221
xmax = 0.3258
ymin = -0.4924
ymax = -0.4888

window3 = Toplevel()
canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")
img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex((((xmax - xmin)/WIDTH) * col + xmin), (((ymax - ymin)/HEIGHT) * row + ymin))
        z = complex(0,0)
        r = mandelbrot(z, c, 0)
        rd = hex(124)[2:].zfill(2)
        gr = hex(255 - r)[2:].zfill(2)
        bl = hex(r)[2:].zfill(2)    
        img3.put("#" + rd + gr + bl, (col, row))


canvas3.pack()
canvas3.postscript(file="file_name.ps", colormode='color')

mainloop()
    


