from tkinter import Tk, filedialog

def seleccionar_excel():
    root = Tk()
    root.withdraw()

    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx")]
    )

    return archivo