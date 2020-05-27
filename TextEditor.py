#fazer a verificação da versão do python no sistema
import sys
v = sys.version
if "2.7" in v:
    from Tkinter import *
    import tkFileDialog
elif "3." in v:
    from tkinter import *
    from tkinter import filedialog

#definição da tela
root = Tk()
text = Text(root)
text.grid()


#metodo de salvamento
def saveas():
    global text
    t = text.get("1.0","end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
button = Button(root, text="Save", command=saveas)
button.grid()

#trocar font para helvetica
def FontHelvetica():
    global text
    text.config(font="Helvetica")


#trocar font para courier
def FontCourier():
    global text
    tex.config(font=Courier)


#meu de troca de fonte
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)



#rodando o programa
root.mainloop()