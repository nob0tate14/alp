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

import configparser
import importlib
from logging import config, RootLogger
import logging
import os
from os.path import dirname, abspath
import subprocess
import sys
from tkinter import ttk, messagebox
import tkinter


def get_alplogger():
    return Alp.logger_


class Alp(object):
    INI_PATH = f"{dirname(abspath(__file__))}/setting.ini"
    ALP_DIR = dirname(dirname(dirname(abspath(__file__))))

    BAT_DIR = f"{ALP_DIR}/resource/bat"
    CONF_DIR = f"{ALP_DIR}/resource/conf"

    vase_ = {}
    logger_: RootLogger

    @staticmethod
    def beginning(ini_file=INI_PATH, logger=None):
        Alp.vase_ = {}
        cp = configparser.ConfigParser()
        cp.read(ini_file)
        prj_dir = dirname(dirname(dirname(dirname(abspath(__file__)))))

        if ini_file != Alp.INI_PATH:
            Alp.BAT_DIR = cp["alp.setting"]["bat_dir"]
            Alp.CONF_DIR = cp["alp.setting"]["conf_dir"]
        else:
            alp_dir = dirname(dirname(abspath(__file__)))
            Alp.BAT_DIR = eval(cp["alp.setting"]["bat_dir"])
            Alp.CONF_DIR = eval(cp["alp.setting"]["conf_dir"])

        if logger is None:
            Alp.logger_ = logging.getLogger("Alp")
        else:
            Alp.logger_ = logger

    def load_widget_sub(self, rt, wdgs):
        get_alplogger().debug("load widget")
        for wdg in wdgs:
            if wdg['Type'] == "ScrolledText":
                sc = importlib.import_module('tkinter.scrolledtext')
                exec(f"{wdg['Name']}=getattr(sc, 'ScrolledText')(rt)")
            else:
                exec(f"{wdg['Name']}=ttk.{wdg['Type']}(rt)")
            obj = eval(f"{wdg['Name']}")
            get_alplogger().debug(obj)
            Alp.vase_[wdg["Name"]] = obj
            # execex(locals(), f"parent={wdg['Name']}")
            if "Option" in wdg:
                for opt in wdg["Option"]:
                    if opt == "RunExec":
                        exec(
                            f"{wdg['Name']}['command']=lambda:exec_bat({wdg['Option'][opt]})")
                    elif opt == "Default" and wdg['Type'] == "Entry":
                        obj.insert(0, wdg['Option'][opt])
                    else:
                        exec(
                            f"{wdg['Name']}['{opt}']={wdg['Option'][opt]}")
            if "Widgets" in wdg:
                self.load_widget_sub(obj, wdg["Widgets"])
            if isinstance(obj, ttk.Frame) and isinstance(rt, ttk.Notebook):
                rt.add(obj, text=(
                    wdg["Text"] if "Text" in wdg else ""), padding=3)
            else:
                pos = "side='left'"
                if wdg['Type'] == "ScrolledText":
                    pos = "expand=2,fill='both'"
                elif wdg['Type'] == "Frame":
                    pos = "anchor='nw',pady=2,fill='x'"
                elif isinstance(obj, ttk.Notebook):
                    pos = "expand=1, fill='both'"
                exec(f"{wdg['Name']}.pack({pos})")

    def load_widgets(self, rt, j: dict):
        top_keys = j.keys()
        for ky in top_keys:
            if ky == "Widgets":
                self.load_widget_sub(rt, j[ky])
            else:
                exec(f"rt.{ky}('{j[ky]}')")

def exec_bat(retmode, bnm, *parms):
    p = ""
    for pm in parms:
        p += " " + (Alp.vase_[pm]).get()

    bt = "/".join([Alp.BAT_DIR, bnm])
    # ret = subprocess.run([bt, p], shell=True, stdout=subprocess.PIPE)
    ret = subprocess.run(bt + " " + p, shell=True, stdout=subprocess.PIPE)
    ret_stdout = ret.stdout.decode("utf-8")
    get_alplogger().debug(ret_stdout)
    if retmode == "D":
        messagebox.showinfo('result', f"return code:{ret.returncode}")
    else:
        show_windowsub1(ret)


def exec_py3(bnm, *parms):
    p = ""
    for pm in parms:
        p += " " + (Alp.vase_[pm]).get()

    ret = subprocess.run(f"python3 {bnm} {p}",
                         shell=True, stdout=subprocess.PIPE)
    ret_stdout = ret.stdout.decode("utf-8")
    get_alplogger().debug(ret_stdout)
    # messagebox.showinfo('result', f"return code:{ret.returncode}")
    show_windowsub1(ret)


def show_windowsub1(ret):
    # clss = locate("alp.v.ms1.SubWindow1")
    clss = getattr(importlib.import_module("alp.v.ms1"), "SubWindow1")
    ms = clss("ms1.json")
    Alp.vase_["lbl102"]["text"] = f"return code:{ret.returncode}"
    Alp.vase_["txt2"].insert(tkinter.INSERT, ret.stdout.decode("utf-8"))
    ms.loop_mainframe()
