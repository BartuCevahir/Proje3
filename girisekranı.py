import sys
from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kütüphane Kayıt")
        self.setFixedSize(500, 300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Kullanıcı Adı:"))
        self.ad_input = QLineEdit()
        layout.addWidget(self.ad_input)

        layout.addWidget(QLabel("Şifre:"))
        self.sifre_input = QLineEdit()
        self.sifre_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.sifre_input)

        self.hatirla = QCheckBox("Beni hatırla")
        layout.addWidget(self.hatirla)

        giris_btn = QPushButton("Giriş yap")
        giris_btn.clicked.connect(self.giris_yap)
        layout.addWidget(giris_btn)

        self.durum_label = QLabel("")
        layout.addWidget(self.durum_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def giris_yap(self):
        ad = self.ad_input.text().strip()
        sifre = self.sifre_input.text().strip()

        if not ad or not sifre:
            self.durum_label.setText("Alanlar boş bırakılamaz!")
            return

        if ad == "admin" and sifre == "1234":
            self.ana_menuyu_ac()
        else:
            self.durum_label.setText("Hatalı kullanıcı adı veya şifre!")

    def ana_menuyu_ac(self):
        print("Ana Menü açılıyor...")  # Test için
        from anamenu import AnaMenu
        self.ana_menu = AnaMenu()
        self.ana_menu.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GirisEkrani()
    window.show()
    app.exec()