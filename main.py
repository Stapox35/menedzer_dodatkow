#FOR LINUX
#!/usr/bin/env python3
import os
#FOR WINDOWS
import sys
if sys.platform[:3] == "win":
    if hasattr(sys, 'frozen'):
        os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QScrollArea, QFormLayout, QGroupBox,QFrame,QProgressBar, QFileDialog
from ksztalty import Ksztalty, Ksztalt
# from PyQt5.QtWidgets import QHBoxLayout2
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap, QIcon, QImage
from PyQt5.QtCore import QPoint, QRect, QSize
from urllib import *
from urllib.request import urlopen
import requests
from funkcje import sprawdzwersje, SprawdzCzyZainstalowany,PodajDateInstalacji, PodajSciezkeSymulatora
import array as arr
from pyunpack import Archive
import shutil
import codecs
import datetime
import os as _os
import subprocess


sciezka_roota = ""
sciezka_roota_programu = os.getcwd()
globalURL= "http://stapox.cal24.pl/"
zmiennaCopyright = "Copyright © 2019 stapox"
listazezwolen = [0,0,0,0,0,0,0,0,0,0,0]
tablicazezwolen = arr.array('i', listazezwolen)
versionMenedzer = "0.3L"
sciezka_roota = ""
log = open(sciezka_roota_programu+"/log_men.txt", "w+")
x = datetime.datetime.now()
log.write(str(x))
log.close()

