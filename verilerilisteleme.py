from PyQt6.QtWidgets import *
import mysql.connector
vt = mysql.connector.connect(host="localhost",user="root",password="1234",database="pythondersleri")


class kayit_listele(QMainWindow):


    def tabloya_yerlestir(self, veriler):
        """veri listesini tabloya ekler"""
        self.kayit_tablosu.setRowCount(len(veriler))  # Satır sayısını belirle


        for satir, eklenecek_satir in enumerate(veriler):
            for sutun, bilgi in enumerate(eklenecek_satir):
                self.kayit_tablosu.setItem(satir, sutun, QTableWidgetItem(str(bilgi)))


       
    def tablo_verisi_al(x):
        secilen_vt = vt.cursor()
        secilen_vt.execute(f"select * from pythondersleri.ogrenciler")
        kayitlar = secilen_vt.fetchall()
        print(secilen_vt.rowcount, "kayıt listeleniyor..\n\n",kayitlar)
        secilen_vt.close()
        return kayitlar


    # def __init__(x, parent = ..., flags = ...):
    def __init__(x):
        # super().__init__(parent, flags)
        super().__init__()


        # x.tablo_verisi_al()    
        x.setWindowTitle("Kayıt Listesi")
        x.setGeometry(300, 300, 500, 400)


        # Layout oluştur
        ana_layout = QVBoxLayout()


        # QTableWidget oluştur (4 sütunlu)
        x.kayit_tablosu = QTableWidget()
        x.kayit_tablosu.setColumnCount(2)
        x.kayit_tablosu.setHorizontalHeaderLabels(["ADI SOYADI", "TELEFON NO"])
        # x.kayit_tablosu.cellClicked.connect(x.satir_tiklandi)


   
        tablo_verisi = x.tablo_verisi_al()
        x.tabloya_yerlestir(tablo_verisi)




        
        ana_layout.addWidget(x.kayit_tablosu) # Tabloyu layout'a ekle
        x.setLayout(ana_layout)




        ana_layout.addWidget(QLabel("..."))


        ana_widget = QWidget()
        ana_widget.setLayout(ana_layout)


        x.setCentralWidget(ana_widget)


if __name__ == "__main__":
    app = QApplication([])
    pencere = kayit_listele()
    pencere.show()
    app.exec()
