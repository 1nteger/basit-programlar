#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os , sqlite3
path = os.getcwd()
con = sqlite3.connect("{}/veritabani.db".format(path))
con.row_factory = sqlite3.Row
cur = con.cursor()
if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")
try:
    cur.execute("CREATE TABLE tablo(komut TEXT, cevap TEXT)")
    con.commit()
except:
    pass
while True:
    x = input("Komutu giriniz:")
    x = x.replace("I","ı")
    x = x.replace("İ","i")
    x = x.lower()
    if x == "kapat":
        break
    komutlar = cur.execute("SELECT komut,cevap FROM tablo")
    y = False
    for i in komutlar.fetchall():
        if i["komut"] == x:
            print(i["cevap"])
            input("Devam etmek için herhangi bir tuşa basınız...")
            y = True
    if y == False:
        z = input("Bu komut girildiğinde verilmesini istediğiniz cevabı giriniz:")
        z = z.replace("I","ı")
        z = z.replace("İ","i")
        z = z.lower()
        cur.execute("INSERT INTO tablo(komut,cevap) VALUES('{}','{}')".format(x,z))
        print("Komut başarıyla eklendi!")
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
input("Program sonlandırıldı...")
if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")
con.close()
