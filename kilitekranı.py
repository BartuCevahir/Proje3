import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Kütüphane Kayıt Uygulaması")
window.setFixedWidth(500)
window.setFixedHeight(300)

layout = QVBoxLayout() # layout = QHBoxLayout()

layout.addWidget(QLabel("Ad:"))
layout.addWidget(QLineEdit())
layout.addWidget(QLabel("Şifre:"))
layout.addWidget(QLineEdit())
layout.addWidget(QCheckBox("Beni hatırla"))
layout.addWidget(QPushButton("Giriş yap"))
layout.addWidget(QLabel("..."))

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)
window.show()
app.exec()
