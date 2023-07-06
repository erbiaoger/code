import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

# 创建窗口和布局
window = QWidget()
layout = QVBoxLayout(window)

# 创建按钮
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
button3 = QPushButton("Button 3")

# 将按钮添加到布局中，并设置位置
layout.addWidget(button1, 0)  # 添加到布局的第一个位置
layout.addWidget(button2, 2)  # 添加到布局的第三个位置
layout.addWidget(button3, Qt.AlignmentFlag.AlignRight)  # 添加到布局的右边界

# 显示窗口
window.show()

sys.exit(app.exec())
