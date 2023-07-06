

import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, 
                             QPushButton, QToolTip, QMessageBox, 
                             QMenu, QHBoxLayout, QVBoxLayout, QGridLayout, 
                             QWidget, QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QFont, QIcon, QAction


class MainWindow_a(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.resize(800, 400)
        self.center()

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.initStatusBar()
        self.initMenu()
        self.inittoggleMenu()

        self.initButtons()

        self.inittoolbar()
        #self.initDialog()
        


        #self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Hello World')
        self.show()
    
    def initStatusBar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Statusbar')
    
    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        newAct = QAction('New', self)
        addMenu = QMenu('Add', self)
        addMenu.addAction('Add mail')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addMenu(addMenu)

    def inittoggleMenu(self):
        def toggleMenu(state):
            if state:
                self.statusbar.show()
            else:
                self.statusbar.hide()

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(toggleMenu)

        viewMenu.addAction(viewStatAct)

    def initButtons(self):
        btn = QPushButton('Butt', self)
        btn.setToolTip('This is a QpushButton widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QApplication.instance().quit)




    def inittoolbar(self):
        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(QApplication.instance().quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

    def initDialog(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Buttons')
        self.show()


    def center(self):
        qr = self.frameGeometry()                       # get a rectangle specifying the geometry of the main window
        cp = self.screen().availableGeometry().center() # get the center point of the screen

        qr.moveCenter(cp)                               # move the rectangle's center point to the screen's center point
        self.move(qr.topLeft())                         # move the top-left point of the application window to the top-left point of the qr rectangle, thus centering the window on our screen

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        # 重写了 QWidget 类中的 contextMenuEvent 方法
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")

        action = cmenu.exec(self.mapToGlobal(event.pos()))

        if action == quitAct:
            QApplication.instance().quit()
        elif action == newAct:
            self.statusbar.showMessage('new')
        elif action == openAct:
            widget_b = Widget_b()
            self.statusbar.showMessage('open')




class Widget_a(QWidget):

    def __init__(self):
        super().__init__()
        print('widget_a init')
        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


class Widget_b(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()







def main():

    app = QApplication(sys.argv)
    mainWindow = MainWindow_a()
    #widget = Widget_a()
    #widget = Widget_b()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()