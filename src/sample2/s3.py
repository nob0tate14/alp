import json
from os.path import dirname
from tkinter import ttk, StringVar
import tkinter
from tkinter.constants import N, S, W, E


def fnc_print():
    print("test")


fl = __file__
st = dirname(dirname(fl))
print(st)
f = open(st + "/resource/conf/smp.json", "r")
j = json.load(f)

root = tkinter.Tk()
root.title(j["root"]["title"])
root.geometry(j["root"]["geometry"])

frame1 = ttk.Frame(root)
frame1["relief"] = "groove"
frame1["borderwidth"] = 1

label1 = ttk.Label(frame1, text='label dayo')

t = StringVar()

entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(frame1, text='OK', command=fnc_print)
label1["relief"] = "groove"
label1["borderwidth"] = 1

label1.pack(side=tkinter.LEFT)
entry1.pack(side=tkinter.LEFT)
button1.pack(side=tkinter.TOP)
label2 = ttk.Label(frame1, text='label dayodayo', borderwidth=4)
label2.pack(side=tkinter.LEFT)
label2["relief"] = "groove"
# label2["borderwidth"]=1
entry2 = ttk.Entry(frame1, textvariable=t)
entry2.pack(side=tkinter.TOP)

frame1.pack()
root.mainloop()
