# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:40:22 2020

@author: ASUS
"""

import shapefile  # megimport library shapefile
w=shapefile.Writer("soal1") # inisialiasi untuk Membuat file shapefile baru menggunakan Writer dan membuat oject baru
w.shapeType # Untuk menentukan shapeType nya

w.field("kolom1","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom1 Type Character
w.field("kolom2","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom2 Type Character 

w.record("ngek","satu") # Untuk mengisi field yang sudah dibuat 
w.record("ngok","dua") # Untuk mengisi field yang sudah dibuat 

w.point(1,1) # untuk mengisi data point sebagai koordinat dimana x = 1 dan y = 1
w.point(2,2) # untuk mengisi data point sebagai koordinat dimana x = 2 dan y = 2

w.close() # menutup perintah