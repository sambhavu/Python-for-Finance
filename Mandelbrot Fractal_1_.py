from PIL import Image 
from numpy import complex, array 
import colorsys


#setting width of the output image 
WIDTH =1024

# return tuple of colors as ints of rgb 
def rgb_conv(i):
     color = 225*array(colorsys.hsv_to_rgb(i/225.0, 1.0, 0.5))
     return tuple(color.astype(int)) 

#mandelbrot function

def mandelbrot(x,y): 
     c0 = complex(x,y) 
     c=0
     for i in range (1,1000): 
          if abs(c) > 2:
              return rgb_conv(i)
          c=c*c+c0
     return (0,0,0) 

#creating an image in RGB

img = Image.new('RGB', (WIDTH, int(WIDTH/2)))

pixels = image.load()

for x in range (image.size[0]):
     print("%.2f%%" % (x/WIDTH*100.0))


image.show()
