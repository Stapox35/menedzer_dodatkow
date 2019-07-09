#FOR LINUX
#!/usr/bin/env python3
import os
#FOR WINDOWS
import sys
if sys.platform[:3] == "win":
    if hasattr(sys, 'frozen'):
        os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QScrollArea, QFormLayout, QGroupBox,QFrame,QProgressBar, QFileDialog, QTextEdit
from shapes import Ksztalty, Ksztalt
# from PyQt5.QtWidgets import QHBoxLayout2
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap, QIcon, QImage
from PyQt5.QtCore import QPoint, QRect, QSize
from urllib import *
from urllib.request import urlopen
import requests
from function import TakeMyVersion, IsInstall,TakeInstallDate, TakePathSimulator, CheckPathSimulator, CheckInstallAddons
import array as arr
from pyunpack import Archive
import shutil
import codecs
import datetime
import os as _os
import subprocess
import time

backgroundcolor = "#007e43"
buttonscolor = "#00b15e"
textcolor1 = "white"
textcolor2 = "black"


path_simulator_root = ""
path_program_root = os.getcwd()
globalURL= "http://stapox.cal24.pl/"
CopyrightText = "Copyright © 2019 stapox"
PermissionList = [0,0,0,0,0,0,0,0,0,0,0]
PermissionArray = arr.array('i', PermissionList)
versionMenedzer = "0.3L"
path_simulator_root = ""
log = open(path_program_root+"/log_men.txt", "w+")
x = datetime.datetime.now()
log.write(str(x))
log.close()

