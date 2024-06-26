# Prueba Técnica Fernando Herrera
import tkinter as tk
import os
from tkinter import filedialog
from handleEmail import send_email
from handleExcel import obtenerDatos
from help import filtrarDatos
from handleForm import sendForm

#funcion para obtener el nombre del archivo de excel
my_dir=None
def read_name(): 
    global my_dir
    my_dir = filedialog.askopenfile(filetypes=[("Archivos de Excel", "*.xlsx")]).name
    l1.config(text=my_dir)
    window.quit()
  
#Una simple gui para obtener el archivo excel
window = tk.Tk()
window.title("Prueba técnica")
window.geometry("800x600")

b1=tk.Button(window,text="Select File",font=22,command=lambda:read_name(),bg="lightgreen")
b1.grid(row=0,column=0,padx=10,pady=20)
l1=tk.Label(window,text=my_dir,bg="yellow",font=18)
l1.grid(row=0,column=1,padx=2)
window.mainloop()

#Funcion para obtener array de datos
print(my_dir)
registrosExcel = obtenerDatos(my_dir)

atrasados = filtrarDatos(registrosExcel,"Atrasado",9)
regularizados = filtrarDatos(registrosExcel,"Regularizado",9)

try:
    print("INICIO Envio emails")
    send_email(atrasados)
except Exception as e:
    #Hay un email (Eladio.Piña_yyy1234@Hotmail.com) que hace saltar una excepcion por que tiene un ñ, no pude solucionarlo, pero lo guardo como reto personal
    print("Hubo un error",e)

try:
    os.system('cls')
    print("INICIO Formulario")
    sendForm(regularizados)
    print("FIN PROGRAMA")
except Exception as e:
    print("Hubo un error",e)



