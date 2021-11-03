# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:16:44 2020

@author: ASUS
"""
print(1184042 % 8)
import shapefile # mengimport library shapefile
w=shapefile.Writer("soal10", shapeType=shapefile.POLYGON) # inisialiasi untuk Membuat file shapefile baru menggunakan Writer dan membuat oject baru
w.shapeType # menentukan shapeType nya

w.field("kolom1","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom1 Type Character
w.field("kolom2","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom2 Type Character

w.record("parhan","hambali") # Untuk mengisi field yang sudah dibuat
w.record("real","madrid") # Untuk mengisi field yang sudah dibuat
w.record("gratis","ongkir") # Untuk mengisi field yang sudah dibuat
w.record("shoope","tokopedia") # Untuk mengisi field yang sudah dibuat

w.poly([[[1,1],[5,1], [5,5],[1,5], [1,1]]])  # Untuk mengisi data poly sesuai koordinat masing - masing x dan y
w.poly([[[6,1],[10,1], [10,5],[6,5], [6,1]]])  # Untuk mengisi data poly sesuai koordinat masing - masing x dan y
w.poly([[[1,6],[5,6], [5,10],[1,10], [1,6]]])  # Untuk mengisi data poly sesuai koordinat masing - masing x dan y
w.poly([[[6,6],[10,6], [10,10],[6,10], [6,6]]])  # Untuk mengisi data poly sesuai koordinat masing - masing x dan y

w.close() # menutup perintah

