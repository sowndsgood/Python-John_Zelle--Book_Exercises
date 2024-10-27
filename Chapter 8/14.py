# Grayscale Image Convertor

from graphics import *

def main()->None:

    filename=input("Enter the name of a file containing a GIF or PPM image:")

    win=GraphWin("Grayscale Converter",500,500)
    
    image=Image(Point(250,250),filename)
    image.draw(win)

    width=image.getWidth()
    height=image.getHeight()

    win.getMouse()
    for i in range(width):
        for j in range(height):
            r,g,b=image.getPixel(i,j)
            brightness=int(round(0.299*r+0.587*g+0.114*b))
            image.setPixel(i,j,color_rgb(brightness,brightness,brightness))
        win.update() #Every column updated
    output_file=input("Enter the name for output file:")
    image.save(output_file)

if __name__=='__main__':
    main()