from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QScrollArea, QFormLayout, QGroupBox,QFrame
from ksztalty import Ksztalty, Ksztalt
# from PyQt5.QtWidgets import QHBoxLayout2
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap, QIcon, QImage
from PyQt5.QtCore import QPoint, QRect, QSize
from urllib import *
from urllib.request import urlopen
import requests
from funkcje import sprawdzwersje
import os
import array as arr

sciezka_roota = os.getcwd()
globalURL= "http://stapox.cal24.pl/"
zmiennaCopyright = "Copyright © 2019 stapox "
listazezwolen = [0,0,0,0,0,0,0,0,0,0,0]
tablicazezwolen = arr.array('i', listazezwolen)

#tablicazezwolen = []
class menedzer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()
    global layoutOM1, layoutV
    layoutOM1 = QVBoxLayout()
    layoutV = QVBoxLayout()
    def interfejs(self):
        
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
        dodajBtn.setStyleSheet("width: 200px; height: 75px;")
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
        layout3.setSpacing(32)
        layout2.addLayout(layout3)
        
        layoutV.addLayout(layout2)
        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 30pt Times New Roman; color: white; text-align: center; width: 1200px")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

       
        napis3 = QLabel()
        napis3.setText("O Projekcie")
        napis2.setStyleSheet("font: 30pt Times New Roman; color: white; text-align: center; width: 1200px")
        layoutOM1.addWidget(napis3)

       
            

        
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
       
        if nadawca.text() == "O &projekcie":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.funkcja1()
        if nadawca.text() == "O &zespole":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.funkcja2()
        if nadawca.text() == "&Home":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.interfejs()
        if nadawca.text() == "&Kontakt":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.funkcja3()
        if nadawca.text() == "&Instaluj dodatki":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(-1)
        if nadawca.text() == "Lokomotywy &elektryczne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(1)
        if nadawca.text() == "Lokomotywy &spalinowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(2)
        if nadawca.text() == "Lokomotywy &parowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(3)
        if nadawca.text() == "Wagony &osobowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(4)
        if nadawca.text() == "Wagony &towarowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(5)
        if nadawca.text() == "P&ojazdy specjalne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(6)
        if nadawca.text() == "S&cenerie":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(7)
        if nadawca.text() == "Elektryczne &zespoły trakcyjne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(8)
        if nadawca.text() == "Spalino&we zespoły trakcyjne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(9)
        if nadawca.text() == "Wagony &akumulatorowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(10)
        if nadawca.text() == "Wagony &motorowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(11)
        if nadawca.text() == "Pokaż &wszystkie":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(-1)
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def funkcja1(self):
        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;")
        layout.addWidget(dodajBtn)
        dodajBtn.clicked.connect(self.dzialanie)

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
        url2 = globalURL+"img/skrin-o-projekcie.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        zdjecie.setPixmap(pixmap3)
        zdjecie.move(0,125)
        
        layout3 = QHBoxLayout()
        layout3.setDirection(2)

        napis5 = QLabel(self)
        napis5.setText("O Projekcie")
        napis5.setStyleSheet("font: 18pt Times New Roman; color: white; font-weight: 700")
        layout3.addWidget(napis5)

        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        data = data.replace('\n', ' ')
        #i = 0
        flagaoprojekcie = False
        text = data.split(' ')
        textpl = ""
        for s in text:
            if flagaoprojekcie:
                if s == "[OZ]":
                    flagaoprojekcie = False
                    break
                textpl = textpl+' '+s
            if s == "[OP]":
                flagaoprojekcie = True
                #print("rozpoczalem_wydzielac")
        
       #print(textpl[5:len(textpl)-2])

        napisPL = QLabel(self)
        napisPL.setText(textpl[5:len(textpl)-1])
        napisPL.setStyleSheet("font: 16pt Times New Roman; color: white")
        napisPL.setWordWrap(True)
        layout3.addWidget(napisPL)
        layout2.addWidget(zdjecie)
        layout2.addLayout(layout3)
        layoutV.addLayout(layout2)

        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

    def pokazszczegoly(self, iddodatku):
        self.clearLayout(layoutV)
        id = iddodatku
        print(id)

    def pokazwybrane(self, klucz):
        mojawersja = sprawdzwersje(sciezka_roota, globalURL)
        print(mojawersja)
        #http://stapox.cal24.pl/files/menedzer_dodatki.php

        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;")
        layout.addWidget(dodajBtn)
        dodajBtn.clicked.connect(self.dzialanie)

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

        
        layoutkolejny = QHBoxLayout()
        
        response = requests.get(globalURL+"files/menedzer_dodatki.php")
        data = response.text
        
        data = data.replace("<br>", "")
        data = data.replace("<br/>", "")
        data = data.replace("<br />", "")
        data = data.split(';')
        #print(data[0])
        formLayout = QFormLayout()
        groupbox = QGroupBox()
        
        

        for i in data:
            if i == "":
                break
            frame = QFrame()
            pomocnicza = str(i).split('$')
            aktualneid = pomocnicza[0].replace(" ", "")
            layoutdodatek = QHBoxLayout()
            layoutprzycisk = QHBoxLayout()
            layoutopisy = QHBoxLayout()
            layoutdodatek.setDirection(2)
            
            tyul = QLabel(pomocnicza[1].replace("<q>", '"').replace("</q>", '"'))
            tyul.setStyleSheet("font: 25px Times New Roman; font-weight: 800")
            layoutdodatek.addWidget(tyul)
            
            #QLabel().setPixmap(QPixmap().loadFromData(urlopen(adres).read()))
            label = QLabel()
            pixmap = QPixmap()
            adres = str(globalURL+pomocnicza[3])
            #print(adres)
            data =  urlopen(adres).read()
            pixmap.loadFromData(data)
            label.setPixmap(pixmap)
            #label.move(20,15)
            layoutopisy.addWidget(label)
            opis = QLabel(pomocnicza[8])
            opis.setWordWrap(True)
            layoutopisy.addWidget(opis)
            
            layoutdodatek.addLayout(layoutopisy)
            wersja = pomocnicza[6]
            wersja = wersja.split(" ")
            layoutprzycisk.addWidget(QLabel(pomocnicza[6]))
            przycisk_sprawdz_wiecej = QPushButton("&Dowiedz się więcej i instaluj!", self)
            przycisk_sprawdz_wiecej.setStyleSheet("height: 25px; background-color: #dc3545; color: white")
            id = int(pomocnicza[0])
            przycisk_sprawdz_wiecej.clicked.connect(lambda: self.pokazszczegoly(id))
            #TODO: do ogarnięcia, żeby id szło poprawne :P
            #przycisk_sprawdz_wiecej.setFocusPolicy()
            layoutprzycisk.addWidget(przycisk_sprawdz_wiecej)
            layoutdodatek.addLayout(layoutprzycisk)
            frame.setLayout(layoutdodatek)
            frame.setStyleSheet("background-color: #999999; border-radius: 8px")
            aktualnyklucz = pomocnicza[2]
            aktualnyklucz = aktualnyklucz.replace(" ", "")
            aktualnyklucz = int(aktualnyklucz)
            if mojawersja != -1 and mojawersja == wersja[1] or mojawersja == -1 and aktualnyklucz == klucz or klucz == -1:

                formLayout.addRow(frame)
                
                tablicazezwolen[aktualnyklucz-1] = tablicazezwolen[aktualnyklucz-1]+1
                #print(tablicazezwolen[0])

            if(aktualneid == 1):
                break

                
            '''
            labelList.append(QLabel("Label"))
            buttonList.append(QPushButton(" Click me"))
            formLayout.addRow(labelList[i], buttonList[i])
            '''
        groupbox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(520)
        scroll.setFixedWidth(800)





        layout3 = QHBoxLayout()
        layout3.setDirection(2)
        scroll_area = QScrollArea()
        scroll_area.setBaseSize(300,400)
        scroll_area.setLayout(layout3)

        dodajBtn = QPushButton("Pokaż &wszystkie", self)
        dodajBtn.setStyleSheet("width: 100px; height: 50px;")
        layout3.addWidget(dodajBtn)
        dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[0] != 0:
            dodajBtn = QPushButton("Lokomotywy &elektryczne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[1] != 0:
            dodajBtn = QPushButton("Lokomotywy &spalinowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[2] !=0:
            dodajBtn = QPushButton("Lokomotywy &parowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[3] !=0:
            dodajBtn = QPushButton("Wagony &osobowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[4] !=0:
            dodajBtn = QPushButton("Wagony &towarowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[5] !=0:
            dodajBtn = QPushButton("P&ojazdy specjalne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[7] !=0:
            dodajBtn = QPushButton("Elektryczne &zespoły trakcyjne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[8] !=0:
            dodajBtn = QPushButton("Spalino&we zespoły trakcyjne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[9] !=0:
            dodajBtn = QPushButton("Wagony &akumulatorowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[10] !=0:
            dodajBtn = QPushButton("Wagony &motorowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[6] !=0:
            dodajBtn = QPushButton("S&cenerie", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)

        


        
        layoutkolejny.addWidget(scroll_area)
        layoutkolejny.addWidget(scroll)
        layoutV.addLayout(layoutkolejny)
      

        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

    def funkcja2(self):
        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;")
        layout.addWidget(dodajBtn)
        dodajBtn.clicked.connect(self.dzialanie)

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
        url2 = globalURL+"img/skrin-o-zespole.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        zdjecie.setPixmap(pixmap3)
        zdjecie.move(0,125)
        
        layout3 = QHBoxLayout()
        layout3.setDirection(2)

        napis5 = QLabel(self)
        napis5.setText("O Zespole")
        napis5.setStyleSheet("font: 18pt Times New Roman; color: white; font-weight: 700")
        layout3.addWidget(napis5)

        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        data = data.replace('\n', ' ')
        i = 0
        flagaoprojekcie = False
        text = data.split(' ')
        textpl = ""
        for s in text:
            if flagaoprojekcie:
                if s == "[KONT]":
                    flagaoprojekcie = False
                    break
                textpl = textpl+' '+s
            if s == "[OZ]":
                flagaoprojekcie = True
                #print("rozpoczalem_wydzielac")
        
        #print(textpl[5:len(textpl)-2])

        napisPL = QLabel(self)
        napisPL.setText(textpl[5:len(textpl)-1])
        napisPL.setStyleSheet("font: 16pt Times New Roman; color: white")
        napisPL.setWordWrap(True)
        layout3.addWidget(napisPL)
        layout2.addLayout(layout3)
        layout2.addWidget(zdjecie)
        
        layoutV.addLayout(layout2)

        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

    def funkcja3(self):
        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;")
        layout.addWidget(dodajBtn)
        dodajBtn.clicked.connect(self.dzialanie)

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
        url2 = globalURL+"img/scr-kontakt.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        zdjecie.setPixmap(pixmap3)
        zdjecie.move(0,125)
        
        layout3 = QHBoxLayout()
        layout3.setDirection(2)

        napis5 = QLabel(self)
        napis5.setText("Kontakt")
        napis5.setStyleSheet("font: 20pt Times New Roman; color: white; font-weight: 700")
        layout3.addWidget(napis5)

        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        data = data.replace('\n', ' ')
        i = 0
        flagaoprojekcie = False
        text = data.split(' ')
        textpl = ""
        for s in text:
            if flagaoprojekcie:
                if s == "[END]":
                    flagaoprojekcie = False
                    break
                textpl = textpl+' '+s
            if s == "[KONT]":
                flagaoprojekcie = True
                #print("rozpoczalem_wydzielac")
        
        #print(textpl[5:len(textpl)-2])

        napisPL = QLabel(self)
        setetx = textpl[5:len(textpl)-1]
        setetx = setetx.split('"')
        napisPL.setText(setetx[0])
        napisPL.setStyleSheet("font: 16pt Times New Roman; color: white")
        napisPL.setWordWrap(True)

        napisPL2 = QLabel(self)
        napisPL2.setText("Mail do uber-admina stapoxa: "+setetx[2])
        napisPL2.setStyleSheet("font: 16pt Times New Roman; color: white")

        layout3.addWidget(napisPL)
        layout3.addWidget(napisPL2)
        layout2.addLayout(layout3)
        layout2.addWidget(zdjecie)
        
        layoutV.addLayout(layout2)

        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = menedzer()
sys.exit(app.exec_())