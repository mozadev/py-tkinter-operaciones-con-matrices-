import tkinter
from tkinter import messagebox
from random import randint


def calcular():
    n1 = txtnumero1.get()
    n2=int(n1)

    if (len(n1) == 0):
        messagebox.showinfo(message="el tamanio de la matrices !!", title="Mensaje")
        txtnumero1.focus()

    else:
        matriz = []
        matriz2 = []
        for r in range(n2):
            fila = []
            fila2 = []
            for c in range(n2):
                fila.append(randint(1, 100))
                fila2.append(randint(1, 100))
            matriz.append(fila)
            matriz2.append(fila2)

        area.insert(1.0, "matriz 1")
        area.insert(2.0,matriz)
        area.insert(4.0, "\n")
        area.insert(3.0, "matriz 2")
        area.insert(5.0,matriz2)

ventana = tkinter.Tk()  # instancia del formulario
ventana.title("Ventana Principal")
ventana.geometry("600x500")
# ventana.configure(background='green')
lblnumero1 = tkinter.Label(ventana, text='ingrese el tamnio de la matriz nxn:')
lblnumero1.place(x=100, y=50)
txtnumero1 = tkinter.Entry(ventana, width=20)
txtnumero1.place(x=310, y=50)

boton = tkinter.Button(ventana, text="procesar", command=calcular)
boton.place(x=250, y=100)
area = tkinter.Text(ventana)
area.config(width=80, height=13)
area.place(x=50, y=150)

ventana.mainloop()  # ejec