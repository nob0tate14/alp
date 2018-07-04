
import json
from os.path import dirname
from tkinter import ttk, StringVar
import tkinter
from tkinter.constants import N, E, S, W


def fnc_print():
    print("test")


def test_1():
    frame1 = ttk.Frame(root)
    label1 = ttk.Label(frame1, text='Your name:')

    t = StringVar()

    entry1 = ttk.Entry(frame1, textvariable=t)
    button1 = ttk.Button(frame1, text='OK', command=fnc_print)

    frame1.grid(row=0, column=0, sticky=(N, E, S, W))
    label1.grid(row=1, column=1, sticky=E)
    entry1.grid(row=1, column=2, sticky=W)
    button1.grid(row=2, column=2, sticky=W)

    for child in frame1.winfo_children():
        child.grid_configure(padx=5, pady=5)


fl = __file__
st = dirname(dirname(fl))
print(st)
f = open(st + "/resource/conf/smp.json", "r")
j = json.load(f)

root = tkinter.Tk()
root.title(j["root"]["title"])
root.geometry(j["root"]["geometry"])
frm = ttk.Frame(root)
fr = j["main_frame"]
print(fr)
for obj in fr:
    print(obj)
    exec(obj["name"] + "=ttk." + obj["Type"] + "(frm," + obj["option"] + ")")

    exec(obj["name"] + ".pack()")


lbl = ttk.Label(frm, text="123")
lbl["text"] = "テキストラベル"
lbl.pack()
frm.pack()
print(frm)
root.mainloop()
