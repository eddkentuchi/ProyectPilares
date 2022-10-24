#Bibliotecas
from platform import win32_edition
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime

#Creación de archivo
sFileStamp = time.strftime('%Y%m%d')
sFileName = '\ProyectPilares\Data\PILARES' + sFileStamp + '.txt'
f=open(sFileName, 'a')

#Guardado de estado de tiempo
sTimeStamp = time.strftime('%H%M%S')
#f.write(sTimeStamp + '\n')
print (sTimeStamp)
#Variable de fila de botones
rowB= 5

#Colores
c1= "#9F2241" #Rojo
c2= "#235b4e" #Verde
c3= "Black" #Fuentes
c4= "#DDC9A3" #Dorado
c5= "#98989A" #Gris
c6= "White" #Blanco
"""
sTmpFileStamp = time.strftime('%Y%m%d')
if sFileStamp != sTmpFileStamp:
	f.write('Titulo'+'\n')
"""

#Definición de función de folio
def invoicePilares(themePilares):
	messageP= messageTxt.get(1.0,"end-1c")
	if len(messageP)!=0:
		f.write(themePilares + ',' + messageP +','+ sTimeStamp +'\n')
		print (themePilares + ',' + messageP +','+ sTimeStamp +'\n')
		openNewW()
	else:
		print("vacío")
		messagebox.showwarning("Cuidado","Folio Inválido")


#Segunda Ventana
def openNewW():
	windowInitP.withdraw()
	global win2
	win2=tk.Toplevel(windowInitP)
	win2.attributes('-topmost', True)
	win2.geometry("120x60+0+0")
	win2.title("Registro Pilares")
	win2.config(background=c6)
	#imageLP2 = tk.PhotoImage(file="Soy_PILARES2.png").subsample(10)
	#imageLPSmall2 = tk.Label(win2,image= imageLP2,background="red")
	buttonSix = tk.Button(win2,text ="Finalizar",
	width= 14,height =2,background=c4,
	activeforeground=c6,activebackground=c1,
	foreground=c3,command= lambda: initPilares("Finalizar"))
	#imageLPSmall2.grid(row=1,column=0,padx=5,pady =5)
	buttonSix.grid(row=1,column=1,padx=5,pady =10)

#Ventana Inicial
def initPilares(themePilares):
	sTimeStamp = time.strftime('%H%M%S')
	f.write(themePilares + ','+ sTimeStamp +'\n')
	print (themePilares + ','+ sTimeStamp +'\n')
	windowInitP.deiconify()
	win2.withdraw()

#Creación de Primer ventana
windowInitP = tk.Tk()
windowInitP.attributes('-topmost', True,'-fullscreen', True)
windowInitP.geometry("800x600+0+0")
windowInitP.title("Registro Pilares")
windowInitP.config(bg=c6)

#Imagenes pilares
imageLP = tk.PhotoImage(file="img\Soy_PILARES.png").subsample(5)
imageLPSmall = tk.Label(windowInitP,image= imageLP,background=c6)
imageCP = tk.PhotoImage(file="img\Cintillo.png").subsample(2)
imageCPSmall = tk.Label(windowInitP,image= imageCP,background=c6)

#Creación contenedores
invoiceP= tk.Label(windowInitP,text="Folio Pilares",font=("Vendana",16),foreground=c3,background=c6)
themeU= tk.Label(windowInitP,text="Uso de dispositivo",font=("Source_Sands_Pro",12),foreground=c3,background=c6)
messageTxt =tk.Text(windowInitP,width=30,height=2)

buttonOne = tk.Button(windowInitP,text ="Académico",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Academico"))

buttonTwo = tk.Button(windowInitP,text ="Laboral",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Laboral"))

buttonThree = tk.Button(windowInitP,text ="Servicios",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Servicios"))

buttonFour = tk.Button(windowInitP,text ="Lúdico",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Ludico"))

buttonFive = tk.Button(windowInitP,text ="Trámite",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Tramite"))

#Ubicación contenedores
imageLPSmall.grid(row=1,column=0,columnspan=8,padx=5,pady =0)
invoiceP.grid(row=2,column=0,columnspan=5,padx=5,pady =10)
messageTxt.grid(row=3,column=1,columnspan=3,padx=5,pady =5)
themeU.grid(row=4,column=1,columnspan=3,padx=5,pady =5)
buttonOne.grid(row=rowB,column=0,padx=20,pady =10)
buttonTwo.grid(row=rowB,column=1,padx=20)
buttonThree.grid(row=rowB,column=2,padx=20)
buttonFour.grid(row=rowB,column=3,padx=20)
buttonFive.grid(row=rowB,column=4,padx=20)
imageCPSmall.grid(row=rowB+1,column=0,columnspan=5,padx=5,pady =5)

sTmpFileStamp = time.strftime('%Y%m%d%H%M')



"""
if sTmpFileStamp != sFileStamp:
		  	f.close
            sFileName = '\out' + sFileStamp + '.txt'
		   	f=open(sFileName, 'a')
		   	sFileStamp = sTmpFileStamp
			print ("creando el archivo")

e_texto= Entry(ventana, font=("Calabri 20"))
buttonOne.grid(row=1,column=0,padx=20,pady =400)
"""
windowInitP.mainloop()