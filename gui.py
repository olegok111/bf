#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import ut
from PyQt5.QtWidgets import QApplication, QWidget


def main(title_info: ut.TitleInfo) -> None:
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(*ut.RESOLUTION)
    w.move(*ut.INIT_WINDOW_POS)
    w.setWindowTitle(title_info.title)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    t_inf = ut.TitleInfo(title_override='gui.py testing mode')
    main(t_inf)
