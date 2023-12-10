# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:08:16 2023

@author: Dafasyah Adinata
"""

def hitung_jumlah_hari(bulan, tahun):

    if bulan == 2:
    
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

# Input bulan dan tahun dari pengguna
bulan = int(input("Masukkan nomor bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

while bulan < 1 or bulan > 12:
    print("Nomor bulan tidak valid. Silakan masukkan nomor bulan yang benar.")
    bulan = int(input("Masukkan nomor bulan (1-12): "))

jumlah_hari = hitung_jumlah_hari(bulan, tahun)
print(f"Jumlah hari dalam bulan {bulan} tahun {tahun}: {jumlah_hari} hari.")
