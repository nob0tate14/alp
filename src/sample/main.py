
from alp.ml import Alp
from sample.v.mw import MainWindow


if __name__ == '__main__':
    Alp.beginning()
    mw = MainWindow("mw.json")
    mw.loop_mainframe()
