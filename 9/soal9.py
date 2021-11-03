# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:15:39 2020

@author: ASUS
"""

import shapefile # mengimport library shapefile
w=shapefile.Writer("soal9", shapeType=shapefile.POLYGON) # inisialiasi untuk Membuat file shapefile baru menggunakan Writer dan membuat oject baru
w.shapeType # menentukan shapeType nya

w.field("kolom1","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom1 Type Character
w.field("kolom2","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom2 Type Character

w.record("ngek","satu") # Untuk mengisi field yang sudah dibuat
w.record("crot","dua") # untuk mengisi field yang sudah dibuat 

w.poly([[[1,3],[5,3], [5,2],[1,2], [1,3]]]) # Untuk mengisi data poly sesuai koordinat masing - masing x dan y
w.poly([[[1,6],[5,6], [5,9],[1,9], [1,6]]]) # Untuk mengisi data poly sesuai koordinat masing - masing x dan y

w.close() # menutup perintah