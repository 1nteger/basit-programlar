#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")
def hash1(x):
    hash1f = x + 26
    hash2f = x + 19
    hash3f = x + 51
    hash4f = x + 74
    if hash1f > 128:
        hash1f = hash1f % 128
    if hash2f > 128:
        hash2f = hash2f % 128
    if hash3f > 128:
        hash3f = hash3f % 128
    if hash4f > 128:
        hash4f = hash4f % 128
    return [hash1f,hash2f,hash3f,hash4f]
def hash2(x):
    hash1f = x + 15
    hash2f = x + 4
    hash3f = x + 94
    hash4f = x + 57
    if hash1f > 128:
        hash1f = hash1f % 128
    if hash2f > 128:
        hash2f = hash2f % 128
    if hash3f > 128:
        hash3f = hash3f % 128
    if hash4f > 128:
        hash4f = hash4f % 128
    return [hash1f,hash2f,hash3f,hash4f]
def hash3(x):
    hash1f = x + 56
    hash2f = x + 1
    hash3f = x + 12
    hash4f = x + 9
    if hash1f > 128:
        hash1f = hash1f % 128
    if hash2f > 128:
        hash2f = hash2f % 128
    if hash3f > 128:
        hash3f = hash3f % 128
    if hash4f > 128:
        hash4f = hash4f % 128
    return [hash1f,hash2f,hash3f,hash4f]
def hash4(x):
    hash1f = x + 72
    hash2f = x + 12
    hash3f = x + 21
    hash4f = x + 1
    if hash1f > 128:
        hash1f = hash1f % 128
    if hash2f > 128:
        hash2f = hash2f % 128
    if hash3f > 128:
        hash3f = hash3f % 128
    if hash4f > 128:
        hash4f = hash4f % 128
    return [hash1f,hash2f,hash3f,hash4f]

harfler = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p', 'ğ', 'ü', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Ğ', 'Ü', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ş', 'İ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Ö', 'Ç', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '-', 'é', '!', "'", '^', '+', '%', '&', '/', '(', ')', '=', '?', '_', '<', '>', '£', '#', '$', '½', '¾', '{', '[', ']', '}', '\\', '|', '~', '.', '·', '×', 'µ', '”', '“', '¢', '»', '«', 'â', 'ß', 'ª', '´', ',', '`', 'ô', 'î', 'û', '←', '₺', ':', ';',"@", ' ', '\t']
x = input("Şifrelenmesini istediğiniz kelimeyi giriniz:")
xx = 0
for i in x:
    xx += harfler.index(i)
if xx > 128:
    xx = xx % 128

hash1 = hash1(xx)
hash2 = hash2(xx)
hash3 = hash3(xx)
hash4 = hash4(xx)
x = ""
for i in hash1:
    x += harfler[i]
for i in hash2:
    x += harfler[i]
for i in hash3:
    x += harfler[i]
for i in hash4:
    x += harfler[i]
print(x)
input("Program sonlandırıldı")
if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")
