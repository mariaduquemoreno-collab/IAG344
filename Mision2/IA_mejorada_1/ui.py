# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import messagebox
from controller import procesar_instruccion
from utils import seleccionar_excel

archivo_seleccionado = None


def iniciar_app():
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")

    # Etiqueta
    tk.Label(
        root,
        text="Escriba una instrucción en lenguaje natural"
    ).pack(pady=10)

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)

    # Seleccionar archivo
    def seleccionar():
        global archivo_seleccionado
        archivo_seleccionado = seleccionar_excel()

        if archivo_seleccionado:
            messagebox.showinfo(
                "Archivo seleccionado",
                f"Archivo cargado:\n{archivo_seleccionado}"
            )

    # Ejecutar instrucción
    def ejecutar():
        global archivo_seleccionado

        if not archivo_seleccionado:
            messagebox.showerror(
                "Error",
                "Primero selecciona un archivo Excel"
            )
            return

        texto = entrada.get()

        if not texto.strip():
            messagebox.showerror(
                "Error",
                "La instrucción no puede estar vacía"
            )
            return

        exito, mensaje = procesar_instruccion(
            texto,
            archivo_seleccionado
        )

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    # Botones
    tk.Button(
        root,
        text="Seleccionar archivo",
        command=seleccionar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Ejecutar instrucción",
        command=ejecutar
    ).pack(pady=10)

    root.mainloop()
