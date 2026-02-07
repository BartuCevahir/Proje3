from PyQt6.QtWidgets import *
import mysql.connector

class KayitSilmeEkrani(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kayıt Sil")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.telefon_input = QLineEdit()
        self.telefon_input.setPlaceholderText("Silinecek telefon numarası")
        layout.addWidget(self.telefon_input)

        sil_btn = QPushButton("Sil")
        sil_btn.clicked.connect(self.kayit_sil)
        layout.addWidget(sil_btn)

        self.setLayout(layout)

    def kayit_sil(self):
        telefon = self.telefon_input.text()

        if not telefon:
            QMessageBox.warning(self, "Hata", "Telefon numarası boş olamaz!")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pythondersleri"
            )

            cursor = db.cursor()
            sql = "DELETE FROM ogrenciler WHERE telefon = %s"
            cursor.execute(sql, (telefon,))
            db.commit()

            if cursor.rowcount > 0:
                QMessageBox.information(self, "Başarılı", "Kayıt silindi.")
                self.telefon_input.clear()
            else:
                QMessageBox.warning(self, "Bulunamadı", "Bu numaraya ait kayıt yok.")

            db.close()

        except Exception as e:
            QMessageBox.critical(self, "Veritabanı Hatası", str(e))
