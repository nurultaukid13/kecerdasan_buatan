import numpy as np
import skfuzzy as fuzz

# Fuzzifikasi variabel masukan
suhu = np.arange(20, 41, 1)
kelembaban = np.arange(0, 101, 1)
kecepatan = np.arange(0, 186, 1)

# Pembentukan fungsi keanggotaan suhu
suhu_rendah = fuzz.trapmf(suhu,[20, 20, 25, 30])
suhu_normal = fuzz.trimf(suhu, [25, 30, 35])
suhu_tinggi = fuzz.trapmf(suhu, [30, 35, 40, 40])

# Pembentukan fungsi keanggotaan kelembaban
kelembaban_kering = fuzz.trapmf(kelembaban, [0, 0, 25, 50])
kelembaban_normal = fuzz.trimf(kelembaban, [25, 50, 75])
kelembaban_basah = fuzz.trapmf(kelembaban, [50, 75, 100, 100])

# Pembentukan fungsi keanggotaan tingkat penyakit
kecepatan_lambat = fuzz.trapmf(kecepatan, [0, 0, 46.25, 92.5])
kecepatan_sedang = fuzz.trimf(kecepatan, [46.25, 92.5, 138.75])
kecepatan_cepat = fuzz.trapmf(kecepatan, [92.5, 138.75, 185, 185])

# Definisi dataset
dataset = [
    [25.6, 96.3],
    [23, 93.6],
    [28.3, 84.5],
    [28.6, 82.5],
    [29.4, 78],
    [33.7, 56.8],
    [38.1, 64],
    [35.8, 60.7],
    [21.7, 99.9],
    [20.6, 99.9],
    [32.9, 79.7],
    [29.7, 79.1]
]

# Menghitung jumlah data pada dataset
n_data = len(dataset)

# Inisialisasi variabel hasil
hasil_kecepatan = []

# Melakukan perhitungan fuzzy dan mencetak hasil kecepatan untuk setiap data
for data in dataset:
    suhu_input = data[0]
    kelembaban_input = data[1]
    # Proses fuzzifikasi
    suhu_rendah_degree = fuzz.interp_membership(suhu, suhu_rendah, suhu_input)
    suhu_normal_degree = fuzz.interp_membership(suhu, suhu_normal, suhu_input)
    suhu_tinggi_degree = fuzz.interp_membership(suhu, suhu_tinggi, suhu_input)

    kelembaban_kering_degree = fuzz.interp_membership(
        kelembaban, kelembaban_kering, kelembaban_input)
    kelembaban_normal_degree = fuzz.interp_membership(
        kelembaban, kelembaban_normal, kelembaban_input)
    kelembaban_basah_degree = fuzz.interp_membership(
        kelembaban, kelembaban_basah, kelembaban_input)

    # Inferensi dengan menggunakan metode Tsukamoto
    # Rule 1: IF suhu rendah AND kelembaban kering THEN kecepatan lambat
    rule1 = np.fmin(suhu_rendah_degree, kelembaban_kering_degree)
    kecepatan_output1 = np.fmin(rule1, kecepatan_lambat)

    # Rule 2: IF suhu rendah AND kelembaban normal THEN kecepatan lambat
    rule2 = np.fmin(suhu_rendah_degree, kelembaban_normal_degree)
    kecepatan_output2 = np.fmin(rule2, kecepatan_lambat)

    # Rule 3: IF suhu rendah AND kelembaban basah THEN kecepatan lambat
    rule3 = np.fmin(suhu_rendah_degree, kelembaban_basah_degree)
    kecepatan_output3 = np.fmin(rule3, kecepatan_lambat)

    rule4 = np.fmin(suhu_normal_degree, kelembaban_kering_degree)
    kecepatan_output4 = np.fmin(rule4, kecepatan_sedang)

    rule5 = np.fmin(suhu_normal_degree, kelembaban_normal_degree)
    kecepatan_output5 = np.fmin(rule5, kecepatan_sedang)

    rule6 = np.fmin(suhu_normal_degree, kelembaban_basah_degree)
    kecepatan_output6 = np.fmin(rule6, kecepatan_cepat)

    rule7 = np.fmin(suhu_tinggi_degree, kelembaban_kering_degree)
    kecepatan_output7 = np.fmin(rule7, kecepatan_sedang)

    rule8 = np.fmin(suhu_tinggi_degree, kelembaban_normal_degree)
    kecepatan_output8 = np.fmin(rule8, kecepatan_cepat)

    rule9 = np.fmin(suhu_tinggi_degree, kelembaban_basah_degree)
    kecepatan_output9 = np.fmin(rule9, kecepatan_cepat)

    # Penggabungan output dari semua aturan
    kecepatan_agg = np.fmax(kecepatan_output1,
                            np.fmax(kecepatan_output2,
                                    np.fmax(kecepatan_output3,
                                            np.fmax(kecepatan_output4,
                                                    np.fmax(kecepatan_output5,
                                                            np.fmax(kecepatan_output6,
                                                                    np.fmax(kecepatan_output7,
                                                                            np.fmax(kecepatan_output8,
                                                                                    kecepatan_output9))))))))

    # Defuzzifikasi menggunakan metode Tsukamoto
    kecepatan_defuzz = fuzz.defuzz(kecepatan, kecepatan_agg, 'centroid')
    kecepatan_result = kecepatan_defuzz

    # Menambahkan hasil kecepatan ke dalam variabel hasil
    hasil_kecepatan.append(kecepatan_result)

# Menampilkan hasil kecepatan
for i in range(n_data):
    data = dataset[i]  # Perbarui variabel data dengan data yang sedang diproses
    print("Data", i+1, ":", data)
    print("Hasil kecepatan Menggunakan Metode Tsukamoto =", hasil_kecepatan[i])
    
# Menghitung akurasi
target_kecepatan = [55, 55, 55, 55, 161.75, 129.77, 165.07, 165.06, 14.76, 12.5, 102.92, 164.56]
akurasi = 100 - (np.mean(np.abs(np.subtract(target_kecepatan, hasil_kecepatan))) / np.mean(target_kecepatan) * 100)

# Menampilkan akurasi
print("Akurasi: {}%".format(akurasi))