#  Copyright 2018 Nobuo Tateishi<nob0tate14@gmail.com>
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import copy
import inspect
import subprocess
from tkinter import messagebox, StringVar, ttk
import tkinter

from alp.settings import BAT_DIR


smug = {}


class WindowCoreJ(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    def load_widget(self, rt, wdgs):
        print("load widget")
        global smug
        for wdg in wdgs:
            execex(locals(), f"{wdg['Name']}={wdg['Type']}(rt)")
            obj = eval(f"{wdg['Name']}")
            print(obj)
            if wdg["Type"] == "ttk.Entry":
#                 v = StringVar()
#                 obj["textvariable"] = StringVar()
                smug[wdg["Name"]] = obj
            # execex(locals(), f"parent={wdg['Name']}")
            if "Option" in wdg:
                for opt in wdg["Option"]:
                    exec(set_exc(
                        f"{wdg['Name']}['{opt}']={wdg['Option'][opt]}"))
            if "Widgets" in wdg:
                self.load_widget(obj, wdg["Widgets"])
            if isinstance(obj, ttk.Frame) and isinstance(rt, ttk.Notebook):
                rt.add(obj, text=(
                    wdg["Text"] if "Text" in wdg else ""), padding=3)
            else:
                pos = "side='left'"
                if wdg['Type'] == "ttk.Frame":
                    pos = "anchor='nw',pady=2"
                elif isinstance(obj, ttk.Notebook):
                    print("nb.pack")
                    pos = "expand=1, fill='both'"
                exec(set_exc(f"{wdg['Name']}.pack({pos})"))

    def load_widgets_j(self, rt, j: dict):
        top_keys = j.keys()
        for ky in top_keys:
            if ky == "Widgets":
                self.load_widget(rt, j[ky])
            else:
                exec(set_exc(f"rt.{ky}('{j[ky]}')"))

def set_exc(exc):
    print(exc)
    return exc


def execex(lcls, exc):
    print(exc)
    exec(exc, globals(), lcls)

def exec_bat(bnm, *parms):
    p = ""
    for pm in parms:
        p += " " + (smug[pm]).get()

    bt = "/".join([BAT_DIR, bnm])
    print(bt)
    print(p)
    # ret = subprocess.run([bt, p], shell=True, stdout=subprocess.PIPE)
    ret = subprocess.run(bt + " " + p, shell=True, stdout=subprocess.PIPE)
    ret_stdout = ret.stdout.decode("utf-8")
    print(ret_stdout)
    messagebox.showinfo('result', f"return code:{ret.returncode}")
