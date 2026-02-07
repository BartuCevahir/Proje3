from PyQt6.QtWidgets import *

class AnaMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Menü")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        # Butonlar
        dugme1 = QPushButton("Yeni Kayıt")
        dugme2 = QPushButton("Kayıtlar")
        dugme3 = QPushButton("Kayıt Sil")

        layout.addWidget(dugme1)
        layout.addWidget(dugme2)
        layout.addWidget(dugme3)

        # Buton işlevleri
        dugme1.clicked.connect(self.kayit_ekle_ac)
        dugme2.clicked.connect(self.kayit_goster_ac)
        dugme3.clicked.connect(self.kayit_silme_ac)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def kayit_ekle_ac(self):
        from kayıtekleme import kayit_ekrani
        self.kayit_ekrani = kayit_ekrani()
        self.kayit_ekrani.show()

    def kayit_goster_ac(self):
        from verilerilisteleme import kayit_listele
        self.kayit_listeleme_ekrani = kayit_listele()
        self.kayit_listeleme_ekrani.show()

    def kayit_silme_ac(self):
        from kayitsilme import KayitSilmeEkrani
        self.kayit_silme_ekrani = KayitSilmeEkrani()
        self.kayit_silme_ekrani.show()