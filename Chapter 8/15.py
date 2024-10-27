# Color negative Image Convertor

from graphics import *

def main()->None:

    filename=input("Enter the name of a file containing a GIF or PPM image:")

    win=GraphWin("Color Negative Image Convertor Converter",500,500)
    
    image=Image(Point(250,250),filename)
    image.draw(win)

    width=image.getWidth()
    height=image.getHeight()

    win.getMouse()
    for i in range(width):
        for j in range(height):
            r,g,b=image.getPixel(i,j)
            image.setPixel(i,j,color_rgb(255-r,255-g,255-b))
        win.update() #Every column updated
    output_file=input("Enter the name for output file:")
    image.save(output_file)

if __name__=='__main__':
    main()