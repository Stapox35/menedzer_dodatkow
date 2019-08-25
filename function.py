import os
import requests
import datetime
def TakeMyVersion(root, globalURL):
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

def IsInstall(root, id):
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

def TakeInstallDate(root, id):
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

def TakePathSimulator():
    root = os.getcwd()
    path = root+"/.config_men.ini"
    ini = open(path, "r")
    for linijka in ini.readlines():
        linijka = linijka.replace("\n", "")
        if linijka[:2] == "-p":
            path = linijka[3:]
            path = path.replace(";", "")
            return path


def TakePath7z():
    root = os.getcwd()
    path = root+"/.config_men.ini"
    ini = open(path, "r")
    for linijka in ini.readlines():
        linijka = linijka.replace("\n", "")
        if linijka[:2] == "-z":
            path = linijka[3:]
            path = path.replace(";", "")
            return path


def CheckPathSimulator(path_simulator_root):
    MaszynaBool = True
    print(path_simulator_root)
    if not os.path.isdir(path_simulator_root+"/dynamic"):
        MaszynaBool = False
    if not os.path.isdir(path_simulator_root+"/textures"):
        MaszynaBool = False
    if not os.path.isdir(path_simulator_root+"/scenery"):
        MaszynaBool = False
    return MaszynaBool

def CheckInstallAddons(path_simulator_root, globalURL, path_program_root):
    log = open(path_program_root+"/log_men.txt", "a")
    log.write("Check install add-ons!\n")
    root = os.getcwd()
    x = datetime.datetime.now()
    path_simulator_root = str(path_simulator_root)
    path = root+"/.config_men.ini"
    ini = open(path, "a", encoding="utf-8")
    response = requests.get(globalURL+"files/menedzer_dodatki.php")
    data = response.text
    data = data.replace("<br>", "")
    data = data.replace("<br/>", "")
    data = data.replace("<br />", "")
    data = data.split(';')
    for i in data:
        auxiliaryVariable = i.split("$")
        CurrentId = int(auxiliaryVariable[0])
        log.write("Active addons id: "+str(CurrentId)+"\n")
        adresRI = auxiliaryVariable[10]
        log.write("RI path: "+str(adresRI)+"\n")
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
                    print(path_simulator_root+"/"+path)
                    log.write(path_simulator_root+"/"+path)

                    if not os.path.isfile(path_simulator_root+"/"+path):
                        ThisIdBool = False  
                        log.write("  not\n")
                    else: 
                        log.write("  check\n")
            if o[:8] == "[VERIFY]":
                VerifyBool = True
        if ThisIdBool == True:
            ini.write("-a "+str(CurrentId)+"$"+str(1)+"$"+str(x)+";\n")
            log.write("Check this addons\n")
            log.write("-a "+str(CurrentId)+"$"+str(1)+"$"+str(x)+";\n")
        else: 
            log.write("not all files!\n")
        if CurrentId == 1:
            break
    ini.close()
    log.close()
