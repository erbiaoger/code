import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip, QMessageBox,
                             QMainWindow, QHBoxLayout, QVBoxLayout, QFileDialog, QSizePolicy)
from PyQt6.QtGui import QIcon, QFont, QAction, QGuiApplication
from PyQt6.QtCore import Qt

import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import dptf 

MyProgram = dptf.MyGPR()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        # 设置主窗口的位置和大小
        screen = QGuiApplication.primaryScreen()
        width = screen.geometry().width()
        height = screen.geometry().height()
        self.resize(width, height)
        
        # 创建一个主窗口的中心部件
        # 创建一个用于布局的QWidget对象，并设置其布局为垂直布局
        central_widget = QWidget()
        central_widget.setLayout(QHBoxLayout())
        self.setCentralWidget(central_widget)
        self.layout = central_widget.layout()

        # 设置主窗口的大小策略
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setSizePolicy(size_policy)

        # 设置主窗口的标题和图标
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('web.png'))
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is <b>csimGPR</b> GUI')

        # 初始化主窗口的菜单栏、工具栏和状态栏
        self.initFigure()
        self.initStatusBar()
        self.initMenu()
        #self.inittoggleMenu()
        self.initButtons()
        #self.inittoolbar()
        #self.initDialog()
        self.initModel(MyProgram)
        self.initData(MyProgram)
        self.imshowData(MyProgram)

        self.show()

    def initFigure(self):
        # 创建一个Matplotlib的Figure对象
        self.fig = Figure()
        # 创建一个Matplotlib的Canvas对象，并将Figure对象传递给它
        self.canvas = FigureCanvas(self.fig)
        # 将 Canvas 和工具栏添加到布局中
        toolbar = NavigationToolbar(self.canvas, self)
        new = QWidget()
        newLayout = QVBoxLayout()
        new.setLayout(newLayout)
        newLayout.addWidget(self.canvas, 0)
        newLayout.addWidget(toolbar, 0)
        self.layout.addWidget(new, 0)


    def initMenu(self):
        # define a menu bar
        menubar = self.menuBar()
        # First menu
        fileMenu = menubar.addMenu('File')
        EditMenu = menubar.addMenu('Edit')
        ViewMenu = menubar.addMenu('View')
        ToolsMenu = menubar.addMenu('Tools')
        AGCMenu = menubar.addMenu('AGC')
        HelpMenu = menubar.addMenu('Help')

        def act(name, shortcut, tip, func):
            # define a action
            name.setShortcut(shortcut)
            name.setStatusTip(tip)
            name.setCheckable(True)
            name.triggered.connect(func)

        openAct = QAction(QIcon('open.png'), 'Open', self)
        act(openAct, 'Ctrl+O', 'Open new File', \
            lambda: [self.importData(MyProgram), self.imshowData(MyProgram)])
        
        openModelAct = QAction(QIcon('open.png'), 'Open Model', self)
        act(openModelAct, 'Ctrl+M', 'Open new Model', \
            lambda: [self.importModel(MyProgram)])
        
        saveAct = QAction(QIcon('save.png'), 'Save', self)
        act(saveAct, 'Ctrl+S', 'Save File', \
            lambda: [self.saveData(MyProgram)])
        
        undoAct = QAction(QIcon('undo.png'), 'Undo', self)
        act(undoAct, 'Ctrl+Z', 'Undo', \
            lambda: [MyProgram.undo(), self.imshowData(MyProgram)])
        
        redoAct = QAction(QIcon('redo.png'), 'Redo', self)
        act(redoAct, 'Ctrl+R', 'Redo', \
            lambda: [MyProgram.redo(), self.imshowData(MyProgram)])

        fileMenu.addAction(openAct)
        fileMenu.addAction(openModelAct)
        fileMenu.addAction(saveAct)
        EditMenu.addAction(undoAct)
        EditMenu.addAction(redoAct)
    

    def initStatusBar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Statusbar')

    def initButtons(self):

        btnImshowPoint = QPushButton('Pick Point', self)
        btnImshowPoint.setToolTip('This is a <b>QPushButton</b> widget')
        #btn1.resize(self.btn1.sizeHint())
        btnImshowPoint.move(0, 0)
        btnImshowPoint.clicked.connect(lambda: [self.imshowPoint(MyProgram)])

        btnClickOn = QPushButton('Click On', self)
        btnClickOn.setToolTip('This is a <b>QPushButton</b> widget')
        #btn1.resize(self.btn1.sizeHint())
        btnClickOn.move(0, 1)
        btnClickOn.clicked.connect(lambda: [self.clickOn(MyProgram)])

        new = QWidget()
        newLayout = QVBoxLayout()
        new.setLayout(newLayout)
        newLayout.addWidget(btnImshowPoint, 0)
        newLayout.addWidget(btnClickOn, 0)
        self.layout.addWidget(new, 0, Qt.AlignmentFlag.AlignTop)

    def importData(self, MyProgram):
        filetypes = 'All (*.mat *.h5);;HDF5 (*.h5)'
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', filetypes)
        self.statusbar.showMessage('Importing data from ' + fname)
        MyProgram.importData(fname)
        self.statusbar.showMessage('Data imported! Data shape: '+str(MyProgram.spec.shape))

    def saveData(self, MyProgram):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save file', '.', 'GPRPy (*.gpr)')
        self.statusbar.showMessage('Save data to ' + fname)
        MyProgram.saveData(fname)
        self.statusbar.showMessage('Data saved!')

    def importModel(self, MyProgram):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.')
        self.statusbar.showMessage('Importing data from ' + fname)
        MyProgram.importModel(fname)
        self.statusbar.showMessage('Model imported')

    def initModel(self, MyProgram):
        fname = 'CED_west3.h5'
        MyProgram.importModel(fname)
        self.statusbar.showMessage('Model imported')

    def initData(self, MyProgram):
        fname = 'CFs_-115.0_-110.0_37.5_44.5.h5'
        MyProgram.importData(fname)
        self.statusbar.showMessage('Data imported')

    def imshowData(self, MyProgram):
        freq = MyProgram.freq
        velo = MyProgram.velo
        fname = MyProgram.name

        fig = self.fig; fig.clear(); ax = fig.add_subplot(111); ax.cla() 
        ax.imshow(MyProgram.spec,  extent=[min(freq), max(freq), min(velo), max(velo)],\
                   cmap='jet', interpolation='none', aspect='auto')
        ax.set_xlabel('Frequency (MHz)'); ax.set_ylabel('Velocity (m/ns)'); ax.set_title(f'{fname}')
        self.canvas.draw()

        return fig, ax
    
    def imshowPoint(self, MyProgram):
        MyProgram.pickPoint()
        point = MyProgram.point
        freq = MyProgram.freq
        velo = MyProgram.velo
        fname = MyProgram.name

        fig = self.fig; fig.clear(); ax = fig.add_subplot(111); ax.cla() 
        ax.imshow(MyProgram.spec,  extent=[min(freq), max(freq), min(velo), max(velo)],\
                   cmap='jet', interpolation='none', aspect='auto')
        ax.scatter(point[:,0], point[:,1], s=6, c='g', marker='+')
        ax.set_xlabel('Frequency (MHz)'); ax.set_ylabel('Velocity (m/ns)'); ax.set_title(f'{fname}')
        self.canvas.draw()

        return fig, ax
    
    def clickOn(self, MyProgram):
        MyProgram.pickPoint()
        self.points = MyProgram.point
        # 连接鼠标点击事件和回调函数
        self.canvas.mpl_connect('button_press_event', lambda event: self.on_canvas_click(event, MyProgram))

    
    def on_canvas_click(self, event, MyProgram):

        freq = MyProgram.freq
        velo = MyProgram.velo
        fname = MyProgram.name
        # 当鼠标点击时，获取点击的坐标
        x = event.xdata
        y = event.ydata

        # 将点击的坐标添加到点的列表中
        # points.append([x, y])
        # points = np.array(points)
        # print(points)
        self.points = np.vstack((self.points, [x, y]))

        #ax.plot(*zip(*self.points), 'ro')  # 绘制红色的点

        fig = self.fig; fig.clear(); ax = fig.add_subplot(111); ax.cla() 
        ax.imshow(MyProgram.spec,  extent=[min(freq), max(freq), min(velo), max(velo)],\
                   cmap='jet', interpolation='none', aspect='auto')
        ax.scatter(self.points[:, 0], self.points[:, 1], s=6, c='r', marker='x')
        ax.set_xlabel('Frequency (MHz)'); ax.set_ylabel('Velocity (m/ns)'); ax.set_title(f'{fname}')
        self.canvas.draw()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()