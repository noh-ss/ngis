# ngis TEST 작업입니다.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu, QGridLayout, QLabel, QTextEdit, QLineEdit, QDialog, QPushButton



class DialogPassword(QDialog):

    def __init__(self):
        super().__init__()
        self.execDialog()

    def execDialog(self):

        self.setWindowTitle("비밀번호확인")
        self.setGeometry(500, 500, 300, 200)

        grid = QGridLayout()

        self.label1 = QLabel("테이블")
        self.label2 = QLabel("설명")
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.btn   = QPushButton('close')
        self.btn.clicked.connect(self.closeDialog)

        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.edit1, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.edit2, 1, 1)
        grid.addWidget(self.btn, 2, 0, 1, 2)

        self.setLayout(grid)

    def closeDialog(self):
        self.close()

class Ngis(QMainWindow):

    def __init__(self):
        super().__init__()
        self.execUI()

    def execUI(self):

        # file menu
        # file >> Automatic Programs
        programAct = QAction('&Automatic Programs', self)
        programAct.setShortcut('Ctrl+G')
        programAct.setStatusTip('Automatic generation of Programs')
        programAct.triggered.connect(self.autoProgram)

        # file >> Exit
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        # Database menu
        # Database >> Password
        passwordAct = QAction('&Password', self)
        passwordAct.setShortcut('Ctrl+D')
        passwordAct.setStatusTip('Password check')
        passwordAct.triggered.connect(self.passwordCheck)

        # Database >> DB Backup
        backupAct = QAction('&DB Backup', self)
        backupAct.setShortcut('Ctrl+B')
        backupAct.setStatusTip('Backup Database')
        backupAct.triggered.connect(self.backupDB)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(programAct)
        fileMenu.addAction(exitAct)

        databaseMenu = menubar.addMenu('&Database')
        databaseMenu.addAction(passwordAct)
        databaseMenu.addAction(backupAct)

        self.toolbar = self.addToolBar('exit')
        self.toolbar.addAction(exitAct)

        self.statusBar().showMessage('Ready')
        self.setGeometry(500, 500, 1024, 768)
        self.setWindowTitle('RBA(Roh\'s Business Automation)')
        self.show()

    def backupDB(self):
        self.setGeometry(500, 500, 1024, 768)
        self.setWindowTitle('RBA(Roh\'s Business Automation)')
        self.show()

    def autoProgram(self):

        grid2 = QGridLayout()

        self.lb1 = QLabel("프로그램명")
        self.lb2 = QLabel("테이블명")
        self.ed1 = QLineEdit()
        self.ed2 = QLineEdit()

        grid2.addWidget(self.lb1, 0, 0)
        grid2.addWidget(self.ed1, 0, 1)
        grid2.addWidget(self.lb2, 1, 0)
        grid2.addWidget(self.ed2, 1, 1)

        self.setLayout(grid2)
        self.show()


    def passwordCheck(self):
        passDialog = DialogPassword()
        passDialog.exec_()

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