class menedzer(QWidget): 
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self.interfejs()
    
    global layoutOM1, layoutV
    layoutOM1 = QVBoxLayout()
    layoutV = QVBoxLayout()

    def config(self):
        log = open(sciezka_roota_programu+"/log_men.txt", "a")
        log.write(sciezka_roota_programu)
        log.write("\r\n rozpoczynamy config\r\n")
        flagapierwszegouruchamiania = False
        if not os.path.isfile(sciezka_roota_programu+"/.config_men.ini"):
            flagapierwszegouruchamiania = True
        if flagapierwszegouruchamiania:
            name = QFileDialog.getExistingDirectory(self, "Podaj ścieżkę do symulatora!")
            print(str(name))
            if str(name) == "":
                self.destroy()
                if sys.platform[:3] == "win":
                    sys.exit(0)
                if sys.platform[:5] == "linux":
                    exit()
            sciezka_roota = str(name)
            ini = open(sciezka_roota_programu+"/.config_men.ini", "w+")
            x = datetime.datetime.now()
            ini.write("-p "+str(sciezka_roota)+";\n")
            ini.write("-v "+str(versionMenedzer)+"$"+str(x)+";\n")
            ini.write("[ADDONS]\n")
            response = requests.get(globalURL+"files/menedzer_dodatki.php")
            data = response.text
            data = data.replace("<br>", "")
            data = data.replace("<br/>", "")
            data = data.replace("<br />", "")
            data = data.split(';')
            for i in data:
                pomocnicza = i.split("$")
                aktualneid = int(pomocnicza[0])
                adresRI = pomocnicza[10]
                flagaweryfikacji = False
                response = requests.get(adresRI)
                dataRI = response.text
                flagategoid=True
                for o in dataRI.split('\n'):
                    o=o.replace("\r", "").replace(" ", "").replace("\t", "")
                    if flagaweryfikacji:
                        if o =="":
                            flagaweryfikacji = False
                        path = o.split("=")[0]
                        if path != "":
                            path = path.replace('\\', "/")
                            #print(sciezka_roota+"/"+path)
                            if not os.path.isfile(sciezka_roota+"/"+path):
                                flagategoid = False  
                    if o[:8] == "[VERIFY]":
                        flagaweryfikacji = True
                if flagategoid == True:
                    ini.write("-a "+str(aktualneid)+"$"+str(1)+"$"+str(x)+";\n")
                if aktualneid == 1:
                    break
            ini.close()
        sciezka_roota = str(PodajSciezkeSymulatora())
        flagamaszyny = True
        print(sciezka_roota)
        if not os.path.isdir(sciezka_roota+"/dynamic"):
            flagamaszyny = False
        if not os.path.isdir(sciezka_roota+"/textures"):
            flagamaszyny = False
        if not os.path.isdir(sciezka_roota+"/scenery"):
            flagamaszyny = False
        
        if flagamaszyny == False:
            QMessageBox.warning(self, "Błąd", "Skonfiguruj jeszcze raz program!", QMessageBox.Ok)
            os.remove(sciezka_roota_programu+"/.config_men.ini")
            #print(name)
           
            self.config()
            '''exit
            self.destroy()
            exit()
            '''
        #print(sciezka_roota_programu)
        print(sciezka_roota)
        log.close()


    def NewConfig(self):
        os.remove(sciezka_roota_programu+"/.config_men.ini")
        self.config()

    def interfejs(self):
        sciezka_roota_programu = os.getcwd()
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
        dodajBtn.setStyleSheet("width: 200px; height: 75px; background-color: #00b15e")
        layout3.addWidget(dodajBtn)
        dodajBtn2 = QPushButton("O &projekcie", self)
        dodajBtn2.setStyleSheet("width: 200px; height: 75px; background-color: #00b15e")
        layout3.addWidget(dodajBtn2)
        dodajBtn3 = QPushButton("O &zespole", self)
        dodajBtn3.setStyleSheet("width: 200px; height: 75px; background-color: #00b15e")
        layout3.addWidget(dodajBtn3)
        dodajBtn4 = QPushButton("&Kontakt", self)
        dodajBtn4.setStyleSheet("width: 200px; height: 75px; background-color: #00b15e")
        layout3.addWidget(dodajBtn4)
        layout3.setSpacing(32)
        layout2.addLayout(layout3)
        
        layoutV.addLayout(layout2)
        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 30pt Times New Roman; color: white; text-align: center; width: 1200px")

        
        
        layoutpomocniczy = QHBoxLayout()

        configBtn = QPushButton("&Konfiguruj", self)
        configBtn.setStyleSheet("width: 50px; height: 75px; background-color: #00b15e")
        layoutpomocniczy.addWidget(configBtn)
        configBtn.clicked.connect(self.dzialanie)
        layoutpomocniczy.addWidget(napis2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)


        



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
        self.setWindowIcon(QIcon(sciezka_roota_programu+'/icon.ico'))
        print(sciezka_roota_programu+'/icon.ico')
        self.setStyleSheet("background-color: #007e43")
        self.setLayout(layoutV)

        #self.setLayout(layoutV)
        self.show()
        self.config()
    
   


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
        if nadawca.text() == "&Wróć":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.pokazwybrane(-1)
        if nadawca.text() == "&Konfiguruj":
            self.NewConfig()
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
        dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
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
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)
    
    def funckjainstalacji(self,adres, progress, Button,id,flaga, multiplier=1):
        log = open(sciezka_roota_programu+"/log_men.txt", "a", encoding="utf-8")
        sciezka_roota = PodajSciezkeSymulatora()
        response = requests.get(adres)
        data = response.text
        #progress.setValue(1)
        progress.setValue(progress.value()+14.28*1*multiplier) #14%
        download = False
        linkacz=""
        adrestext = ""
        seria="x"
        seriaflaga = False
        textures = False
        WpisTextures=""
        WspTextures="\n"
        for i in data.split("\n"):
            i = i.replace("\t", "")
            i = i.replace("\r", "")
            i = i.replace(" ", "")
            if download:
                i = i.split("=")
                linkacz = i[0]
                download = False
            if textures:
                i = i.split("=")
                adrestext = i[0]
                seria = i[1]
                textures = False
            if seriaflaga:
                if i =="":
                    seriaflaga = False
                if i[:1] == "!":
                    WspTextures = i
                else:
                    i = str(i).replace("\n", "").replace(" ","").replace("\r\n", "").replace("\t", "").replace("\r", "")
                    WpisTextures = WpisTextures+str(i)+"\r\n"
            if i[:10] == "[DOWNLOAD]":
                download = True
            if i[:14] == "[TEXTURES.TXT]":
                textures = True
            if i[:len(seria)+2] == "["+seria+"]":
                seriaflaga = True
        print(linkacz)
        print(adrestext)
        print(seria)
        print(WspTextures)
        print(WpisTextures)
        log.write(str(linkacz+"\r\n"))
        log.write(str(adrestext+"\r\n"))
        log.write(str(seria+"\r\n"))
        log.write(str(WspTextures+"\r\n"))
        progress.setValue(progress.value()+14.28*1*multiplier)
        
        filename = os.path.basename(linkacz)

        response = requests.get(linkacz, stream=True)
        tempSciezka = sciezka_roota+"/temp/"
        if not os.path.exists(tempSciezka):
            os.makedirs(tempSciezka)
        progress.setValue(progress.value()+14.28*1*multiplier)
        if response.status_code == 200:
            with open(tempSciezka+filename, 'wb') as out:
                out.write(response.content)
                adresArciwum = tempSciezka+filename
                progress.setValue(progress.value()+14.28*1*multiplier)
        else:
            print('Request failed: %d' % response.status_code)
            QMessageBox.warning(self, "Błąd", "Pobieranie dodatku nie powiodło się! Proszę spróbować jeszcze raz", QMessageBox.Ok)
            self.pokazszczegoly(id)
        if sys.platform[:3] == "win":
            if os.path.isfile("C:/Program Files (x86)/7-Zip/7z.exe"):
                log.write("\r\n 7zip x86 ")
                file7z = '"C:/Program Files (x86)/7-Zip/7z.exe" x "'+adresArciwum +'" -o"'+sciezka_roota+'" -y'
                subprocess.call(file7z)
            elif os.path.isfile("C:/Program Files/7-Zip/7z.exe"):
                log.write("\r\n 7zip Programfiles ")
                file7z='"C:/Program Files/7-Zip/7z.exe" x "'+adresArciwum +'" -o"'+sciezka_roota+'"  -y'
                subprocess.call(file7z)
            else:
                QMessageBox.warning(self, "Błąd", "Nie znaleziono 7-zip! Proszę zainstalować!!!", QMessageBox.Ok)
                self.pokazszczegoly(id)
                log.write("\r\n 7zip Brak")
        if sys.platform[:5]:
            Archive(adresArciwum).extractall(sciezka_roota)
        progress.setValue(progress.value()+14.28*1*multiplier)
        textures = open(sciezka_roota+"/"+adrestext+"/textures.txt", "a", encoding="utf-8")
        textures.write("\r\n"+WpisTextures)
        textures.close()

        progress.setValue(progress.value()+14.28*1*multiplier)
        shutil.rmtree(tempSciezka, ignore_errors=True)
        log.write("57\r\n")
        #os.system("del "+tempSciezka)
        log.write("usuniete\r\n")
        
        progress.setValue(multiplier*100)
        print(round(progress.value()/(multiplier*100), 0))
        Button.setDisabled(True)
        ini = open(sciezka_roota_programu+"/.config_men.ini", "a")
        x = datetime.datetime.now()
        ini.write("-a "+str(id)+"$"+str(1)+"$"+str(x)+";\n")
        log.write("-a "+str(id)+"$"+str(1)+"$"+str(x)+";\n")
        ini.close()
        response = requests.get(globalURL+"files/menedzer_dodaj.php?id="+str(id))
        data = response.text

        log.write("\r\nZainstalowano\r\n")
        log.write(str(id))
        log.close()
        if flaga:
            QMessageBox.information(self, "Zainstalowano", "Wybrany dodatek został zainstalowany!", QMessageBox.Ok)
            self.pokazszczegoly(id)
        if not flaga:
            return progress.value()
    def instaluj(self, id, adres):
        sciezka_roota = PodajSciezkeSymulatora()
        progress = QProgressBar()
        print(adres)
        adres = adres
        self.clearLayout(layoutV)
        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Wróć", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
        layout.addWidget(dodajBtn)
        dodajBtn.clicked.connect(lambda: self.pokazszczegoly(id))
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
        layoutinstalacji = QHBoxLayout()
        layoutinstalacji.setDirection(2)
        dodajBtn = QPushButton("&Instaluj!", self)
        dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #00b15e")
        layoutinstalacji.addWidget(dodajBtn)
        dodajBtn.clicked.connect(lambda: self.funckjainstalacji(adres,progress,dodajBtn,id,True))
        label = QLabel("Trwa instalowanie, proszę czekać ... ")
        label.setStyleSheet("font: 40px Times New Roman; color: white")
        layoutinstalacji.addWidget(label)
        
        progress.setGeometry(10,10,500,50)
        layoutinstalacji.addWidget(progress)
        layoutV.addLayout(layoutinstalacji)

        #progress.setValue(50)
        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

        #self.funckjainstalacji(adres, progress)

    def pokazszczegoly(self, id):
        sciezka_roota = PodajSciezkeSymulatora()
        if id == 0:
            id = int(self.sender().text().replace("&Dowiedz się więcej i instaluj! (", "").replace(")", ""))
        else:
            id=id
        print(id)
        self.clearLayout(layoutV)

        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Wróć", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
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
            if int(aktualneid) == id:

                layoutdodatek = QHBoxLayout()
                layoutprzycisk = QHBoxLayout()
                layoutopisy = QHBoxLayout()
                layouttytul = QHBoxLayout()

                layoutdodatek.setDirection(2)
                
            
                
                #QLabel().setPixmap(QPixmap().loadFromData(urlopen(adres).read()))
                label = QLabel()
                pixmap = QPixmap()
                adres = str(globalURL+pomocnicza[4])
                #print(adres)
                data =  urlopen(adres).read()
                pixmap.loadFromData(data)
                label.setPixmap(pixmap.scaled(260,158))
                layouttytul.addWidget(label)

                tyul = QLabel(pomocnicza[1].replace("<q>", '"').replace("</q>", '"'))
                tyul.setStyleSheet("font: 25px Times New Roman; font-weight: 800")
                layouttytul.addWidget(tyul)
                
                label = QLabel()
                pixmap = QPixmap()
                adres = str(globalURL+pomocnicza[5])
                data =  urlopen(adres).read()
                pixmap.loadFromData(data)
                label.setPixmap(pixmap.scaled(260,158))
                
                layouttytul.addWidget(label)

                layoutdodatek.addLayout(layouttytul)
                opis = QLabel(str(pomocnicza[9]).replace("<b>", "").replace("</b>", ""))
                opis.setStyleSheet("font: 16px")
                opis.setWordWrap(True)
                layoutopisy.addWidget(opis)
                
                layoutdodatek.addLayout(layoutopisy)
                wersja = pomocnicza[6]
                wersja = wersja.split(" ")
                version = QLabel(pomocnicza[6])
                version.setStyleSheet("font: 16px")  
                layoutprzycisk.addWidget(version)  
                przycisk_sprawdz_wiecej = QPushButton("&Instaluj!", self)
                przycisk_sprawdz_wiecej.setStyleSheet("height: 25px; background-color: #082567; color: white")
                przycisk_sprawdz_wiecej.clicked.connect(lambda: self.instaluj(id, pomocnicza[10]))
                #TODO: do ogarnięcia, żeby id szło poprawne :P
                #przycisk_sprawdz_wiecej.setFocusPolicy()
                if SprawdzCzyZainstalowany(sciezka_roota_programu, id):
                    przycisk_sprawdz_wiecej.setDisabled(True)
                    przycisk_sprawdz_wiecej.setStyleSheet("height: 25px; background-color: #808080; color: white")
                layoutprzycisk.addWidget(przycisk_sprawdz_wiecej)
                layoutdodatek.addLayout(layoutprzycisk)

                layoutenty = QHBoxLayout()
                layoutenty.setDirection(2)
                authors = QLabel("Autorzy: "+pomocnicza[7])
                authors.setStyleSheet("font: 16px; line-height: 28px")
                layoutenty.addWidget(authors)
                ReleaseDate = QLabel("Data wydania: "+pomocnicza[12])
                ReleaseDate.setStyleSheet("font: 16px")
                layoutenty.addWidget(ReleaseDate)
                if SprawdzCzyZainstalowany(sciezka_roota, id):
                    #string = PodajDateInstalacji(sciezka_roota, id)
                    InstallDate = QLabel("Data instalacji: "+str(PodajDateInstalacji(sciezka_roota_programu, id)))
                    InstallDate.setStyleSheet("font: 16px;")
                    layoutenty.addWidget(InstallDate)

                layoutdodatek.addLayout(layoutenty)

                frame.setLayout(layoutdodatek)
                frame.setStyleSheet("color: white")
                aktualnyklucz = pomocnicza[2]
                aktualnyklucz = aktualnyklucz.replace(" ", "")
                aktualnyklucz = int(aktualnyklucz)


                formLayout.addRow(frame)
                break

        groupbox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(520)
        scroll.setFixedWidth(1150)
        scroll.horizontalScrollBar().setEnabled(False)





        layoutkolejny.addWidget(scroll)
        layoutV.addLayout(layoutkolejny)
      

        napis2 = QLabel(self)
        napis2.setText(zmiennaCopyright)
        napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
        layoutpomocniczy = QHBoxLayout()
        layoutpomocniczy.addWidget(napis2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

    def pokazwybrane(self, klucz):
        self.clearLayout(layoutV)
        sciezka_roota = PodajSciezkeSymulatora()
        mojawersja = sprawdzwersje(sciezka_roota, globalURL)
        #print(mojawersja)
        #http://stapox.cal24.pl/files/menedzer_dodatki.php

        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
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
            id = int(pomocnicza[0])
            przycisk_sprawdz_wiecej = QPushButton("&Dowiedz się więcej i instaluj! ("+str(id)+")", self)
            przycisk_sprawdz_wiecej.setStyleSheet("height: 25px; background-color: #dc3545; color: white")
            przycisk_sprawdz_wiecej.clicked.connect(lambda: self.pokazszczegoly(0))
            #TODO: do ogarnięcia, żeby id szło poprawne :P
            #przycisk_sprawdz_wiecej.setFocusPolicy()
            layoutprzycisk.addWidget(przycisk_sprawdz_wiecej)
            layoutdodatek.addLayout(layoutprzycisk)
            frame.setLayout(layoutdodatek)
            frame.setStyleSheet("background-color: #999999; border-radius: 8px")
            aktualnyklucz = pomocnicza[2]
            aktualnyklucz = aktualnyklucz.replace(" ", "")
            aktualnyklucz = int(aktualnyklucz)
            if mojawersja != -1 and mojawersja == wersja[1] or mojawersja == -1 and aktualnyklucz == klucz:

                formLayout.addRow(frame)
                
                tablicazezwolen[aktualnyklucz-1] = tablicazezwolen[aktualnyklucz-1]+1
                #print(tablicazezwolen[0])
            elif mojawersja != -1 and mojawersja == wersja[1] or mojawersja == -1 and klucz == -1:
                formLayout.addRow(frame)
                
                tablicazezwolen[aktualnyklucz-1] = tablicazezwolen[aktualnyklucz-1]+1
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

        dodajBtn = QPushButton("&Instaluj wszystkie", self)
        dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #082567; color: white")
        layout3.addWidget(dodajBtn)
        dodajBtn.clicked.connect(lambda: self.ScreenInstallAllAddons())
        dodajBtn = QPushButton("Pokaż &wszystkie", self)
        dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
        layout3.addWidget(dodajBtn)
        dodajBtn.clicked.connect(self.dzialanie)
        
        
        
        if tablicazezwolen[0] != 0:
            dodajBtn = QPushButton("Lokomotywy &elektryczne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[1] != 0:
            dodajBtn = QPushButton("Lokomotywy &spalinowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[2] !=0:
            dodajBtn = QPushButton("Lokomotywy &parowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[3] !=0:
            dodajBtn = QPushButton("Wagony &osobowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[4] !=0:
            dodajBtn = QPushButton("Wagony &towarowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[5] !=0:
            dodajBtn = QPushButton("P&ojazdy specjalne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[7] !=0:
            dodajBtn = QPushButton("Elektryczne &zespoły trakcyjne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[8] !=0:
            dodajBtn = QPushButton("Spalino&we zespoły trakcyjne", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[9] !=0:
            dodajBtn = QPushButton("Wagony &akumulatorowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[10] !=0:
            dodajBtn = QPushButton("Wagony &motorowe", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
            layout3.addWidget(dodajBtn)
            dodajBtn.clicked.connect(self.dzialanie)
        if tablicazezwolen[6] !=0:
            dodajBtn = QPushButton("S&cenerie", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px; background-color: #00b15e")
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
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

    def funkcja2(self):
        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
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
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)

    def funkcja3(self):
        layout = QHBoxLayout()
        dodajBtn = QPushButton("&Home", self)
        dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
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
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
        layoutpomocniczy.addWidget(version)
        #layoutpomocniczy.addSpacing(50)
        layoutV.addLayout(layoutpomocniczy)
    
    def InstallAllAddons(self, Ids, progress,Button):
        a=0
        for i in Ids.split(','):
            if i=="":
                break
            print(i)
            response = requests.get(globalURL+"files/menedzer_dodatki.php")
            data = response.text
            many = 1/int(len(Ids.split(',')))
            for j in data.split(';'):
                if j=="":
                    break
                word = j.split('$')
                IdAddons = int(word[0])
               
                if IdAddons == int(i):
                    a=a+1
                    Valueprogress = self.funckjainstalacji(word[10],progress,Button,IdAddons,False,many)

                    

        QMessageBox.information(self, "Zainstalowano", "Wszystkie dostępne dodatki zostały zainstalowane!", QMessageBox.Ok)
        self.clearLayout(layoutV)
        self.pokazwybrane(-1)
               #print(IdAddons)

    def ScreenInstallAllAddons(self):
        sciezka_roota = PodajSciezkeSymulatora()
        version = sprawdzwersje(sciezka_roota, globalURL)
        sciezka_roota_programu = os.getcwd()
        #print(version)
        Ids = ""
        response = requests.get(globalURL+"files/menedzer_dodatki.php")
        data = response.text

        for i in data.split(';'):
            if i=="":
                break
            word = i.split('$')

            idAddons = int(word[0])
            addonsVer = (word[6].split(' '))[1]
            print(addonsVer)
            if addonsVer == version and not SprawdzCzyZainstalowany(sciezka_roota_programu, idAddons):
                Ids = Ids+str(idAddons)+','
        if(Ids[len(Ids)-1:]) == ',':
            Ids = Ids[:len(Ids)-1]
        print(Ids)
        if Ids == "":
            self.pokazwybrane(-1)
            QMessageBox.information(self, "Błąd!", "Wszystkie dostępne dodatki dla Twojej wersji zostały zainstalowane!", QMessageBox.Ok)
        else:
            progress = QProgressBar()
            self.clearLayout(layoutV)
            layout = QHBoxLayout()
            dodajBtn = QPushButton("&Wróć", self)
            dodajBtn.setStyleSheet("width: 100px; height: 75px;  background-color: #00b15e")
            layout.addWidget(dodajBtn)
            dodajBtn.clicked.connect(lambda: self.pokazwybrane(-1))
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
            layoutinstalacji = QHBoxLayout()
            layoutinstalacji.setDirection(2)
            dodajBtn = QPushButton("&Instaluj!", self)
            dodajBtn.setStyleSheet("width: 100px; height: 50px;  background-color: #00b15e")
            layoutinstalacji.addWidget(dodajBtn)
            dodajBtn.clicked.connect(lambda: self.InstallAllAddons(Ids, progress,dodajBtn))
            label = QLabel("Trwa instalowanie, proszę czekać ... ")
            label.setStyleSheet("font: 40px Times New Roman; color: white")
            layoutinstalacji.addWidget(label)
            
            progress.setGeometry(10,10,500,50)
            layoutinstalacji.addWidget(progress)

            response = requests.get(globalURL+"files/menedzer_dodatki.php")
            data = response.text
            Titles_text = ""
            for i in data.split(';'):
                if i=="":
                    break

                word = i.split('$')
                addonsVer = (word[6].split(' '))[1]
                print(addonsVer)
                if addonsVer == version and not SprawdzCzyZainstalowany(sciezka_roota_programu, idAddons):
                    Titles_text = Titles_text+' '+word[1].replace("<q>", "").replace("</q>", "")+",\n"
            if(Titles_text[len(Titles_text)-2:]) == ',\n':
                Titles_text = Titles_text[:len(Titles_text)-2]
            Titles = QLabel(Titles_text)
            Titles.setStyleSheet("Font: 18px")
            layoutinstalacji.addWidget(Titles)



            layoutV.addLayout(layoutinstalacji)

            #progress.setValue(50)
            napis2 = QLabel(self)
            napis2.setText(zmiennaCopyright)
            napis2.setStyleSheet("font: 25pt Times New Roman; color: white; text-align: center; width: 1200px; text-align: jutify")
            layoutpomocniczy = QHBoxLayout()
            layoutpomocniczy.addWidget(napis2)
            version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
            version.setStyleSheet("font: 15pt Times New Roman; color: white; text-align: center;")
            layoutpomocniczy.addWidget(version)
            #layoutpomocniczy.addSpacing(50)
            layoutV.addLayout(layoutpomocniczy)


        




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = menedzer()
sys.exit(app.exec_())