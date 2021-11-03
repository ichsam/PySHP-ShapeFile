# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:02:25 2020

@author: ASUS
"""

import shapefile # mengimport library shapefile

w=shapefile.Writer("soal5") # inisialiasi untuk Membuat file shapefile baru menggunakan Writer dan membuat oject baru
w.shapeType # menentukan shapeType nya

w.field("kolom1","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom1 Type Character
w.field("kolom2","C") # untuk membuat dbf nya terlebih dahulu yang berupa kolom2 Type Character

w.record("ngek","satu") # Untuk mengisi field yang sudah dibuat 

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # mengisi data line sesuai koordinat masing masing x dan y

w.close() # menutup perintah
