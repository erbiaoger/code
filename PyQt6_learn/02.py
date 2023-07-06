import sys
from PyQt6.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox
from PyQt6.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.resize(400, 400)
        self.center()
        
        self.statusBar().showMessage('Ready')


        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Butt', self)
        btn.setToolTip('This is a QpushButton widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QApplication.instance().quit)



        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Tooltips')
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

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

