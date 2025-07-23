from tkinter import *

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(row=1, column=1)

g = Label(bg="green", width=20, height=5)
g.grid(row=2, column=2)

b = Label(bg="blue", width=40, height=5)
b.grid(row=3, column=1, columnspan=2)



window.mainloop()