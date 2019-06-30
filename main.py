from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from ksztalty import Ksztalty, Ksztalt
# from PyQt5.QtWidgets import QHBoxLayout2
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap, QIcon, QImage
from PyQt5.QtCore import QPoint, QRect, QSize
from urllib import *
from urllib.request import urlopen

flagamiejsca = 0


class menedzer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
        
        if flagamiejsca == 0:


            self.gorna_belka = Ksztalt(self, Ksztalty.Rect)
            self.gorna_belka.ustawSize(x=-1, y=-1, xsize=1205, ysize=125)
            self.gorna_belka.ustawkolorO(255,255,255)
            self.gorna_belka.ustawgradient(1200,100,1200,125,0,126,67,255,255,255)


            self.dolna_belka = Ksztalt(self,Ksztalty.Rect)
            self.dolna_belka.ustawSize(x=-1, y=551, xsize=1202, ysize=125)
            self.dolna_belka.ustawgradient(1200,575,1200,550,0,126,67,255,255,255)
            self.dolna_belka.ustawkolorO(255,255,255)

            
            label = QLabel(self)
            url = "http://stapox.cal24.pl/img/logo_maszyna.gif"  
            data = urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap2 = pixmap.scaled(251, 70)
            label.setPixmap(pixmap2)
            label.move(20,15)


            napis = QLabel(self)
            napis.setText("Menedżer nieoficjalnych dodatków")
            napis.setStyleSheet("font: 30pt Times New Roman; color: white; font-weight: 700")
            napis.move(400, 25)

            napis2 = QLabel(self)
            napis2.setText("Copyright © 2019 stapox ")
            napis2.setStyleSheet("font: 30pt Times New Roman; color: white")
            napis2.move(400, 600)


            zdjecie = QLabel(self)
            url2 = "http://stapox.cal24.pl/img/img_tytulowa.jpg"
            data =  urlopen(url2).read()
            pixmap3 = QPixmap()
            pixmap3.loadFromData(data)
            #  pixmap4 = pixmap3.scaled(755, 425)
            zdjecie.setPixmap(pixmap3)
            zdjecie.move(0,125)

            dodajBtn = QPushButton("&Instaluj dodatki", self)
            dodajBtn.setStyleSheet("width: 200px; height: 75px")
            dodajBtn.move(900, 145)

            dodajBtn2 = QPushButton("O &projekcie", self)
            dodajBtn2.setStyleSheet("width: 200px; height: 75px")
            dodajBtn2.move(900, 245)

            dodajBtn3 = QPushButton("O &zespole", self)
            dodajBtn3.setStyleSheet("width: 200px; height: 75px")
            dodajBtn3.move(900, 345)

            dodajBtn4 = QPushButton("&Kontakt", self)
            dodajBtn4.setStyleSheet("width: 200px; height: 75px")
            dodajBtn4.move(900, 445)


           
            dodajBtn.clicked.connect(self.dzialanie)
            dodajBtn2.clicked.connect(self.dzialanie)
            dodajBtn3.clicked.connect(self.dzialanie)
            dodajBtn4.clicked.connect(self.dzialanie)

           
        self.resize(1200, 675)
        self.setWindowTitle("Menedżer nieoficjalnych dodatków")
        self.show()


    def dzialanie(self):

        nadawca = self.sender()

        

        if nadawca.text() == "&Instaluj dodatki":
            QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = menedzer()
    sys.exit(app.exec_())
