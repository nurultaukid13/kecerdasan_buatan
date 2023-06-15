import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#variabel
suhu = np.arange(20, 41, 1)
kelembapan = np.arange(0, 101, 1)
kecepatan = np.arange(0, 186, 1)

#range himpunan fuzzy dari grafik
suhu_dingin = fuzz.trapmf(suhu, [20, 20, 25, 30])
suhu_hangat = fuzz.trimf(suhu, [25, 30, 35])
suhu_panas = fuzz.trapmf(suhu, [30, 35, 40, 40])

kelembapan_kering = fuzz.trapmf(kelembapan, [0, 0, 25, 50])
kelembapan_normal = fuzz.trimf(kelembapan, [25, 50, 75])
kelembapan_basah = fuzz.trapmf(kelembapan, [50, 75, 100, 100])

kecepatan_lambat = fuzz.trapmf(kecepatan, [0, 0, 62, 124])
kecepatan_sedang = fuzz.trimf(kecepatan, [62, 124, 185])
kecepatan_cepat = fuzz.trapmf(kecepatan, [124, 185, 185, 185])

# Looping untuk setiap data di dataset
input_suhu = 25.6
input_kelembapan = 96.3

# Menentukan Derajat Keanggotaan (fuzzifikasi)
x = []
x.append(fuzz.interp_membership(suhu, suhu_dingin, input_suhu))
x.append(fuzz.interp_membership(suhu, suhu_hangat, input_suhu))
x.append(fuzz.interp_membership(suhu, suhu_panas, input_suhu))

y = []
y.append(fuzz.interp_membership(kelembapan, kelembapan_kering, input_kelembapan))
y.append(fuzz.interp_membership(kelembapan, kelembapan_normal, input_kelembapan))
y.append(fuzz.interp_membership(kelembapan, kelembapan_basah, input_kelembapan))

print("==========================")
print("Derajat Keanggotaan suhu")
if x[0] > 0:
    print("Dingin: " + str(round(x[0], 3)))
if x[1] > 0:
    print("Hangat: " + str(round(x[1], 3)))
if x[2] > 0:
    print("Panas: " + str(round(x[2], 3)))
print("Derajat Keanggotaan kelembapan")
if y[0] > 0:
    print("Kering: " + str(round(y[0], 3)))
if y[1] > 0:
    print("Normal: " + str(round(y[1], 3)))
if y[2] > 0:
    print("Basah: " + str(round(y[2], 3)))


# Memodelkan Rule Base dan Inferensi Tsukamoto

#z = (apred[i] * (z2 - z1)) + z1 ->cepat
# z = (apred[i] * (124-0))+0
# z = (apred *124)

#z = (apred[i] * (z2 - z1)) + z1 ->sedang
#z = (apred[i] * (185-62)) +62
#z = (apred[i] * 123)+62

#z = (apred[i] * (z2 - z1)) + z1->lambat
#z = (apred[i] * (185-124))+124
#z = (apred[i] * 61))+124

apred1 = np.fmin(x[0], y[0])
print("\n==========================")
print("Lambat, Nilai apred1 =", round(apred1, 3))
z1 = round((apred1 * 61)+124, 3)
print("Nilai z1 =", z1)

apred2 = np.fmin(x[0], y[1])
print("Lambat, Nilai apred2 =", round(apred2, 3))
z2 = round((apred2 * 61)+124, 3)
print("Nilai z2 =", z2)

apred3 = np.fmin(x[0], y[2])
print("Lambat, Nilai apred3 =", round(apred3, 3))
z3 = round((apred3 * 61)+124, 3)
print("Nilai z3 =", z3)

apred4 = np.fmin(x[1], y[0])
print("Sedang, Nilai apred4 =", round(apred4, 3))
z4 = round((apred4 * 123)+62, 3)
print("Nilai z4 =", z4)

apred5 = np.fmin(x[1], y[1])
print("Sedang, Nilai apred4 =", round(apred5, 3))
z5 = round((apred5 * 123)+62, 3)
print("Nilai z5 =", z5)

apred6 = np.fmin(x[1], y[2])
print("Cepat, Nilai apred6 =", round(apred6, 3))
z6 = round((apred6 * 124), 3)
print("Nilai z6 =", z6)

apred7 = np.fmin(x[2], y[0])
print("Sedang, Nilai apred7 =", round(apred7, 3))
z7 = round((apred7 * 123)+62, 3)
print("Nilai z7 =", z7)

apred8 = np.fmin(x[2], y[1])
print("Cepat, Nilai apred8 =", round(apred8, 3))
z8 = round((apred8 * 124), 3)
print("Nilai z8 =", z8)

apred9 = np.fmin(x[2], y[2])
print("Cepat, Nilai apred9 =", round(apred9, 3))
z9 = round((apred9 * 124), 3)
print("Nilai z9 =", z9)

# Menggabungkan aturan-aturan dengan operasi maksimum
output_combined = np.maximum.reduce([z1, z2, z3, z4, z5, z6, z7, z8, z9])

# Defuzzifikasi menggunakan metode Tsukamoto
z = np.sum(output_combined * output_combined) / np.sum(output_combined)

# Menampilkan hasil output
print("==========================")
print("Output:")
print("Kecepatan Kipas:", z)

if z <= 185 and z>124:
    print("Kondisi: Cepat")
elif z >= 60 and z <= 124:
    print("Kondisi: Sedang")
else:
    print("Kondisi: Lambat")
