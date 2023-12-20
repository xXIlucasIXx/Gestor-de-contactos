import tkinter as tk
from tkinter import ttk

lista_contactos = []

def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()

    if nombre and telefono:  
        contacto = {"nombre": nombre, "telefono": telefono}
        lista_contactos.append(contacto)
        tree.insert("", "end", values=(nombre, telefono))  

def eliminar_contacto():
    seleccion = tree.selection()
    
    if seleccion:
        item = seleccion[0]
        indice = tree.index(item)
        lista_contactos.pop(indice)
        tree.delete(item)


ventana = tk.Tk()
ventana.title("Gestión de Contactos")

etiqueta_nombre=tk.Label(text="Nombre")
etiqueta_nombre.pack()
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)
etiqueta_telefono=tk.Label(text="Telefono")
etiqueta_telefono.pack()
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.pack(pady=5)


boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_contacto)
boton_agregar.pack(pady=5)
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_contacto)
boton_eliminar.pack(pady=5)


columns = ("Nombre", "Teléfono")
tree = ttk.Treeview(ventana, columns=columns, show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.pack(pady=10)



ventana.mainloop()