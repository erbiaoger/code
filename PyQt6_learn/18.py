import sys
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MplWidget(QtWidgets.QWidget):
    
        def __init__(self, parent=None):
            super(MplWidget, self).__init__(parent)
    
            self.canvas = MplCanvas(self)
            self.toolbar = NavigationToolbar(self.canvas, self)
    
            self.vbl = QtWidgets.QVBoxLayout()
            self.vbl.addWidget(self.canvas)  # the matplotlib canvas
            self.vbl.addWidget(self.toolbar)  # the matplotlib toolbar
            self.setLayout(self.vbl)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        mpl_btn = QtWidgets.QPushButton("MPL")
        mpl_btn.clicked.connect(self.mpl)
        layout.addWidget(mpl_btn)

        self.show()

    def mpl(self):
        self.mpl = MplWidget()
        self.mpl.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()