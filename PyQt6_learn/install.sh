pyinstaller -D 02.py --add-data '/Users/zhiyuzhang/miniconda3/lib/python3.10/site-packages/PyQt6/*.so:PyQt6/' --hidden-import PyQt6.QtCore --hidden-import PyQt6.QtGui --hidden-import PyQt6.QtWidgets


### question 1
## pyinstaller vision too high
## conda install pyinstaller-5.6.2
## pyinstaller -D 02.py 这样都不用导入 PyQt6

