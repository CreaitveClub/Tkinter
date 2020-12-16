import tkinter as tk
import tkinter.font as font
from tkinter import *

from PIL import ImageTk, Image

# ***********************************************************
# ***********************************************************
splash_root = tk.Tk()
splash_root.title("Veni Vidi Vici")
splash_root.iconbitmap(r'i.ico')
splash_root.geometry("400x250+500+250")
a = ImageTk.PhotoImage(Image.open('aa.png'))
ph = Label(image=a)
ph.pack()
# ***********************************************************
# ***********************************************************
f = 0
forc = ''


def mainw():
    splash_root.destroy()

    root = tk.Tk()

    root.title("Sezar Shifrelemesi")
    root.geometry("800x500+280+50")
    root.iconbitmap(r'i.ico')
    root.state('zoomed')

    herfb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    herfk = "abcdefghijklmnopqrstuvwxyz"

    root.configure(bg="#D648CE")
    myfont = font.Font(family='Times', size=20)
    myfont1 = font.Font(family='Times', size=15)
    def koder():
        shifr = ""
        soz = tb.get()
        for i in range(len(soz)):
            for j in range(len(herfk)):
                if soz[i] == herfk[j]:
                    if j <= len(herfk) - 4:
                        shifr += herfk[j + 3]
                    else:
                        shifr += herfk[j - (len(herfk) - 3)]
                elif soz[i] == herfb[j]:
                    if j <= len(herfb) - 4:
                        shifr += herfb[j + 3]
                    else:
                        shifr += herfb[j - (len(herfb) - 3)]
                elif soz[i] == ' ':

                    global f
                    if f != i:
                        shifr += ' '
                        f = i
        # print(shifr)
        global forc
        label.config(text=shifr)
        forc = shifr
        tb.delete(0, END)

    def dekoder():
        deshifr = ""
        soz = tb.get()
        for i in range(len(soz)):
            for j in range(len(herfk)):
                if soz[i] == herfk[j]:
                    if j <= len(herfk) + 4:
                        deshifr += herfk[j - 3]
                    else:
                        deshifr += herfk[j - (len(herfk) + 3)]
                elif soz[i] == herfb[j]:
                    if j <= len(herfb) + 4:
                        deshifr += herfb[j - 3]
                    else:
                        deshifr += herfb[j - (len(herfb) + 3)]
                elif soz[i] == ' ':
                    global f
                    if f != i:
                        deshifr += ' '
                        f = i
        # print(deshifr)
        label.config(text=deshifr)
        global forc
        forc = deshifr
        tb.delete(0, END)

    def copy():

        root.clipboard_clear()
        root.clipboard_append(forc)

    koder = tk.Button(root, text='Shifrele', font=myfont, border=5, bg='#A7DDFA', fg='red', padx=10, pady=5,command=koder)
    koder.place(relwidth=0.3, relheight=0.1, relx=0.1, rely=0.35)

    dekoder = tk.Button(root, text='Deshifrele', font=myfont, border=5, bg='#A7DDFA', fg='red', padx=10, pady=5,
                        command=dekoder)
    dekoder.place(relwidth=0.3, relheight=0.1, relx=0.6, rely=0.35)

    yazi = tk.StringVar()

    tb = tk.Entry(root, width=4, border=3, font=myfont, textvariable=yazi)
    tb.grid(column=0, row=1)
    tb.place(relwidth=0.6, relheight=0.1, relx=0.2, rely=0.15)

    label = tk.Label(root, width=4, font=myfont, text='')
    label.grid(column=0, row=1)
    label.place(relwidth=0.55, relheight=0.1, relx=0.2, rely=0.5)

    copy = tk.Button(root, text='Kopy', font=myfont1, border=2, bg='#A7DDFA', fg='red', padx=10, pady=5, command=copy)
    copy.place(relwidth=0.08, relheight=0.1, relx=0.72, rely=0.5)


splash_root.after(4000, mainw)
mainloop()
