import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.resize(250, 250)
        self.move(300, 300)

        self.setWindowTitle('First')
        self.show

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()