print ("Hello","\n")
for i in range(0, 10, 2):
    print("wartosc: ", i, " ", end='') 
# print(sep='\n')
names = ["Ania", "Kasia", "Jan", "Piotr", "Paweł"]
for name in names:
    print("Cześć", name) 


from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me")

btn.grid(column=1, row=0)

window.mainloop()