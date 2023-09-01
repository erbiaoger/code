import sys
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QSplitter, QApplication, QMainWindow)
from PyQt6.QtCore import (Qt, QUrl)
#from PyQt6.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebEngineCore import QWebEngineProfile
from PySide6.QtWebEngineCore import QWebEngineScript
from PyQt6.QtGui import QPalette, QPixmap, QBrush, QColor
from render_html import *

#pip3 install PyQt5==5.15.2
#pip3 install pyecharts==1.9.0

#所有图表参考https://pyecharts.org/#/zh-cn/intro
#范例和展示效果https://gallery.pyecharts.org/#/README
#使用方法https://www.jianshu.com/p/554d64470ec9
#加载速度https://www.cnblogs.com/tomoya0307/p/12737117.html
#参考范例模板https://blog.csdn.net/lildkdkdkjf/article/details/106571356



# render = render_in_browser()

class MainWindow(QMainWindow):

    print("init")
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.setBackground()

    #设置背景图
    def setBackground(self):
        palette = QPalette()
        pix = QPixmap("./images/bg.jpg")
        pix = pix.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)#自适应图片大小
        palette.setBrush(self.backgroundRole(), QBrush(pix))# 设置背景图片
        #palette.setColor(self.backgroundRole(), QColor(192, 253, 123))  # 设置背景颜色
        self.setPalette(palette)

    #画界面元素
    def initUI(self):
        main_box = QHBoxLayout(self)

        self.browser1 = QWebEngineView()
        #self.browser1.page().setBackgroundColor(Qt.transparent)
        self.browser1.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.browser1.load(QUrl("file:///html/title.html"))

        self.browser2 = QWebEngineView()
        #self.browser2.page().setBackgroundColor(Qt.transparent)
        self.browser2.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Geo_lines("html/geo_lines.html")
        self.browser2.load(QUrl("file:///html/geo_lines.html"))

        self.browser3 = QWebEngineView()
        #self.browser3.page().setBackgroundColor(Qt.transparent)
        self.browser3.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Liquid_data_precision("html/liquid_data_precision.html")
        self.browser3.load(QUrl("file:///html/liquid_data_precision.html"))

        self.browser4 = QWebEngineView()
        #self.browser4.page().setBackgroundColor(Qt.transparent)
        self.browser4.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Liquid_without_outline("html/liquid_without_outline.html")
        self.browser4.load(QUrl("file:///html/liquid_without_outline.html"))

        self.browser5 = QWebEngineView()
        #self.browser5.page().setBackgroundColor(Qt.transparent)
        self.browser5.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Gauge("html/gauge.html")
        self.browser5.load(QUrl("file:///html/gauge.html"))

        self.browser6 = QWebEngineView()
        #self.browser6.page().setBackgroundColor(Qt.transparent)
        self.browser6.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Stack_bar_percent("html/stack_bar_percent.html")
        self.browser6.load(QUrl("file:///html/stack_bar_percent.html"))

        self.browser7 = QWebEngineView()
        #self.browser7.page().setBackgroundColor(Qt.transparent)
        self.browser7.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Bar3d_punch_card("html/bar3d_punch_card.html")
        self.browser7.load(QUrl("file:///html/bar3d_punch_card.html"))

        self.browser8 = QWebEngineView()
        #self.browser8.page().setBackgroundColor(Qt.transparent)
        self.browser8.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Grid_multi_yaxis("html/grid_multi_yaxis.html")
        self.browser8.load(QUrl("file:///html/grid_multi_yaxis.html"))

        self.browser9 = QWebEngineView()
        #self.browser9.page().setBackgroundColor(Qt.transparent)
        self.browser9.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Line_areastyle_boundary_gap("html/line_areastyle_boundary_gap.html")
        self.browser9.load(QUrl("file:///html/line_areastyle_boundary_gap.html"))

        self.browser10 = QWebEngineView()
        s#elf.browser10.page().setBackgroundColor(Qt.transparent)
        self.browser10.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.render.Pie_position("html/pie_position.html")
        self.browser10.load(QUrl("file:///html/pie_position.html"))

        splitter_width = 2
        splitter1 = QSplitter(Qt.Vertical)
        #splitter1.setStyleSheet("QSplitter::handle { background-color: white }")
        splitter1.setStyleSheet("QSplitter::handle { background-color: rgb(0,51,102) }")
        #splitter1.setStyleSheet("background-color: rgb(255,255,255);")
        splitter1.setHandleWidth(splitter_width)
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.setHandleWidth(splitter_width)
        splitter3 = QSplitter(Qt.Horizontal)
        splitter3.setHandleWidth(splitter_width)
        splitter4 = QSplitter(Qt.Vertical)
        splitter4.setHandleWidth(splitter_width)
        splitter5 = QSplitter(Qt.Horizontal)
        splitter5.setHandleWidth(splitter_width)
        splitter6 = QSplitter(Qt.Vertical)
        splitter6.setHandleWidth(splitter_width)
        splitter7 = QSplitter(Qt.Vertical)
        splitter7.setHandleWidth(splitter_width)
        splitter8 = QSplitter(Qt.Vertical)
        splitter8.setHandleWidth(splitter_width)
        splitter9 = QSplitter(Qt.Vertical)
        splitter9.setHandleWidth(splitter_width)

        splitter1.addWidget(self.browser1)
        splitter1.addWidget(splitter2)
        splitter1.setSizes([1, 13])

        splitter2.addWidget(splitter6)
        splitter2.addWidget(splitter3)
        splitter2.setSizes([1, 3])

        splitter3.addWidget(splitter4)
        splitter3.addWidget(splitter8)
        splitter3.setSizes([2, 1])

        splitter4.addWidget(splitter5)
        splitter4.addWidget(self.browser2)
        splitter4.setSizes([1, 3])

        splitter5.addWidget(self.browser3)
        splitter5.addWidget(self.browser4)

        splitter6.addWidget(self.browser5)
        splitter6.addWidget(splitter7)
        splitter6.setSizes([1, 2])

        splitter7.addWidget(self.browser6)
        splitter7.addWidget(self.browser7)

        splitter8.addWidget(self.browser8)
        splitter8.addWidget(splitter9)
        splitter8.setSizes([1, 2])

        splitter9.addWidget(self.browser9)
        splitter9.addWidget(self.browser10)

        main_box.addWidget(splitter1)
        self.setLayout(main_box)
        self.setGeometry(0, 0, 2000, 1000)
        self.setWindowTitle('大屏展示')
        self.show()

    def resizeEvent(self, event):
        print("resizeEvent")
        self.setBackground()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()