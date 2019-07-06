import os
import requests

def sprawdzwersje(root, globalURL):
    path_rev = root+"/rev.ini"
    if os.path.isfile(path_rev):
        plik = open(path_rev, "r")
        aktualny_rev = plik.read()
        aktualny_rev = aktualny_rev.replace(" ", "")
        aktualny_rev = aktualny_rev.replace("\n", "")
        plik.close()
        response = requests.get(globalURL+"files/config_menedzer_serwer.ini")
        data = response.text
        flagaoprojekcie = True
        text = data.split('\n')
        textpl = ""
        for s in text:
            if flagaoprojekcie:
                if s == "[OP]":
                    flagaoprojekcie = False
                    break
                textpl = textpl+' '+s
        textpl = textpl.replace("[REV]", "")
        textpl = textpl.replace(" ", "")
        textpl = textpl.replace('"', "")
        textpl = textpl.split(';')
        for i in textpl:
            i = i.split("=")
            if i[0] == aktualny_rev:
                return i[1]
        return -1    
    else:
        return -1

'''
Klucze
1-lok ele
2-lok spal
3-lok par
4-wagony os
5-wagony tow
6-pojazdy specjalne
7-scenerie (?)
8-EZT
9-SZT
10-wagony akumulatorowe
11-wagony motorowe
'''

def SprawdzCzyZainstalowany(root, id):
    root = os.getcwd()
    path = root+"/.config_men.ini"
    ini = open(path, "r")
    for linijka in ini.readlines():
        linijka = linijka.replace("\n", "")
        if linijka[:2] == "-a":
            wpiszrodlowy = linijka[3:]
            id1 = int(wpiszrodlowy.split("$")[0])
            if id1 == int(id):
                if int(wpiszrodlowy.split("$")[1]) == 1:
                    return True #zablokowane
    return False 

def PodajDateInstalacji(root, id):
    root = os.getcwd()
    path = root+"/.config_men.ini"
    ini = open(path, "r")
    for linijka in ini.readlines():
        linijka = linijka.replace("\n", "")
        if linijka[:2] == "-a":
            wpiszrodlowy = linijka[3:]
            id1 = int(wpiszrodlowy.split("$")[0])
            if id1 == int(id):
                return str(wpiszrodlowy.split("$")[2]).replace(";", "")

def PodajSciezkeSymulatora():
    root = os.getcwd()
    path = root+"/.config_men.ini"
    ini = open(path, "r")
    for linijka in ini.readlines():
        linijka = linijka.replace("\n", "")
        if linijka[:2] == "-p":
            path = linijka[3:]
            path = path.replace(";", "")
            return path