class menedzer(QWidget): 
    def __init__(self, parent=None):
        super().__init__(parent)
    
        #self.config()
        if not os.path.isfile(path_program_root+"/.config_men.ini"):
            self.interfejs(False)
        else:
            self.interfejs(True)
    global layoutOM1, layoutV, progress,label
    layoutOM1 = QVBoxLayout()
    layoutV = QVBoxLayout()

    def SaveConfig(self, Path7zArea, PathArea):
        
        os.remove(path_program_root+"/.config_men.ini")
        ini = open(path_program_root+"/.config_men.ini", "w+", encoding="utf-8")
        ini.write("-p "+str(PathArea)+";\n")
        ini.write("-v "+str(versionMenedzer)+"$"+str(x)+";\n")
        if Path7zArea == "":
            ini.write("-z None;\n")
        else:
            ini.write("-z "+str(Path7zArea)+";\n")
       
        ini.write("[ADDONS]\n")
        ini.close()
        CheckInstallAddons(PathArea, globalURL)
        self.interfejs(True)

    def cancelConfig(self, Path7zArea, PathArea):
        if sys.platform[:3] == "win":
            if os.path.isfile(str(Path7zArea)+"/7z.exe") and CheckPathSimulator(str(PathArea)):
                self.interfejs(True)
            else:
                self.interfejs(False)
        else:
            if CheckPathSimulator(str(PathArea)):
                self.interfejs(True)
            else:
                self.interfejs(False)
        
    def changePathSimulator(self, PathTextArea, ButtonSave):
        name = QFileDialog.getExistingDirectory(self, "Podaj ścieżkę do symulatora!")
        PathTextArea.setText(name)
        if CheckPathSimulator(name):
            PathTextArea.setStyleSheet("background-color: green; color: "+textcolor1)
            ButtonSave.setEnabled(True)
        else:
            PathTextArea.setStyleSheet("background-color: red; color: "+textcolor1)
            ButtonSave.setEnabled(False)

    def Autofind7z(self, textArea, ButtonSave):
        #if sys.platform[:3] == "win":
        print("WINDOWS")
        if sys.platform[:3] == "win":
            if os.path.isfile("C:/Program Files (x86)/7-Zip/7z.exe"):
                textArea.setText("C:/Program Files (x86)/7-Zip/")
                textArea.setStyleSheet("background-color: green; color: "+textcolor1)
                ButtonSave.setEnabled(True)
            elif os.path.isfile("C:/Program Files/7-Zip/7z.exe"):
                textArea.setText("C:/Program Files/7-Zip/")
                textArea.setStyleSheet("background-color: green; color: "+textcolor1)
                ButtonSave.setEnabled(True)
            else:
                QMessageBox.warning(self, "Błąd", "Nie znaleziono 7-zip! Proszę wskazać lokalizację ręcznie!", QMessageBox.Ok)
                textArea.setStyleSheet("background-color: red; color: "+textcolor1)
                ButtonSave.setEnabled(False)

    def changePath7z(self, textArea, ButtonSave):
        if sys.platform[:3] == "win":
            name = QFileDialog.getExistingDirectory(self, "Podaj ścieżkę do katalogu 7-zip!")
            if os.path.isfile(name+'/7z.exe'):
                textArea.setText(name)
                textArea.setStyleSheet("background-color: green; color: "+textcolor1)
                ButtonSave.setEnabled(True)
            else:
                QMessageBox.warning(self, "Błąd", "Nie znaleziono 7-zip! Proszę spróbować jeszcze raz!", QMessageBox.Ok)
                textArea.setStyleSheet("background-color: red; color: "+textcolor1)
                ButtonSave.setEnabled(False)

    def config(self):
        self.clearLayout(layoutV)
        layoutTitle = QHBoxLayout()
        url = globalURL+"img/logo_maszyna.gif"  
        label = QLabel()
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        layoutTitle.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        layoutTitle.addWidget(inscription)
        layoutV.addLayout(layoutTitle)
        layoutPath = QHBoxLayout()

        textStarted = QLabel("Konfiguracja menedżera")
        textStarted.setStyleSheet("font: 35px Times New Roman;  color: "+textcolor1+"; font-weight: 800")
        layoutV.addWidget(textStarted)
        '''
        configFile = QLabel("Plik konfiguracyjny: "+path_program_root+"/.config_men.ini")
        configFile.setStyleSheet("font: 18px Times New Roman;  color: "+textcolor1+";")
        layoutV.addWidget(configFile)
        '''

        configPathLayout = QHBoxLayout()
        configPathLayout.setDirection(2)
        textPath = QLabel("Proszę wybrać ścieżkę do głównego katalogu symulatora maszyna")
        textPath.setStyleSheet("font: 20px Times New Roman;  color: "+textcolor1)
        layoutV.addWidget(textPath)
        FolderPath = QTextEdit()
        #FolderPath.setText("KUPA")
        FolderPath.setMaximumHeight(35)
        FolderPath.setMinimumHeight(35)
        FolderPath.setStyleSheet("color: "+textcolor1)
        FolderPath.setPlaceholderText("Ścieżka do symulatora")
        layoutPath.addWidget(FolderPath)

        FolderPathButton = QPushButton("Przeglądaj")
        FolderPathButton.setStyleSheet("width: 200px; height: 35px; background-color: "+buttonscolor)
        FolderPathButton.clicked.connect(lambda: self.changePathSimulator(FolderPath, SaveBtn))
        layoutPath.addWidget(FolderPathButton)
        #configPathLayout.addLayout(layoutPath)
        layoutV.addLayout(layoutPath)

        version = QLabel("Wersja menedżera - "+versionMenedzer)
        version.setStyleSheet("font: 20px Times New Roman;  color: "+textcolor1)
        layoutV.addWidget(version)
        sysVer = QLabel()
        sysVer.setStyleSheet("font: 20px Times New Roman;  color: "+textcolor1)
        if sys.platform[:3] == "win":
            if sys.platform[3:5] == "32":
                sysVer.setText("System: Windows 32-bitowy")
            if sys.platform[3:5] == "64":
                sysVer.setText("System: Windows 64-bitowy")
        elif sys.platform[:5] == "linux":
            sysVer.setText("System: Linux")
        else:
            sysVer.setText("System: "+sys.platform)
        layoutV.addWidget(sysVer)

        zip7label = QLabel("Program 7-zip")
        zip7label.setStyleSheet("font: 20px Times New Roman;  color: "+textcolor1)
        #if windows
        layoutV.addWidget(zip7label)
    
        layout7zip = QHBoxLayout()
        Folder7zipPath = QTextEdit()
        Folder7zipPath.setMaximumHeight(35)
        Folder7zipPath.setMinimumHeight(35)
        Folder7zipPath.setPlaceholderText("Ścieżka do programu 7-zip")
        layout7zip.addWidget(Folder7zipPath)

        View7zip = QPushButton("Przeglądaj")
        View7zip.setStyleSheet("width: 200px; height: 35px; background-color: "+buttonscolor)
        layout7zip.addWidget(View7zip)

        View7zipAuto = QPushButton("Znajdź automatycznie")
        View7zipAuto.setStyleSheet("width: 200px; height: 35px; background-color: "+buttonscolor)
        View7zipAuto.clicked.connect(lambda: self.Autofind7z(Folder7zipPath, SaveBtn))
        layout7zip.addWidget(View7zipAuto)

        layoutV.addLayout(layout7zip)

        if sys.platform[:3] != "win":
            View7zip.setEnabled(False)
            View7zipAuto.setEnabled(False)
            Folder7zipPath.setEnabled(False)
            zip7label.setStyleSheet("font: 20px Times New Roman;  color: grey")
        layoutButtons = QHBoxLayout()

        CancelBtn = QPushButton("&Anuluj")
        CancelBtn.setStyleSheet("width: 200px; height: 75px; background-color: "+buttonscolor)
        layoutButtons.addWidget(CancelBtn)
        CancelBtn.clicked.connect(lambda: self.cancelConfig(str(Folder7zipPath.toPlainText()), str(FolderPath.toPlainText())))


        SaveBtn = QPushButton("&Zapisz ustawienia")
        SaveBtn.setStyleSheet("width: 200px; height: 75px; background-color: "+buttonscolor)
        SaveBtn.clicked.connect(lambda: self.SaveConfig(str(Folder7zipPath.toPlainText()), str(FolderPath.toPlainText())))
        layoutButtons.addWidget(SaveBtn)

        layoutV.addLayout(layoutButtons)

        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)

        if os.path.isfile(path_program_root+"/.config_men.ini"):
            FolderPath.setText(TakePathSimulator())
            print(TakePathSimulator())
            if CheckPathSimulator(str(TakePathSimulator())):
                FolderPath.setStyleSheet("background-color: green; color: "+textcolor1)
                SaveBtn.setEnabled(True)
            else:
                FolderPath.setStyleSheet("background-color: red; color: "+textcolor1)
                SaveBtn.setEnabled(False)


        '''

        log = open(path_program_root+"/log_men.txt", "a")
        log.write(path_program_root)
        log.write("\r\n rozpoczynamy config\r\n")
        firstrunbool = False
        if not os.path.isfile(path_program_root+"/.config_men.ini"):
            firstrunbool = True
        if firstrunbool:
            name = QFileDialog.getExistingDirectory(self, "Podaj ścieżkę do symulatora!")
            print(str(name))
            if str(name) == "":
                self.destroy()
                if sys.platform[:3] == "win":
                    sys.exit(0)
                if sys.platform[:5] == "linux":
                    exit()
            path_simulator_root = str(name)
            ini = open(path_program_root+"/.config_men.ini", "w+")
            x = datetime.datetime.now()
            ini.write("-p "+str(path_simulator_root)+";\n")
            ini.write("-v "+str(versionMenedzer)+"$"+str(x)+";\n")
            ini.write("[ADDONS]\n")
            response = requests.get(globalURL+"files/menedzer_dodatki.php")
            data = response.text
            data = data.replace("<br>", "")
            data = data.replace("<br/>", "")
            data = data.replace("<br />", "")
            data = data.split(';')
            for i in data:
                auxiliaryVariable = i.split("$")
                CurrentId = int(auxiliaryVariable[0])
                adresRI = auxiliaryVariable[10]
                VerifyBool = False
                response = requests.get(adresRI)
                dataRI = response.text
                ThisIdBool=True
                for o in dataRI.split('\n'):
                    o=o.replace("\r", "").replace(" ", "").replace("\t", "")
                    if VerifyBool:
                        if o =="":
                            VerifyBool = False
                        path = o.split("=")[0]
                        if path != "":
                            path = path.replace('\\', "/")
                            #print(path_simulator_root+"/"+path)
                            if not os.path.isfile(path_simulator_root+"/"+path):
                                ThisIdBool = False  
                    if o[:8] == "[VERIFY]":
                        VerifyBool = True
                if ThisIdBool == True:
                    ini.write("-a "+str(CurrentId)+"$"+str(1)+"$"+str(x)+";\n")
                if CurrentId == 1:
                    break
            ini.close()
        path_simulator_root = str(TakePathSimulator())
        MaszynaBool = True
        print(path_simulator_root)
        if not os.path.isdir(path_simulator_root+"/dynamic"):
            MaszynaBool = False
        if not os.path.isdir(path_simulator_root+"/textures"):
            MaszynaBool = False
        if not os.path.isdir(path_simulator_root+"/scenery"):
            MaszynaBool = False
        
        if MaszynaBool == False:
            QMessageBox.warning(self, "Błąd", "Skonfiguruj jeszcze raz program!", QMessageBox.Ok)
            os.remove(path_program_root+"/.config_men.ini")
            #print(name)
        
            self.config()
            #koment
            self.destroy()
            exit()
        #koment
        #print(path_program_root)
        print(path_simulator_root)
        log.close()
        '''

    def NewConfig(self):
        self.config()

    def interfejs(self, FlagActive=True):
        self.clearLayout(layoutV)
        path_program_root = os.getcwd()
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

        
        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

            
                
       



        layout.addWidget(inscription)
        layoutV.addLayout(layout)

        layout2 = QHBoxLayout()

        Image = QLabel(self)
        url2 = globalURL+"img/img_tytulowa.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        Image.setPixmap(pixmap3)
        Image.move(0,125)
        

        layout2.addWidget(Image)
        layout3 = QHBoxLayout()
        layout3.setDirection(2)
        addPushButton = QPushButton("&Instaluj dodatki", self)
        addPushButton.setStyleSheet("width: 200px; height: 75px; background-color: "+buttonscolor)
        layout3.addWidget(addPushButton)
        addPushButton.setEnabled(FlagActive)
        addPushButton2 = QPushButton("O &projekcie", self)
        addPushButton2.setStyleSheet("width: 200px; height: 75px; background-color: "+buttonscolor)
        layout3.addWidget(addPushButton2)
        addPushButton3 = QPushButton("O &zespole", self)
        addPushButton3.setStyleSheet("width: 200px; height: 75px; background-color: "+buttonscolor)
        layout3.addWidget(addPushButton3)
        addPushButton4 = QPushButton("&Kontakt", self)
        addPushButton4.setStyleSheet("width: 200px; height: 75px; background-color: "+buttonscolor)
        layout3.addWidget(addPushButton4)
        layout3.setSpacing(32)
        layout2.addLayout(layout3)
        
        layoutV.addLayout(layout2)
        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px")

        
        
        HelpingLayout = QHBoxLayout()

        configBtn = QPushButton("&Konfiguruj", self)
        configBtn.setStyleSheet("width: 50px; height: 75px; background-color: "+buttonscolor)
        HelpingLayout.addWidget(configBtn)
        configBtn.clicked.connect(self.ActionFunction)
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)


        



        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)

       
        inscription3 = QLabel()
        inscription3.setText("O Projekcie")
        inscription2.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px")
        layoutOM1.addWidget(inscription3)

       
            

        
        addPushButton.clicked.connect(self.ActionFunction)
        addPushButton2.clicked.connect(self.ActionFunction)
        addPushButton3.clicked.connect(self.ActionFunction)
        addPushButton4.clicked.connect(self.ActionFunction)

        layoutX = QVBoxLayout()
        layoutX.setDirection(2)

        self.setWindowTitle("Menedżer nieoficjalnych dodatków")
        '''
        url2 = globalURL+"img/tlo.jpg"
        Image = QLabel(self)
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        Image.setPixmap(pixmap3)
       # layoutX.addWidget(Image)
       #layoutV.addChildLayout(layoutX)
       '''
        self.resize(1200, 675)
        self.setFixedSize(1200,675)
        self.setWindowIcon(QIcon(path_program_root+'/icon.ico'))
        print(path_program_root+'/icon.ico')
        self.setStyleSheet("background-color: "+backgroundcolor)
        self.setLayout(layoutV)

        #self.setLayout(layoutV)
        self.show()
        #self.config()
    
    def ActionFunction(self):

        senderVariable = self.sender()   

        print(senderVariable.objectName())  

        if senderVariable.text() == "O &projekcie":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.function1()
        if senderVariable.text() == "O &zespole":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.Function2()
        if senderVariable.text() == "&Home":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.interfejs()
        if senderVariable.text() == "&Kontakt":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.Function3()
        if senderVariable.text() == "&Instaluj dodatki":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(-1)
        if senderVariable.text() == "Lokomotywy &elektryczne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(1)
        if senderVariable.text() == "Lokomotywy &spalinowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(2)
        if senderVariable.text() == "Lokomotywy &parowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(3)
        if senderVariable.text() == "Wagony &osobowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(4)
        if senderVariable.text() == "Wagony &towarowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(5)
        if senderVariable.text() == "P&ojazdy specjalne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(6)
        if senderVariable.text() == "S&cenerie":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(7)
        if senderVariable.text() == "Elektryczne &zespoły trakcyjne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(8)
        if senderVariable.text() == "Spalino&we zespoły trakcyjne":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(9)
        if senderVariable.text() == "Wagony &akumulatorowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(10)
        if senderVariable.text() == "Wagony &motorowe":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(11)
        if senderVariable.text() == "Pokaż &wszystkie":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(-1)
        if senderVariable.text() == "&Wróć":
            #QMessageBox.warning(self, "Błąd", "Instalowanie dodatków", QMessageBox.Ok)
            self.clearLayout(layoutV)
            self.ViewChoose(-1)
        if senderVariable.text() == "&Konfiguruj":
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

    def function1(self):
        layout = QHBoxLayout()
        addPushButton = QPushButton("&Home", self)
        addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
        layout.addWidget(addPushButton)
        addPushButton.clicked.connect(self.ActionFunction)

        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

        layout.addWidget(inscription)

        layoutV.addLayout(layout)

        layout2 = QHBoxLayout()

        Image = QLabel(self)
        url2 = globalURL+"img/skrin-o-projekcie.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        Image.setPixmap(pixmap3)
        Image.move(0,125)
        
        layout3 = QHBoxLayout()
        layout3.setDirection(2)

        inscription5 = QLabel(self)
        inscription5.setText("O Projekcie")
        inscription5.setStyleSheet("font: 18pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        layout3.addWidget(inscription5)

        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        data = data.replace('\n', ' ')
        #i = 0
        ProjectBool = False
        text = data.split(' ')
        textpl = ""
        for s in text:
            if ProjectBool:
                if s == "[OZ]":
                    ProjectBool = False
                    break
                textpl = textpl+' '+s
            if s == "[OP]":
                ProjectBool = True
                #print("rozpoczalem_wydzielac")
        
       #print(textpl[5:len(textpl)-2])

        inscriptionPL = QLabel(self)
        inscriptionPL.setText(textpl[5:len(textpl)-1])
        inscriptionPL.setStyleSheet("font: 16pt Times New Roman;  color: "+textcolor1)
        inscriptionPL.setWordWrap(True)
        layout3.addWidget(inscriptionPL)
        layout2.addWidget(Image)
        layout2.addLayout(layout3)
        layoutV.addLayout(layout2)

        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)
    
    def InstallFunction(self, adres, progress, Button,id,flaga, labeltex, multiplier=1):
        log = open(path_program_root+"/log_men.txt", "a", encoding="utf-8")
        path_simulator_root = TakePathSimulator()
        response = requests.get(adres)
        labeltex.setText("Trwa instalacja, proszę czekać ...")
        data = response.text
        #progress.setValue(1)
        progress.setValue(progress.value()+14.28*1*multiplier) #14%
        download = False
        LinkVariable=""
        adrestext = ""
        series="x"
        seriesflaga = False
        textures = False
        RegTextures=""
        CoorTextures="\n"
        for i in data.split("\n"):
            i = i.replace("\t", "")
            i = i.replace("\r", "")
            i = i.replace(" ", "")
            if download:
                i = i.split("=")
                LinkVariable = i[0]
                download = False
            if textures:
                i = i.split("=")
                adrestext = i[0]
                series = i[1]
                textures = False
            if seriesflaga:
                if i =="":
                    seriesflaga = False
                if i[:1] == "!":
                    CoorTextures = i
                else:
                    i = str(i).replace("\n", "").replace(" ","").replace("\r\n", "").replace("\t", "").replace("\r", "")
                    RegTextures = RegTextures+str(i)+"\r\n"
            if i[:10] == "[DOWNLOAD]":
                download = True
            if i[:14] == "[TEXTURES.TXT]":
                textures = True
            if i[:len(series)+2] == "["+series+"]":
                seriesflaga = True
        print(LinkVariable)
        print(adrestext)
        print(series)
        print(CoorTextures)
        print(RegTextures)
        log.write(str(LinkVariable+"\r\n"))
        log.write(str(adrestext+"\r\n"))
        log.write(str(series+"\r\n"))
        log.write(str(CoorTextures+"\r\n"))
        progress.setValue(progress.value()+14.28*1*multiplier)
        
        filename = os.path.basename(LinkVariable)

        response = requests.get(LinkVariable, stream=True)
        TempPath = path_simulator_root+"/temp/"
        if not os.path.exists(TempPath):
            os.makedirs(TempPath)
        progress.setValue(progress.value()+14.28*1*multiplier)
        if response.status_code == 200:
            with open(TempPath+filename, 'wb') as out:
                out.write(response.content)
                adresArciwum = TempPath+filename
                progress.setValue(progress.value()+14.28*1*multiplier)
        else:
            print('Request failed: %d' % response.status_code)
            QMessageBox.warning(self, "Błąd", "Pobieranie dodatku nie powiodło się! Proszę spróbować jeszcze raz", QMessageBox.Ok)
            self.ViewDetails(id)
        if sys.platform[:3] == "win":
            if os.path.isfile("C:/Program Files (x86)/7-Zip/7z.exe"):
                log.write("\r\n 7zip x86 ")
                file7z = '"C:/Program Files (x86)/7-Zip/7z.exe" x "'+adresArciwum +'" -o"'+path_simulator_root+'" -y'
                subprocess.call(file7z)
            elif os.path.isfile("C:/Program Files/7-Zip/7z.exe"):
                log.write("\r\n 7zip Programfiles ")
                file7z='"C:/Program Files/7-Zip/7z.exe" x "'+adresArciwum +'" -o"'+path_simulator_root+'"  -y'
                subprocess.call(file7z)
            else:
                QMessageBox.warning(self, "Błąd", "Nie znaleziono 7-zip! Proszę zainstalować!!!", QMessageBox.Ok)
                self.ViewDetails(id)
                log.write("\r\n 7zip Brak")
        if sys.platform[:5] == "linux":
            Archive(adresArciwum).extractall(path_simulator_root)
        progress.setValue(progress.value()+14.28*1*multiplier)
        textures = open(path_simulator_root+"/"+adrestext+"/textures.txt", "a", encoding="utf-8")
        textures.write("\r\n"+RegTextures)
        textures.close()

        progress.setValue(progress.value()+14.28*1*multiplier)
        shutil.rmtree(TempPath, ignore_errors=True)
        log.write("57\r\n")
        #os.system("del "+TempPath)
        log.write("usuniete\r\n")
        
        progress.setValue(multiplier*100)
        print(round(progress.value()/(multiplier*100), 0))
        Button.setDisabled(True)
        ini = open(path_program_root+"/.config_men.ini", "a")
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
            self.ViewDetails(id)
        if not flaga:
            return progress.value()
    def Install(self, id, adres):
        progress = QProgressBar()
        label = QLabel
        path_simulator_root = TakePathSimulator()
        print(adres)
        adres = adres
        self.clearLayout(layoutV)
        layout = QHBoxLayout()
        addPushButton = QPushButton("&Wróć", self)
        addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
        layout.addWidget(addPushButton)
        addPushButton.clicked.connect(lambda: self.ViewDetails(id))
        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

        layout.addWidget(inscription)

        layoutV.addLayout(layout)
        layoutinstalacji = QHBoxLayout()
        layoutinstalacji.setDirection(2)
        addPushButton = QPushButton("&Instaluj!")

        addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color:  #082567; color: white")
        layoutinstalacji.addWidget(addPushButton)
        addPushButton.clicked.connect(lambda: self.InstallFunction(adres,progress,addPushButton,id,True,label))

        label.setText("Po naciśnięciu przcisku dodatek zostanie zainstalowany")
        label.setStyleSheet("font: 40px Times New Roman;  color: "+textcolor1)
        layoutinstalacji.addWidget(label)
        
        progress.setGeometry(10,10,500,50)
        layoutinstalacji.addWidget(progress)
        layoutV.addLayout(layoutinstalacji)

        #progress.setValue(50)
        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)

        #time.sleep(1)
        #self.InstallFunction(adres,progress,addPushButton,id,True)
        #self.InstallFunction(adres, progress)


    def ViewDetails(self, id):
        path_simulator_root = TakePathSimulator()
        print(str(id))
        if not id:
            senderVariable = self.sender()   
            id = int(senderVariable.objectName())
        self.clearLayout(layoutV)

        layout = QHBoxLayout()
        addPushButton = QPushButton("&Wróć", self)
        addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
        layout.addWidget(addPushButton)
        addPushButton.clicked.connect(self.ActionFunction)

        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

        layout.addWidget(inscription)

        layoutV.addLayout(layout)

        
        NextLayout = QHBoxLayout()
        
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
            auxiliaryVariable = str(i).split('$')

            CurrentId = auxiliaryVariable[0].replace(" ", "")
            if int(CurrentId) == id:

                AddonsLayout = QHBoxLayout()
                ButtonLayout = QHBoxLayout()
                DescLayout = QHBoxLayout()
                TitleLayout = QHBoxLayout()

                AddonsLayout.setDirection(2)
                
            
                
                #QLabel().setPixmap(QPixmap().loadFromData(urlopen(adres).read()))
                label = QLabel()
                pixmap = QPixmap()
                adres = str(globalURL+auxiliaryVariable[4])
                #print(adres)
                data =  urlopen(adres).read()
                pixmap.loadFromData(data)
                label.setPixmap(pixmap.scaled(260,158))
                TitleLayout.addWidget(label)

                tyul = QLabel(auxiliaryVariable[1].replace("<q>", '"').replace("</q>", '"'))
                tyul.setStyleSheet("font: 25px Times New Roman; font-weight: 800")
                TitleLayout.addWidget(tyul)
                
                label = QLabel()
                pixmap = QPixmap()
                adres = str(globalURL+auxiliaryVariable[5])
                data =  urlopen(adres).read()
                pixmap.loadFromData(data)
                label.setPixmap(pixmap.scaled(260,158))
                
                TitleLayout.addWidget(label)

                AddonsLayout.addLayout(TitleLayout)
                Description = QLabel(str(auxiliaryVariable[9]).replace("<b>", "").replace("</b>", ""))
                Description.setStyleSheet("font: 16px")
                Description.setWordWrap(True)
                DescLayout.addWidget(Description)
                
                AddonsLayout.addLayout(DescLayout)
                Version = auxiliaryVariable[6]
                Version = Version.split(" ")
                version = QLabel(auxiliaryVariable[6])
                version.setStyleSheet("font: 16px")  
                ButtonLayout.addWidget(version)  

                ButtonCheckMore = QPushButton("&Instaluj!", self)
                ButtonCheckMore.setStyleSheet("height: 25px; background-color:  #082567;  color: "+textcolor1)
                #ButtonCheckMore.clicked.connect(lambda: self.HelpingFunctionInstall(id, auxiliaryVariable[10], None, True, 1))
                ButtonCheckMore.clicked.connect(lambda: self.Install(id, auxiliaryVariable[10],))

                #TODO: do ogarnięcia, żeby id szło poprawne :P
                #ButtonCheckMore.setFocusPolicy()
                if IsInstall(path_program_root, id):
                    ButtonCheckMore.setDisabled(True)
                    ButtonCheckMore.setStyleSheet("height: 25px; background-color: #808080;  color: "+textcolor1)
                ButtonLayout.addWidget(ButtonCheckMore)
                AddonsLayout.addLayout(ButtonLayout)

                MoreLayout = QHBoxLayout()
                MoreLayout.setDirection(2)
                authors = QLabel("Autorzy: "+auxiliaryVariable[7])
                authors.setStyleSheet("font: 16px; line-height: 28px")
                MoreLayout.addWidget(authors)
                ReleaseDate = QLabel("Data wydania: "+auxiliaryVariable[12])
                ReleaseDate.setStyleSheet("font: 16px")
                MoreLayout.addWidget(ReleaseDate)
                if IsInstall(path_simulator_root, id):
                    #string = TakeInstallDate(path_simulator_root, id)
                    InstallDate = QLabel("Data instalacji: "+str(TakeInstallDate(path_program_root, id)))
                    InstallDate.setStyleSheet("font: 16px;")
                    MoreLayout.addWidget(InstallDate)

                AddonsLayout.addLayout(MoreLayout)

                frame.setLayout(AddonsLayout)
                frame.setStyleSheet(" color: "+textcolor1)
                CurrectKey = auxiliaryVariable[2]
                CurrectKey = CurrectKey.replace(" ", "")
                CurrectKey = int(CurrectKey)


                formLayout.addRow(frame)
                break

        groupbox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(520)
        scroll.setFixedWidth(1150)
        scroll.horizontalScrollBar().setEnabled(False)





        NextLayout.addWidget(scroll)
        layoutV.addLayout(NextLayout)
      

        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)

    def ViewChoose(self, Key):
        self.clearLayout(layoutV)
        path_simulator_root = TakePathSimulator()
        MyVersion = TakeMyVersion(path_simulator_root, globalURL)
        #print(MyVersion)
        #http://stapox.cal24.pl/files/menedzer_dodatki.php

        layout = QHBoxLayout()
        addPushButton = QPushButton("&Home", self)
        addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
        layout.addWidget(addPushButton)
        addPushButton.clicked.connect(self.ActionFunction)

        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

        layout.addWidget(inscription)

        layoutV.addLayout(layout)

        

        NextLayout = QHBoxLayout()
        
        response = requests.get(globalURL+"files/menedzer_dodatki.php")
        data = response.text
        
        data = data.replace("<br>", "")
        data = data.replace("<br/>", "")
        data = data.replace("<br />", "")
        data = data.split(';')
        #print(data[0])
        formLayout = QFormLayout()
        groupbox = QGroupBox()
        #print(table)
        d = 0

        for i in data:
            if i == "":
                break
            frame = QFrame()
            auxiliaryVariable = str(i).split('$')
            CurrentId = auxiliaryVariable[0].replace(" ", "")
            AddonsLayout = QHBoxLayout()
            ButtonLayout = QHBoxLayout()
            DescLayout = QHBoxLayout()
            AddonsLayout.setDirection(2)
            
            tyul = QLabel(auxiliaryVariable[1].replace("<q>", '"').replace("</q>", '"'))
            tyul.setStyleSheet("font: 25px Times New Roman; font-weight: 800")
            AddonsLayout.addWidget(tyul)
            
            #QLabel().setPixmap(QPixmap().loadFromData(urlopen(adres).read()))
            label = QLabel()
            pixmap = QPixmap()
            adres = str(globalURL+auxiliaryVariable[3])
            #print(adres)
            data =  urlopen(adres).read()
            pixmap.loadFromData(data)
            label.setPixmap(pixmap)
            #label.move(20,15)
            DescLayout.addWidget(label)
            Description = QLabel(auxiliaryVariable[8])
            Description.setWordWrap(True)
            DescLayout.addWidget(Description)
            
            AddonsLayout.addLayout(DescLayout)
            Version = auxiliaryVariable[6]
            Version = Version.split(" ")
            ButtonLayout.addWidget(QLabel(auxiliaryVariable[6]))
            id = int(auxiliaryVariable[0])
            ButtonCheckMore = QPushButton("Dowiedz się więcej!")
            #ButtonCheckMore = QPushButton("Dowiedz się więcej!")
            ButtonCheckMore.setStyleSheet("height: 25px; background-color:  #082567;  color: "+textcolor1)
            ButtonCheckMore.setObjectName(str(id))
            ButtonLayout.addWidget(ButtonCheckMore)
            ButtonCheckMore.clicked.connect(self.ViewDetails)
            #ButtonCheckMore.clicked.connect(self.ActionFunction)
            
            #ButtonCheckMoreArray.append(ButtonCheckMore)

            
            #TODO: do ogarnięcia, żeby id szło poprawne :P
            #ButtonCheckMore.setFocusPolicy()


            AddonsLayout.addLayout(ButtonLayout)
            d=d+1
            frame.setLayout(AddonsLayout)
            frame.setStyleSheet("background-color: #999999; border-radius: 8px")
            CurrectKey = auxiliaryVariable[2]
            CurrectKey = CurrectKey.replace(" ", "")
            CurrectKey = int(CurrectKey)
            if MyVersion != -1 and MyVersion == Version[1] or MyVersion == -1 and CurrectKey == Key:

                formLayout.addRow(frame)
                
                PermissionArray[CurrectKey-1] = PermissionArray[CurrectKey-1]+1
                #print(PermissionArray[0])
            elif MyVersion != -1 and MyVersion == Version[1] or MyVersion == -1 and Key == -1:
                formLayout.addRow(frame)
                
                PermissionArray[CurrectKey-1] = PermissionArray[CurrectKey-1]+1
            if(CurrentId == 1):
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

        addPushButton = QPushButton("&Instaluj wszystkie", self)
        addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color: #082567;  color: "+textcolor1)
        layout3.addWidget(addPushButton)
        addPushButton.clicked.connect(lambda: self.ScreenInstallAllAddons())
        addPushButton = QPushButton("Pokaż &wszystkie", self)
        addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
        layout3.addWidget(addPushButton)
        addPushButton.clicked.connect(self.ActionFunction)
        
        #print(ButtonCheckMoreArray)
        
        if PermissionArray[0] != 0:
            addPushButton = QPushButton("Lokomotywy &elektryczne", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[1] != 0:
            addPushButton = QPushButton("Lokomotywy &spalinowe", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[2] !=0:
            addPushButton = QPushButton("Lokomotywy &parowe", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[3] !=0:
            addPushButton = QPushButton("Wagony &osobowe", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[4] !=0:
            addPushButton = QPushButton("Wagony &towarowe", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[5] !=0:
            addPushButton = QPushButton("P&ojazdy specjalne", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[7] !=0:
            addPushButton = QPushButton("Elektryczne &zespoły trakcyjne", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[8] !=0:
            addPushButton = QPushButton("Spalino&we zespoły trakcyjne", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[9] !=0:
            addPushButton = QPushButton("Wagony &akumulatorowe", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[10] !=0:
            addPushButton = QPushButton("Wagony &motorowe", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)
        if PermissionArray[6] !=0:
            addPushButton = QPushButton("S&cenerie", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px; background-color: "+buttonscolor)
            layout3.addWidget(addPushButton)
            addPushButton.clicked.connect(self.ActionFunction)

        


        
        NextLayout.addWidget(scroll_area)
        NextLayout.addWidget(scroll)
        layoutV.addLayout(NextLayout)
      

        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)

    def Function2(self):
        layout = QHBoxLayout()
        addPushButton = QPushButton("&Home", self)
        addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
        layout.addWidget(addPushButton)
        addPushButton.clicked.connect(self.ActionFunction)

        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

        layout.addWidget(inscription)

        layoutV.addLayout(layout)

        layout2 = QHBoxLayout()

        Image = QLabel(self)
        url2 = globalURL+"img/skrin-o-zespole.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        Image.setPixmap(pixmap3)
        Image.move(0,125)
        
        layout3 = QHBoxLayout()
        layout3.setDirection(2)

        inscription5 = QLabel(self)
        inscription5.setText("O Zespole")
        inscription5.setStyleSheet("font: 18pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        layout3.addWidget(inscription5)

        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        data = data.replace('\n', ' ')
        i = 0
        ProjectBool = False
        text = data.split(' ')
        textpl = ""
        for s in text:
            if ProjectBool:
                if s == "[KONT]":
                    ProjectBool = False
                    break
                textpl = textpl+' '+s
            if s == "[OZ]":
                ProjectBool = True
                #print("rozpoczalem_wydzielac")
        
        #print(textpl[5:len(textpl)-2])

        inscriptionPL = QLabel(self)
        inscriptionPL.setText(textpl[5:len(textpl)-1])
        inscriptionPL.setStyleSheet("font: 16pt Times New Roman;  color: "+textcolor1)
        inscriptionPL.setWordWrap(True)
        layout3.addWidget(inscriptionPL)
        layout2.addLayout(layout3)
        layout2.addWidget(Image)
        
        layoutV.addLayout(layout2)

        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)

    def Function3(self):
        layout = QHBoxLayout()
        addPushButton = QPushButton("&Home", self)
        addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
        layout.addWidget(addPushButton)
        addPushButton.clicked.connect(self.ActionFunction)

        label = QLabel(self)
        url = globalURL+"img/logo_maszyna.gif"  
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap2 = pixmap.scaled(251, 70)
        label.setPixmap(pixmap2)
        label.move(20,15)
        layout.addWidget(label)

        inscription = QLabel(self)
        inscription.setText("Menedżer nieoficjalnych dodatków")
        inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        inscription.move(400, 25)

        layout.addWidget(inscription)

        layoutV.addLayout(layout)

        layout2 = QHBoxLayout()

        Image = QLabel(self)
        url2 = globalURL+"img/scr-kontakt.jpg"
        data =  urlopen(url2).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data)
        #  pixmap4 = pixmap3.scaled(755, 425)
        Image.setPixmap(pixmap3)
        Image.move(0,125)
        
        layout3 = QHBoxLayout()
        layout3.setDirection(2)

        inscription5 = QLabel(self)
        inscription5.setText("Kontakt")
        inscription5.setStyleSheet("font: 20pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
        layout3.addWidget(inscription5)

        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        data = data.replace('\n', ' ')
        i = 0
        ProjectBool = False
        text = data.split(' ')
        textpl = ""
        for s in text:
            if ProjectBool:
                if s == "[END]":
                    ProjectBool = False
                    break
                textpl = textpl+' '+s
            if s == "[KONT]":
                ProjectBool = True
                #print("rozpoczalem_wydzielac")
        
        #print(textpl[5:len(textpl)-2])

        inscriptionPL = QLabel(self)
        setetx = textpl[5:len(textpl)-1]
        setetx = setetx.split('"')
        inscriptionPL.setText(setetx[0])
        inscriptionPL.setStyleSheet("font: 16pt Times New Roman;  color: "+textcolor1)
        inscriptionPL.setWordWrap(True)

        inscriptionPL2 = QLabel(self)
        inscriptionPL2.setText("Mail do uber-admina stapoxa: "+setetx[2])
        inscriptionPL2.setStyleSheet("font: 16pt Times New Roman;  color: "+textcolor1)

        layout3.addWidget(inscriptionPL)
        layout3.addWidget(inscriptionPL2)
        layout2.addLayout(layout3)
        layout2.addWidget(Image)
        
        layoutV.addLayout(layout2)

        inscription2 = QLabel(self)
        inscription2.setText(CopyrightText)
        inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
        HelpingLayout = QHBoxLayout()
        HelpingLayout.addWidget(inscription2)
        version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
        version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
        HelpingLayout.addWidget(version)
        #HelpingLayout.addSpacing(50)
        layoutV.addLayout(HelpingLayout)
    


    def InstallAllAddons(self, Ids, progress,Button,Label):
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
                    Valueprogress = self.InstallFunction(word[10],progress,Button,IdAddons,False,Label,many)

                    

        QMessageBox.information(self, "Zainstalowano", "Wszystkie dostępne dodatki zostały zainstalowane!", QMessageBox.Ok)
        self.clearLayout(layoutV)
        self.ViewChoose(-1)
               #print(IdAddons)

    def ScreenInstallAllAddons(self):
        path_simulator_root = TakePathSimulator()
        version = TakeMyVersion(path_simulator_root, globalURL)
        path_program_root = os.getcwd()
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
            if addonsVer == version and not IsInstall(path_program_root, idAddons):
                Ids = Ids+str(idAddons)+','
        if(Ids[len(Ids)-1:]) == ',':
            Ids = Ids[:len(Ids)-1]
        print(Ids)
        if Ids == "":
            self.ViewChoose(-1)
            QMessageBox.information(self, "Błąd!", "Wszystkie dostępne dodatki dla Twojej wersji zostały zainstalowane!", QMessageBox.Ok)
        else:
            progress = QProgressBar()
            self.clearLayout(layoutV)
            layout = QHBoxLayout()
            addPushButton = QPushButton("&Wróć", self)
            addPushButton.setStyleSheet("width: 100px; height: 75px;  background-color: "+buttonscolor)
            layout.addWidget(addPushButton)
            addPushButton.clicked.connect(lambda: self.ViewChoose(-1))
            label = QLabel(self)
            url = globalURL+"img/logo_maszyna.gif"  
            data = urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap2 = pixmap.scaled(251, 70)
            label.setPixmap(pixmap2)
            label.move(20,15)
            layout.addWidget(label)

            inscription = QLabel(self)
            inscription.setText("Menedżer nieoficjalnych dodatków")
            inscription.setStyleSheet("font: 30pt Times New Roman;  color: "+textcolor1+"; font-weight: 700")
            inscription.move(400, 25)

            layout.addWidget(inscription)

            layoutV.addLayout(layout)
            layoutinstalacji = QHBoxLayout()
            layoutinstalacji.setDirection(2)
            addPushButton = QPushButton("&Instaluj!", self)
            addPushButton.setStyleSheet("width: 100px; height: 50px;  background-color:  #082567; color: white")
            layoutinstalacji.addWidget(addPushButton)
            addPushButton.clicked.connect(lambda: self.InstallAllAddons(Ids, progress,addPushButton,label))
            label = QLabel("Po naciśnięciu przycisku rozpocznie się instalacja")
            label.setStyleSheet("font: 40px Times New Roman;  color: "+textcolor1)
            layoutinstalacji.addWidget(label)
            
            progress.setGeometry(10,10,500,50)
            layoutinstalacji.addWidget(progress)

            response = requests.get(globalURL+"files/menedzer_dodatki.php")
            data = response.text
            Titles_text = "Lista dodatków, które zostaną zainstalowane: \n"
            for i in data.split(';'):
                if i=="":
                    break
                word = i.split('$')
                addonsVer = (word[6].split(' '))[1]
                #print(addonsVer)
                BollFlag = False
                for o in Ids.split(','):
                    #print(o, word[0])
                    if int(word[0]) == int(o):
                        BollFlag = True
                #print(BollFlag)
                if addonsVer == version and BollFlag:
                    
                    Titles_text = Titles_text+' '+word[1].replace("<q>", "").replace("</q>", "")+",\n"
            if(Titles_text[len(Titles_text)-2:]) == ',\n':
                Titles_text = Titles_text[:len(Titles_text)-2]
            Titles = QLabel(Titles_text)
            #print(Titles_text)
            Titles.setStyleSheet("Font: 18px; color: "+textcolor1)
            layoutinstalacji.addWidget(Titles)



            layoutV.addLayout(layoutinstalacji)

            #progress.setValue(50)
            inscription2 = QLabel(self)
            inscription2.setText(CopyrightText)
            inscription2.setStyleSheet("font: 25pt Times New Roman;  color: "+textcolor1+"; text-align: center; width: 1200px; text-align: jutify")
            HelpingLayout = QHBoxLayout()
            HelpingLayout.addWidget(inscription2)
            version = QLabel("Menedżer nieoficjalnych dodatków v."+versionMenedzer)
            version.setStyleSheet("font: 15pt Times New Roman;  color: "+textcolor1+"; text-align: center;")
            HelpingLayout.addWidget(version)
            #HelpingLayout.addSpacing(50)
            layoutV.addLayout(HelpingLayout)


        




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = menedzer()
sys.exit(app.exec_())