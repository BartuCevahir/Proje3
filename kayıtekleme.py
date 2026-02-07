from PyQt6.QtWidgets import *
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="pythondersleri")


class kayit_ekrani(QMainWindow):
       
    def kaydet(x):
        ad = x.ad_input.text()
        nu = x.numara_input.text()
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO ogrenciler (ad, telefon) VALUES ('{ad}', '{nu}')")
        mydb.commit()
        print(mycursor.rowcount, "kayıt eklendi.")


    # def __init__(x, parent = ..., flags = ...):
    def __init__(x):
        # super().__init__(parent, flags)
        super().__init__()
           
        x.setWindowTitle("Kütüphane Kayıt Uygulaması")


        layout = QVBoxLayout() # layout = QHBoxLayout()


        layout.addWidget(QLabel("Kullanıcı Adı Soyadı:"))
        x.ad_input = QLineEdit()
        layout.addWidget(x.ad_input)
        layout.addWidget(QLabel("Telefon Numarası:"))
        x.numara_input = QLineEdit()
        layout.addWidget(x.numara_input)
        x.dugme_kaydet = QPushButton("Giriş Yap")
        layout.addWidget(x.dugme_kaydet)
        x.dugme_kaydet.clicked.connect(x.kaydet)
        layout.addWidget(QLabel("Bilgilerinizi eksiksiz giriniz!"))


        widget = QWidget() ; widget.setLayout(layout)


        x.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([]);
    pencere = kayit_ekrani()
    pencere.show()
    app.exec()
