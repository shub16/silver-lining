#!/usr/bin/python

import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)
window = QWidget()
text = QLineEdit()
button = QPushButton("Hello")

layout = QHBoxLayout(window)
layout.addWidget(text)
layout.addWidget(button)
window.resize(250, 100)
window.setWindowTitle("Hello!")
window.show()
app.exec_()
