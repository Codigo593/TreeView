"""
Created on Tue Jan 11 20:16:32 2022
@author: crist
"""

import tkinter as tk
from tkinter import ttk
def ventanaPrincipal():
    ventana = tk.Tk()
    ventana.geometry("800x700")
    ventana.title("BIENVENIDO AL SORTEO")
    ventana.configure(background='dark turquoise')
    ventana.iconbitmap(r'LogoUniversidad.ico')
    ventana.resizable(0, 0)

    # etiquetas
    etiqueta_rut = tk.Label(ventana,width = 10, text="RUT", bg ="yellow")
    etiqueta_rut.place(x=30, y=50)
    etiqueta_nombre= tk.Label(ventana, width = 10, text="NOMBRE:", bg ="yellow")
    etiqueta_nombre.place(x=30, y=80)
    etiquet_apellido = tk.Label(ventana, width = 10, text="APELLIDO", bg ="yellow")
    etiquet_apellido.place(x=30, y=110)  
      
    yscrollbar = tk.Scrollbar(ventana) 
    yscrollbar.pack(side = tk.RIGHT, fill = tk.Y) 
    
    #Variables
    nombre = tk.StringVar()
    apellido = tk.StringVar()
    rut = tk.StringVar()

    #Entradas
    ent_rut = tk.Entry(ventana, textvariable=rut)
    ent_rut.place(x=110, y=50)
    ent_nombre = tk.Entry(ventana, textvariable=nombre)
    ent_nombre.place(x=110, y=80)
    ent_apellido = tk.Entry(ventana, textvariable=apellido)
    ent_apellido.place(x=110, y=110)
    #Tabla Socios
    arbol = ttk.Treeview(ventana, columns=("Rut","Apellidos", "Nombre"), show="headings")
    
    arbol.column("#1", width=80)
    arbol.column("#2", width=90)
    arbol.column("#3", width=90)
    arbol.heading("#1", text="Rut")
    arbol.heading("#2", text="Apellido")
    arbol.heading("#3", text="Nombre")
    arbol.place(x=280, y=50, width=500, height=230)

    scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=arbol.yview)
    arbol.configure(yscroll=scrollbar.set)
    scrollbar.place(x=780, y=50,width=20, height=230)
    #botones
    boton_registrar= tk.Button(ventana, text="Ingresar Concursante", width=20, height=3, bg ="yellow", command=lambda:GuardarDatos(arbol,rut, apellido, nombre, ent_rut, ent_nombre, ent_apellido))
    boton_registrar.place(x=30, y=350)
    boton_salir = tk.Button(ventana, text="Salir", width=20, height=3, bg ="pink",command=ventana.destroy)
    boton_salir.place(x=600, y=350)
    
    ventana.mainloop()
def GuardarDatos(tabla, rut_dato, apellido_dato, nombre_dato, entry_rut, entry_nomb, entry_apell):
      
    tabla.insert("",tk.END, values=(rut_dato.get(), nombre_dato.get(), apellido_dato.get()))
    entry_nomb.delete(0,tk.END)
    entry_apell.delete(0,tk.END)
    entry_rut.delete(0,tk.END)

ventanaPrincipal()
