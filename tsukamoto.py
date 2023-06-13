import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#variabel
suhu = np.arange(20, 40, 1)
kelembapan = np.arange(0, 150, 1)
kecepatan = np.arange(0, 185, 1)

#range himpunan fuzzy dari grafik
suhu_dingin = fuzz.trapmf(suhu, [20, 20, 25, 30])
suhu_panas = fuzz.trapmf(suhu, [25, 30, 40, 40])
kelembapan_kering = fuzz.trapmf(kelembapan, [0, 0, 50, 100])
kelembapan_basah = fuzz.trapmf(kelembapan, [50, 100, 150, 150])
kecepatan_lambat = fuzz.trapmf(kecepatan, [0, 0, 62, 124])
kecepatan_cepat = fuzz.trapmf(kecepatan, [62, 124, 185, 185])

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
    print("Dingin: " + str(round(x[0], 3)))
if x[1] > 0:
    print("Panas: " + str(round(x[1], 3)))
print("Derajat Keanggotaan kelembapan")
if y[0] > 0:
    print("Kering: " + str(round(y[0], 3)))
if y[1] > 0:
    print("Basah: " + str(round(y[1], 3)))


# Memodelkan Rule Base dan Inferensi Tsukamoto

#(z-0)/(185-0) = apred[i] ->cepat
# z-10 = apred * 185
# z = (apred *185)+ 0

#(0-z)/(185-0) = apred[i] ->lambat
# 0 -z = apred * 185
# -z = (apred * 185)
# z = -(apred * 185)

apred1 = np.fmin(x[1], y[1])
print("\n==========================")
print("Cepat, Nilai apred1 =", round(apred1, 3))
z1 = round((apred1 * 185), 3)
print("Nilai z1 =", z1)

apred2 = np.fmin(x[0], y[0])
print("Lambat, Nilai apred2 =", round(apred2, 3))
z2 = round(- (apred2 * 185), 3)
print("Nilai z2 =", z2)

apred3 = np.fmin(x[0], y[1])
print("Lambat, Nilai apred3 =", round(apred3, 3))
z3 = round(10- (apred3 * 185), 3)
print("Nilai z3 =", z3)

apred4 = np.fmin(x[1], y[0])
print("Cepat, Nilai apred4 =", round(apred4, 3))
z4 = round((apred4 * 185), 3)
print("Nilai z4 =", z4)

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