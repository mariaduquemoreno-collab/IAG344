# https://docs.python.org/es/3/library/tkinter.html

import tkinter as tk
from tkinter import filedialog, messagebox
from proccessor import process_excel_safe #

# ================================================
# Funcion Seleccionar_excel
# ================================================

def seleccionar_excel ():
    return filedialog.askopenfilename(
    title = "Seleccionar archivo Excel.",
    filetypes = [ ( "Archivo Excel", "*.xlsx " )]
    )

# ================================================
# Funcion on_click_procesar
# ================================================

def on_click_procesar ():
    archivo = seleccionar_excel()
    exito, mensaje = process_excel_safe(archivo)
    if exito :
        messagebox.showinfo ( "Proceso completado", mensaje )
    else :
        messagebox.showerror ( "Error", mensaje)

# ================================================
# Funcion iniciar_app
# ================================================

def iniciar_app ():
    root = tk.Tk()
    root.title ("Procesador de archivos")
    root.geometry ("400x400")
    root.resizable (False, False)

    boton = tk.Button (
        root,
        text = "Seleccionar archivo Excel" ,
        command = on_click_procesar ,
        width = 30,
        height = 2
    )
    boton.pack (pady = 60)
    root.mainloop ()

