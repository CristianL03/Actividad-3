from tkinter import*
import math
root = Tk()
root.title("Datos del triangulo equilatero")
root.geometry("600x150")
lado = IntVar()
perimetro = StringVar()
altura = StringVar()
area = StringVar()
def triangulo():
    P = 3*(lado.get())
    H = ((math.sqrt(3))*lado.get())/2
    A = ((lado.get()**2)*math.sqrt(3))/4
    area.set(f"Area:{A}")
    perimetro.set(f"Perimetro:{P}")
    altura.set(f"Altura:{H}")
texto = Label(root, text="Ingrese el lado del triangulo:")
texto.place(x=30, y=10)
entrada = Entry(root, textvariable=lado)
entrada.place(x=185, y=10)
res1 = Entry(root, textvariable=perimetro, state="disabled")
res1.place(x=30,y=40)
res2 = Entry(root, textvariable=altura, state="disabled")
res2.place(x=170,y=40)
res3 = Entry(root, textvariable=area, state="disabled")
res3.place(x=310,y=40)
boton = Button(root, text="Calcular", command=triangulo)
boton.place(x=300, y=80)
root.mainloop()