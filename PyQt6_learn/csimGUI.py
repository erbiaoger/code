import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, 
                             QLabel, QLineEdit, QTextEdit, QMainWindow, QToolTip,
                             QMessageBox, QMenu, QHBoxLayout, QVBoxLayout, QFileDialog)
from PyQt6.QtGui import QIcon, QFont, QAction
from PyQt6.QtCore import Qt

import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import dptf 

MyProgram = dptf.MyGPR()

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize the gprpy
        self.initUI()

    def initUI(self):
        self.resize(800, 400)
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('web.png'))
        #QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is <b>csimGPR</b> GUI')

        self.initStatusBar()
        self.initMenu()
        #self.inittoggleMenu()
        #self.initButtons()
        #self.inittoolbar()
        #self.initDialog()

        self.show()

    def initMenu(self):
        menubar = self.menuBar()
        # First menu
        fileMenu = menubar.addMenu('File')
        EditMenu = menubar.addMenu('Edit')
        ViewMenu = menubar.addMenu('View')
        ToolsMenu = menubar.addMenu('Tools')
        AGCMenu = menubar.addMenu('AGC')
        HelpMenu = menubar.addMenu('Help')
 
        openAct = QAction(QIcon('open.png'), 'Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open new File')
        openAct.setCheckable(True)
        openAct.triggered.connect(lambda: [self.importData(MyProgram), self.imshowData(MyProgram)])

        saveAct = QAction(QIcon('save.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save File')
        saveAct.setCheckable(True)
        saveAct.triggered.connect(lambda: [self.saveData(MyProgram)])

        undoAct = QAction(QIcon('undo.png'), 'Undo', self)
        undoAct.setShortcut('Ctrl+Z')
        undoAct.setStatusTip('Undo')
        undoAct.setCheckable(True)
        undoAct.triggered.connect(lambda: [MyProgram.undo(), self.imshowData()])

        redoAct = QAction(QIcon('redo.png'), 'Redo', self)
        redoAct.setShortcut('Ctrl+R')
        redoAct.setStatusTip('Redo')
        redoAct.setCheckable(True)
        redoAct.triggered.connect(lambda: [MyProgram.redo(), self.imshowData()])

        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        EditMenu.addAction(undoAct)
        EditMenu.addAction(redoAct)
    

    def initStatusBar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Statusbar')
    

    def importData(self, MyProgram):
        filetypes = 'All (*.mat *.2A *.gpr *.DT1 *.DZT *.GPRhdr *.rad);;\
        MAT (*.mat);;2A (*.2A);;GPRPy (*.gpr);;Sensors and Software (*.DT1);;\
            GSSI (*.DZT);;BSQ header (*.GPRhdr);;MALA header (*.rad)'

        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', filetypes)
        self.statusbar.showMessage('Importing data from ' + fname)
        MyProgram.importData(fname)
        self.statusbar.showMessage('Data imported! Data shape: '+str(MyProgram.data.shape))

    def saveData(self, MyProgram):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save file', '.', 'GPRPy (*.gpr)')
        self.statusbar.showMessage('Save data to ' + fname)
        MyProgram.saveData(fname)
        self.statusbar.showMessage('Data saved!')
        pass

    def imshowData(self, MyProgram):
        fig = MplCanvas(self, width=5, height=4, dpi=100)
        fig.axes.imshow(MyProgram.data, cmap='coolwarm', interpolation='none', aspect='auto')
        self.setCentralWidget(fig)
        toolbar = NavigationToolbar(fig, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(fig)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def loadData(self, MyProgram):
        filetypes = 'All (*.mat *.h5);;HDF5 (*.h5)'

        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', filetypes)
        self.statusbar.showMessage('Importing data from ' + fname)
        MyProgram.importData(fname)
        self.statusbar.showMessage('Data imported! Data shape: '+str(MyProgram.data.shape))

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()