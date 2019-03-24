from PIL.Image import *
from math import *
import numpy as np



#methode pour calculer la luminsité d 'un pixel
def luminosite(image,i,j):

    pixel=Image.getpixel(image,(i,j))
    brightness=sum(pixel)/3
	
    return brightness

#methode pour calculer l'energie d 'un pixel  
def energy(image,i,j):
   
   
 
  gx=luminosite(image,i-1,j-1) + (2*luminosite(image,i-1,j)) + luminosite(image,i-1,j+1) - luminosite(image,i+1,j-1) - (2*luminosite(image,i+1,j))-luminosite(image,i+1,j+1)

  gy=luminosite(image,(i-1),(j-1)) + (2*luminosite(image,i,(j-1))) + luminosite(image,(i+1),(j-1)) - luminosite(image,(i-1),(j+1)) - (2*luminosite(image,i,(j+1)))-luminosite(image,(i+1),(j+1))

  return sqrt(pow(gx,2)+pow(gy,2))

  
#methode pour calculer l'energie d 'un pixel  
def energyImage(image):

  w,h=image.size
  
  energie = np.zeros((h,w),dtype='f')
  
  for i in range(w):
  
   for j in range(h):
   
	      energie[j,i]=9000

  
  for i in range(1,w-1):
  
   for j in range(1,h-1):
   
	      energie[j,i]=energy(image,i,j)
	
  return energie
  
   
  
  
  
def Seam(energie):
    
	
    w = len(energie) # Largeur de l'image
    h = len(energie[0])# Longeur de l'image
    seam_d = [[None for y in range(h)] for x in range(w)]
    backtracker = [[None for y in range(h)] for x in range(w)]

    
    for y in range(h):
        for x in range(w):
            if y == 0:
                seam_d[x][y] = energie[x][y]
                backtracker[x][y] = -1
            else:
                if x == 0:
                    minimum = min(seam_d[x][y - 1], seam_d[x + 1][y - 1])
                    if minimum == seam_d[x][y - 1]:
                        backtracker[x][y] = 1
                    else:
                        backtracker[x][y] = 2
                elif x == w - 1:
                    minimum = min(seam_d[x][y - 1], seam_d[x - 1][y - 1])
                    if minimum == seam_d[x][y - 1]:
                        backtracker[x][y] = 1
                    else:
                        backtracker[x][y] = 0
                else:
                    minimum = min(seam_d[x - 1][y - 1], seam_d[x][y - 1], seam_d[x + 1][y - 1])
                    if minimum == seam_d[x - 1][y - 1]:
                        backtracker[x][y] = 0
                    elif minimum == seam_d[x][y - 1]:
                        backtracker[x][y] = 1
                    else:
                        backtracker[x][y] = 2

                seam_d[x][y] = energie[x][y] + minimum
    
    #Minim du tableau en partant de la base 
    min_num = seam_d[0][h - 1]
    index_min = 0
    for x in range(w):
        if min_num > seam_d[x][h - 1]:
            index_min = x
            min_num = seam_d[x][h - 1]

    #backtrack du seam minimal en partant du min de la base de l'image
    y_index = h - 1
    x_index = index_min
    seam = [[None for y in range(2)] for x in range(h)]
    seam[y_index][0] = x_index
    seam[y_index][1] = y_index
    while y_index > 0:
        backtrack = backtracker[x_index][y_index]
        if backtrack == 0:
            x_index -= 1
        elif backtrack != 1:
            x_index += 1
        y_index -= 1

        seam[y_index][0] = x_index
        seam[y_index][1] = y_index

    return seam
	
def SupprimerSeam(im, seam):
    
    w, h = im.size
    image = im.load()
    new_image = new("RGB", (w - 1, h), "white")
    pix = new_image.load()
    for y in range(h):
            bool = False
            for x in range(w):
                if not ((seam[y][0] == x) and (seam[y][1] == y)):
                    color = image[x, y]
                    if bool:
                        pix[x -1, y] = color
                    else:
                        pix[x, y] = color
                else:
                    bool = True


    return new_image
	

im=open("tele.jpg")
m=energyImage(im)
p=Seam(m)
t=SupprimerSeam(im,p)
t.save("tele2.jpg")
  
#ima=open("carve.jpg")
#a=energyImage(ima)
#c=Seam(a)
#d=SupprimerSeam(ima,c)
#d.save("care.jpg")
  
imag=open("tiger.jpg")
e=energyImage(imag)
f=Seam(e)
g=SupprimerSeam(imag,f)
g.save("tige.jpg")








	
	
	


  
