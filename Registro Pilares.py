#Bibliotecas
from platform import win32_edition
import tkinter as tk
from tkinter import messagebox
import time
"""
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred)

db= firestore.client()

doc_ref = db.collection('employee').document('empdoc')

doc_ref.set({
		'name' : 'Eduardo'
		'iname'



})
"""
#Creación de archivo
sFileStamp = time.strftime('%Y%m%d')
sFileName = '\ProyectPilares\Data\PILARES' + sFileStamp + '.txt'
f=open(sFileName, 'a')

#Guardado de estado de tiempo y variables globales
sTimeStampInit = time.strftime('%H%M%S') 
sTimeStampFinish = time.strftime('%H%M%S')
usePilares = "Sin Uso"
#f.write(sTimeStamp + '\n')
#print (sTimeStamp)
#Variable de fila de botones
rowB= 1

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
	global usePilares
	usePilares =themePilares
	global sTimeStampInit
	sTimeStampInit = time.strftime('%H%M%S') 

	#usePilares = themePilares
	if len(messageP)!=0:
		#print (themePilares +'\n')
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
	#win2.iconbitmap("img\Soy_PILARES2.PNG") #Cambiar el icono
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
def initPilares(finishTime):
	messagePi= messageTxt.get(1.0,"end-1c")
	print(finishTime)
	global sTimeStampFinish
	sTimeStampFinish = time.strftime('%H%M%S')
	f=open(sFileName, 'a')
	f.write(usePilares + ',' + messagePi +','+ sTimeStampInit +','+sTimeStampFinish +'\n')
	print (usePilares + ',' + messagePi +','+ sTimeStampInit +','+sTimeStampFinish +'\n')
	f.close()
	windowInitP.deiconify()
	win2.withdraw()

#Creación de Primer ventana
windowInitP = tk.Tk()
#obtener tamaño total de la pantalla
xWindow =windowInitP.winfo_screenwidth()
yWindow= windowInitP.winfo_screenheight()
windowComplit= str(xWindow) + "x" + str(yWindow) + "+0+0"
windowInitP.geometry("800x600+0+0")
#print(windowComplit)

windowInitP.attributes('-topmost', True,'-fullscreen', True)
windowInitP.title("Registro Pilares")
windowInitP.config(bg=c6)


#Imagenes pilares	
imageLP = tk.PhotoImage(file="img\Soy_PILARES.png").subsample(5)
imageLPSmall = tk.Label(windowInitP,image= imageLP,background=c6)
imageCP = tk.PhotoImage(file="img\Cintillo.png").subsample(2)
imageCPSmall = tk.Label(windowInitP,image= imageCP,background=c6)

#Creación contenedores
sign_in= tk.Frame(windowInitP,bg=c6)
invoiceP= tk.Label(sign_in,text="Escribe tu folio PILARES",font=("Vendana",16),foreground=c3,background=c6)
messageTxt =tk.Text(sign_in,width=30,height=2)
teacherP= tk.Label(sign_in,text="Figura que atiende",font=("Vendana",16),foreground=c3,background=c6)
idTeacher =tk.Text(sign_in,width=30,height=2)

hackP= tk.Frame(windowInitP,bg=c6)

themeU= tk.Label(hackP,text="¿Para qué vas a usar este equipo?",font=("Vendana",12),foreground=c3,background=c6)

buttonOne = tk.Button(hackP,text ="Académico",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Academico"))

buttonTwo = tk.Button(hackP,text ="Laboral",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Laboral"))

buttonThree = tk.Button(hackP,text ="Servicios",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Servicios"))

buttonFour = tk.Button(hackP,text ="Lúdico",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Ludico"))

buttonFive = tk.Button(hackP,text ="Trámite",
width= 15,height =2,background=c4,
activeforeground=c6,activebackground=c1,
foreground=c3,command= lambda: invoicePilares("Tramite"))


# Expandir horizontalmente a columna 0.
windowInitP.columnconfigure(0, weight=1)
# Expandir verticalmente la fila 0.
windowInitP.rowconfigure(0, weight=1)

#Ubicación contenedores

imageLPSmall.grid(row=rowB,
column=0,columnspan=5,padx=5,pady =0)

sign_in.grid(row=rowB+1,
column=0,columnspan=6,padx=5,pady =50)
invoiceP.grid(row=1,
column=0,columnspan=2,padx=5,pady =20)
messageTxt.grid(row=2,
column=0,columnspan=2,padx=50,pady =5)
teacherP.grid(row=1,
column=4,columnspan=2,padx=5)
idTeacher.grid(row=2,
column=4,columnspan=2,padx=50)

hackP.grid(row=rowB+2,
column=0,columnspan=5,padx=5,pady =50)
themeU.grid(row=1,
column=0,columnspan=5,pady =20)
buttonOne.grid(row=2,
column=0,padx=20)
buttonTwo.grid(row=2,
column=1,padx=20)
buttonThree.grid(row=2,
column=2,padx=20)
buttonFour.grid(row=2,
column=3,padx=20)
buttonFive.grid(row=2,
column=4,padx=20)
imageCPSmall.grid(row=rowB+3,
column=0,columnspan=5,padx=5,pady =0)



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