#!/usr/bin/python3
#-*-coding:utf-8-*-
from conv import ConvImg
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMessageBox,QWidget,QPushButton,QFileDialog
from PyQt5.QtGui import QIcon

class Conv2ImgApp (QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,300)
        self.center()
        self.setWindowTitle("文件转换器")
        self.setWindowIcon(QIcon("e.png"))
        self.paintButton()
        self.show()
    
    def paintButton(self):
        quitBtn = QPushButton("退出",self)
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        quitBtn.resize(quitBtn.sizeHint())
        quitBtn.move(500,250)

        openFileBtn = QPushButton("选择文件",self)
        openFileBtn.clicked.connect(self.openFile)
        openFileBtn.resize(openFileBtn.sizeHint())
        openFileBtn.move(250,150)

    def closeEvent(self,event):
        reply = QMessageBox.question(self,"退出确认","你要退出程序吗？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes :
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            conv = ConvImg()
            print(fname)
            result = conv.toImage(fname[0])
            QMessageBox.about(self,"结果",result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cia = Conv2ImgApp()
    sys.exit(app.exec_()) 
    