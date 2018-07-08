import json
import tkinter

from alp.ml import Alp


class SubWindow1(tkinter.Tk):
    def __init__(self, filename):
        super().__init__()
        self.create_mf(filename)

    def loop_mainframe(self):
        self.mainloop()

    def create_mf(self, filename):
        f = open(f"{Alp.CONF_DIR}/{filename}", "r")
        j = json.load(f)
        alp = Alp()
        alp.load_widgets_j(self, j)

        mf = tkinter.Frame(master=self)
        mf.pack()

        mf.exit = tkinter.Button(mf, text="閉じる", fg="red",
                                 command=self.destroy)
        mf.exit.pack(side="bottom")
