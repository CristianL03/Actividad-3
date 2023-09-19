from tkinter import*
root = Tk()
root.title("Valores numericos")
root.geometry("600x180")
A = IntVar()
B = IntVar()
ig = StringVar()
def comparar():
    if A.get()==B.get():
        ig.set("A es igual a B")
    elif A.get()>B.get():
        ig.set("A es mayor")
    else:
        ig.set("B es mayor")
texto1 = Label(root, text="Ingrese el valor de A:")
texto1.place(x=30, y=30)
texto2 = Label(root, text="Ingrese el valor de B:")
texto2.place(x=30, y=55)
entrada1 = Entry(root, textvariable=A)
entrada1.place(x=150, y=30)
entrada2 = Entry(root, textvariable=B)
entrada2.place(x=150, y=55)
boton = Button(root, text="Comparar", command=comparar)
boton.place(x=300, y=130)
res = Entry(root, textvariable=ig, state="disabled")
res.place(x=30, y=100)
root.mainloop()