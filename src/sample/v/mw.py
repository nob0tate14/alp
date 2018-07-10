import json
import tkinter

from alp.ml import Alp


class MainWindow(tkinter.Tk):
    def __init__(self, filename):
        super().__init__()
        self.create_mf(filename)

    def loop_mainframe(self):
        self.mainloop()

    def create_mf(self, filename):
        f = open(f"{Alp.CONF_DIR}/{filename}", "r")
        j = json.load(f)
        alp = Alp()
        alp.load_widgets(self, j)

        mf = tkinter.Frame(master=self)
        mf.pack()

        mf.exit = tkinter.Button(mf, text="終了", fg="red",
                                 command=self.destroy)
        mf.exit.pack(side="bottom")

        img = tkinter.Image("photo", file=f"{Alp.CONF_DIR}/gracie.png")
        self.tk.call('wm', 'iconphoto', self._w, img)
