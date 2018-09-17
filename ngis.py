import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu


class Ngis(QMainWindow):

    def __init__(self):
        super().__init__()
        self.execUI()

    def execUI(self):

        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        backupAct = QAction('&DB Backup', self)
        backupAct.setShortcut('Ctrl+B')
        backupAct.setStatusTip('Backup Database')
        backupAct.triggered.connect(self.backupDB)

        programAct = QAction('&Automatic Programs', self)
        programAct.setShortcut('Ctrl+G')
        programAct.setStatusTip('Automatic generation of Programs')
        programAct.triggered.connect(self.autoProgram)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(programAct)
        fileMenu.addAction(exitAct)

        subMenu = QMenu('Oracle', self)
        subMenu.addAction(backupAct)

        editMenu = menubar.addMenu('&Database')
        editMenu.addMenu(subMenu)

        self.toolbar = self.addToolBar('exit')
        self.toolbar.addAction(exitAct)

        self.statusBar().showMessage('Ready')
        self.setGeometry(500, 500, 1024, 768)
        self.setWindowTitle('RBA(Roh\'s Business Automation)')
        self.show()

    def backupDB(self):
         print('backupDB print')

    def autoProgram(self):
         print('automatic Program')

# context menu setting 마우스 우클릭 시 나타나는 메뉴 설정
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

# key event handler
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ngis()
    sys.exit(app.exec_())