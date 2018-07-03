import inspect
import json
import subprocess
import tkinter

from alp.core.tl import get_path_conf, execex, set_exc
from alp.core.wcj import WindowCoreJ


class MainWindow(tkinter.Tk, WindowCoreJ):
    def __init__(self):
        super().__init__()
        self.create_mf()

    def loop_mainframe(self):
        self.mainloop()

    def create_mf(self):

        f = open(get_path_conf() + "/mw.json", "r")
        j = json.load(f)
        self.load_widgets_j(self, j)

        mf = tkinter.Frame(master=self)
        mf.pack()

        mf.exit = tkinter.Button(mf, text="終了", fg="red",
                                 command=self.destroy)
        mf.exit.pack(side="bottom")
