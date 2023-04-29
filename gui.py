#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import ut
from config import*
from PyQt5.QtWidgets import QApplication, QWidget


def main(title_info: ut.TitleInfo) -> None:
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(*RESOLUTION)
    w.move(*INIT_WINDOW_POS)
    w.setWindowTitle(title_info.title)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    t_inf = ut.TitleInfo()
    main(t_inf)
