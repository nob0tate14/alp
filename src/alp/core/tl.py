from os.path import dirname
import subprocess
from tkinter import ttk, StringVar
import tkinter

def get_alpconfpath():
    fl = __file__
    st = dirname(dirname(fl)) + "/conf"
    # print(st)
    return st


def get_path_conf():
    fl = __file__
    st = dirname(dirname(dirname(fl))) + "/resource/conf"
    # print(st)
    return st


def get_path_bat():
    fl = __file__
    st = dirname(dirname(dirname(fl))) + "/resource/bat"
    # print(st)
    return st


def set_exc(exc):
    print(exc)
    return exc


def execex(lcls, exc):
    print(exc)
    exec(exc, globals(), lcls)



