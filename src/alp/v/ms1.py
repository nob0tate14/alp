import json
import tkinter

from alp.core.settings import CONF_DIR
from alp.core.wcj import load_widgets_j


class SubWindow1(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.create_mf()

    def loop_mainframe(self):
        self.mainloop()

    def create_mf(self):

        f = open(CONF_DIR + "/ms1.json", "r")
        j = json.load(f)
        load_widgets_j(self, j)

        mf = tkinter.Frame(master=self)
        mf.pack()

        mf.exit = tkinter.Button(mf, text="閉じる", fg="red",
                                 command=self.destroy)
        mf.exit.pack(side="bottom")
