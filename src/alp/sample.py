
from _io import TextIOWrapper
import os
from tkinter import ttk, StringVar, filedialog
import tkinter

root = tkinter.Tk()
t = StringVar()


def born_logic():
    f: TextIOWrapper
    if not os.path.isfile("./setting"):
        # f=open("setting","w")
        open_setting_window()
    else:
        f = open("setting", "r")
        print(f)


def show_filedialog():
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    t.set(file)
    print("open")


def open_setting_window():

    frm1 = ttk.Frame(root)
    frm1["relief"] = "groove"
    frm1["borderwidth"] = 1
    lbl1 = ttk.Label(frm1)
    lbl1["text"] = "設定ファイル"

    entry1 = ttk.Entry(frm1, textvariable=t)
    btn1 = ttk.Button(frm1, text='ファイル選択', command=show_filedialog)

    lbl1.pack(side=tkinter.LEFT)
    entry1.pack(side=tkinter.LEFT)
    btn1.pack()
    frm1.pack()
    entry1["width"] = 48

    root.mainloop()


if __name__ == '__main__':
    born_logic()
