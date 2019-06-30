from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout
from ksztalty import Ksztalty, Ksztalt
# from PyQt5.QtWidgets import QHBoxLayout2
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap, QIcon, QImage
from PyQt5.QtCore import QPoint, QRect, QSize
from urllib import *
from urllib.request import urlopen

globalURL= "http://stapox.cal24.pl/"


class menedzer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
        

       

        layoutV = QVBoxLayout()
        layoutV.setDirection(2)

       
        layout = QHBoxLayout()
        
        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

       
        napis = QLabel(self)
        napis.setText("Menedżer nieoficjalnych dodatków")
        napis.setStyleSheet("font: 30pt Times New Roman; color: white; font-weight: 700")
        napis.move(400, 25)


       



        layout.addWidget(napis)
        layoutV.addLayout(layout)

        layout2 = QHBoxLayout()

        zdjecie = QLabel(self)
        url2 = globalURL+"img/img_tytulowa.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        zdjecie.setPixmap(pixmap3)
        zdjecie.move(0,125)
        

        layout2.addWidget(zdjecie)
        layout3 = QHBoxLayout()
        layout3.setDirection(2)
        dodajBtn = QPushButton("&Instaluj dodatki", self)
        dodajBtn.setStyleSheet("width: 200px; height: 75px")
        layout3.addWidget(dodajBtn)
        dodajBtn2 = QPushButton("O &projekcie", self)
        dodajBtn2.setStyleSheet("width: 200px; height: 75px")
        layout3.addWidget(dodajBtn2)
        dodajBtn3 = QPushButton("O &zespole", self)
        dodajBtn3.setStyleSheet("width: 200px; height: 75px")
        layout3.addWidget(dodajBtn3)
        dodajBtn4 = QPushButton("&Kontakt", self)
        dodajBtn4.setStyleSheet("width: 200px; height: 75px")
        layout3.addWidget(dodajBtn4)
        layout2.addLayout(layout3)
        layoutV.addLayout(layout2)
        napis2 = QLabel(self)
        napis2.setText("Copyright © 2019 stapox ")
        napis2.setStyleSheet("font: 30pt Times New Roman; color: white; text-align: center")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

       

        
        dodajBtn.clicked.connect(self.dzialanie)
        dodajBtn2.clicked.connect(self.dzialanie)
        dodajBtn3.clicked.connect(self.dzialanie)
        dodajBtn4.clicked.connect(self.dzialanie)

        layoutX = QVBoxLayout()
        layoutX.setDirection(2)

        self.setWindowTitle("Menedżer nieoficjalnych dodatków")
        '''
        url2 = globalURL+"img/tlo.jpg"
        zdjecie = QLabel(self)
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        zdjecie.setPixmap(pixmap3)
       # layoutX.addWidget(zdjecie)
       #layoutV.addChildLayout(layoutX)
       '''
        self.resize(1200, 675)
        self.setFixedSize(1200,675)
       
        self.setStyleSheet("background-color: #007e43")
        self.setLayout(layoutV)

        #self.setLayout(layoutV)
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