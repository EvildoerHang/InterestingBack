"""
   ==============================================
    objectName： InterestingBack
    fileName：   Main_Pane
    Author:      Hang
    Date:        2019/10/31
    description: 主面板功能实现
   ==============================================

"""
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QTextImageFormat, QTextDocumentFragment, QTextListFormat, \
    QTextTableFormat, QTextFrameFormat
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, qApp, QPushButton, QLineEdit, QAction, QCompleter, QTextEdit

from resource.ui_Pane_Main import Ui_Form
import image_rc

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500, 500)
        self.setup_ui()
        self.setupUi(self)

    def setup_ui(self):

        pass
# ================================== start



# ================================== end

if __name__ == '__main__':
    # 测试
    # 判断当前模块是被导入执行还是直接执行
    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())

