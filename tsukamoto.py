import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#variabel
suhu = np.arange(0, 60, 1)
kelembapan = np.arange(0, 150, 1)
kecepatan = np.arange(0, 250, 1)

#range himpunan fuzzy dari grafik
suhu_dingin = fuzz.trapmf(suhu, [0, 0, 20, 40])
suhu_panas = fuzz.trapmf(suhu, [20, 40, 60, 60])
kelembapan_kering = fuzz.trapmf(kelembapan, [0, 0, 50, 100])
kelembapan_basah = fuzz.trapmf(kelembapan, [50, 100, 150, 150])
kecepatan_lambat = fuzz.trapmf(kecepatan, [0, 0, 50, 200])
kecepatan_cepat = fuzz.trapmf(kecepatan, [50, 200, 250, 250])

# Menentukan Input
input_suhu = float(input("Masukkan suhu (20-40): "))
input_kelembapan = float(input("Masukkan kelembapan (50-100): "))

# Menentukan Derajat Keanggotaan (fuzzifikasi)
x = []
x.append(fuzz.interp_membership(suhu, suhu_dingin, input_suhu))
x.append(fuzz.interp_membership(suhu, suhu_panas, input_suhu))

y = []
y.append(fuzz.interp_membership(kelembapan, kelembapan_kering, input_kelembapan))
y.append(fuzz.interp_membership(kelembapan, kelembapan_basah, input_kelembapan))

print("==========================")
print("Derajat Keanggotaan suhu")
if x[0] > 0:
    print("Dingin: " + str(x[0]))
if x[1] > 0:
    print("Panas: " + str(x[1]))
print("Derajat Keanggotaan kelembapan")
if y[0] > 0:
    print("Kering: " + str(y[0]))
if y[1] > 0:
    print("Basah: " + str(y[1]))


# Memodelkan Rule Base dan Inferensi Tsukamoto

#(z-50)/(250-50) = apred[i] ->cepat
# z-50 = apred * 200
# z = (apred *200) + 50

#(50-z)/(250-50) = apred[i] ->lambat
# 50 -z = apred * 200
# -z = (apred * 200) -50
# z = 50 - (apred * 200)

apred1 = np.fmin(x[1], y[1])
print("\n==========================")
print("Cepat, Nilai apred1 = ", apred1)
z1 = (apred1 * 150) + 50
print("Nilai z1 = ", z1)

apred2 = np.fmin(x[0], y[0])
print("Lambat, Nilai apred2 = ", apred2)
z2 = 50 - (apred2 * 150)
print("Nilai z2 = ", z2)

apred3 = np.fmin(x[0], y[1])
print("Lambat, Nilai apred3 = ", apred3)
z3 = 50 - (apred3 * 150)
print("Nilai z3 = ", z3)

apred4 = np.fmin(x[1], y[0])
print("Cepat, Nilai apred4 = ", apred4)
z4 = (apred4 * 150) + 50
print("Nilai z4 = ", z4)

# Menggabungkan aturan-aturan dengan operasi maksimum
output_combined = np.maximum(np.maximum(z1, z2), np.maximum(z3, z4))

# Defuzzifikasi menggunakan metode Tsukamoto
z = np.sum(output_combined * output_combined) / np.sum(output_combined)

# Menampilkan hasil output
print("==========================")
print("Output:")
print("Kecepatan Kipas:", z)

if z >= 150:
    print("Kondisi: Cepat")
else:
    print("Kondisi: Lambat")

# Mengatur plot dan kurva
plt.figure()

# Menampilkan fungsi keanggotaan suhu
plt.plot(suhu, suhu_dingin, 'r', label='Dingin')
plt.plot(suhu, suhu_panas, 'b', label='Panas')
plt.axvline(x=input_suhu, color='g', linestyle='--', label='Input Suhu')
plt.legend()

# Menampilkan fungsi keanggotaan kelembapan
plt.figure()
plt.plot(kelembapan, kelembapan_kering, 'r', label='Kering')
plt.plot(kelembapan, kelembapan_basah, 'b', label='Basah')
plt.axvline(x=input_kelembapan, color='g', linestyle='--', label='Input Kelembapan')
plt.legend()

# Menampilkan grafik output kecepatan kipas
plt.figure()
plt.plot(kecepatan, kecepatan_lambat, 'r', label='Lambat')
plt.plot(kecepatan, kecepatan_cepat, 'b', label='Cepat')

if(z>=150):
    output_membership = fuzz.interp_membership(kecepatan, kecepatan_cepat, z)
    plt.plot(z, fuzz.interp_membership(kecepatan, kecepatan_cepat, z), 'ko', label='Output')
elif(z<150):
    output_membership = fuzz.interp_membership(kecepatan, kecepatan_lambat, z)
    plt.plot(z, fuzz.interp_membership(kecepatan, kecepatan_lambat, z), 'ko', label='Output')
plt.annotate(f"z = {z}", (z, output_membership), textcoords="offset points", xytext=(0,10), ha='center')
plt.legend()

# Menampilkan grafik
plt.show()