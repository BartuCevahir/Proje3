from PyQt6.QtWidgets import *


class ana_ekran(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Kütüphane Kayıt Programı")


        central_widget = QWidget()
        layout = QVBoxLayout()


        dugme1 = QPushButton("YENİ KAYIT")
        dugme1.clicked.connect(self.yenikayit)
        layout.addWidget(dugme1)


        dugme2 = QPushButton("KAYITLAR")
        dugme2.clicked.connect(self.kayıtlistele)
        layout.addWidget(dugme2)


        dugme2 = QPushButton("KAYIT SİL")
        layout.addWidget(dugme2)


        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def yenikayit(x):
        import kayıtekleme
        x.kayit_ekleme_ekrani = kayıtekleme.kayit_ekrani()
        x.kayit_ekleme_ekrani.show()
       
    def kayıtlistele(x):
        import kayit_listeleme
        x.kayit_ekleme_ekrani = kayit_listeleme.()
        x.kayit_ekleme_ekrani.show()
       

app = QApplication([])
window = ana_ekran()
window.show()
app.exec()
