from platform import win32_edition
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
sFileStamp = time.strftime('%Y%m%d')
sFileName = '\Pilares_Registro\Data\PILARES' + sFileStamp + '.txt'
f=open(sFileName, 'a')
#Guardado de estado de tiempo
sTimeStamp = time.strftime('%H%M%S')
#f.write(sTimeStamp + '\n')
print (sTimeStamp)
#Variable de fila de botones
rowB= 5
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
		print("vacio")
		messagebox.showwarning("Cuidado","Folio Invalido")


#Segunda Ventana
def openNewW():
	windowInitP.withdraw()
	global win2
	win2=tk.Toplevel(windowInitP)
	win2.geometry("120x60+0+0")
	win2.title("Registro Pilares")
	win2.config(background="white")
	#imageLP2 = tk.PhotoImage(file="Soy_PILARES2.png").subsample(10)
	#imageLPSmall2 = tk.Label(win2,image= imageLP2,background="red")
	buttonSix = tk.Button(win2,text ="Finalizar",width= 14,height =2,command= lambda: initPilares("Finalizar"))
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
windowInitP.geometry("800x600+0+0")
windowInitP.title("Registro Pilares")
windowInitP.config(bg="white")

#Imagenes pilares
imageLP = tk.PhotoImage(file="img\Soy_PILARES.png").subsample(5)
imageLPSmall = tk.Label(windowInitP,image= imageLP,background="white")
imageCP = tk.PhotoImage(file="img\Cintillo.png").subsample(2)
imageCPSmall = tk.Label(windowInitP,image= imageCP,background="white")

#Creación contenedores
invoiceP= tk.Label(windowInitP,text="Folio Pilares",fg="black",font=("Vendana",12),background="white")
themeU= tk.Label(windowInitP,text="Uso de dispositivo",fg="black",font=("Vendana",12),background="white")
messageTxt =tk.Text(windowInitP,width=30,height=2)
buttonOne = tk.Button(windowInitP,text ="Educativo",width= 15,height =2,command= lambda: invoicePilares("Educativo"))
buttonTwo = tk.Button(windowInitP,text ="Laboral",width= 15,height =2,command= lambda: invoicePilares("Laboral"))
buttonThree = tk.Button(windowInitP,text ="Servicios",width= 15,height =2,command= lambda: invoicePilares("Servicios"))
buttonFour = tk.Button(windowInitP,text ="Lúdico",width= 15,height =2,command= lambda: invoicePilares("Ludico"))
buttonFive = tk.Button(windowInitP,text ="Entretenimiento",width= 15,height =2,command= lambda: invoicePilares("Entretenimiento"))

#Ubicación contenedores
imageLPSmall.grid(row=1,column=0,columnspan=5,padx=5,pady =5)
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