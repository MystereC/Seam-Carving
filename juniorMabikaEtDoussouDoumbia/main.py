from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk




def hello():
   return 30;
   
def GetFiles():

    
    Canevas = Canvas()
    filename = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('jpg files','.jpg'),('bmp files','.bmp'),('all files','.*')])
	
    photo = ImageTk.PhotoImage(file=filename)                  # Nécessaire pour travailler avec différents types d'images
	
    Canevas.config()  # Règle la taille du canvas par rapport à la taille de l'image 
    Canevas.create_image(0,0,anchor=NW,image=photo)            # Règle l'emplacement du milieu de l'image, ici dans le coin Nord Ouest (NW) de la fenetre    
    print(filename)
    Canevas.pack(side=TOP)
    mainloop()
    return filename


	
fenetre = Tk()
fenetre.title('Seam Carving')
 

menuBAR = Menu(fenetre)

sousmenu = Menu(menuBAR, tearoff=0)
menuBAR.add_cascade(label="file", menu= sousmenu) 
sousmenu.add_command(label="ouvrir image", command=GetFiles)
sousmenu.add_separator()
sousmenu.add_separator()
sousmenu.add_command(label="quitter", command=hello)



fenetre.config(menu=menuBAR)






fenetre.mainloop()


