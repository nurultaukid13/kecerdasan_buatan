import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Dataset
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

# Input variables
suhu = ctrl.Antecedent(np.arange(20, 41, 1), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembaban')

# Output variable
kecepatan_kipas = ctrl.Consequent(np.arange(0, 186, 1), 'kecepatan_kipas')

# Fuzzy membership functions
suhu['dingin'] = fuzz.trapmf(suhu.universe, [20, 20, 25, 30])
suhu['hangat'] = fuzz.trimf(suhu.universe, [25, 30, 35])
suhu['panas'] = fuzz.trapmf(suhu.universe, [30, 35, 40, 40])

kelembaban['kering'] = fuzz.trapmf(kelembaban.universe, [0, 0, 25, 50])
kelembaban['normal'] = fuzz.trimf(kelembaban.universe, [25, 50, 75])
kelembaban['basah'] = fuzz.trapmf(kelembaban.universe, [50, 75, 100, 100])

kecepatan_kipas['lambat'] = fuzz.trapmf(kecepatan_kipas.universe, [0, 0, 62, 124])
kecepatan_kipas['sedang'] = fuzz.trimf(kecepatan_kipas.universe, [62, 124, 185])
kecepatan_kipas['cepat'] = fuzz.trapmf(kecepatan_kipas.universe, [124, 185, 185, 185])

# Rules
rule1 = ctrl.Rule(suhu['dingin'] & kelembaban['kering'], kecepatan_kipas['lambat'])
rule2 = ctrl.Rule(suhu['dingin'] & kelembaban['normal'], kecepatan_kipas['lambat'])
rule3 = ctrl.Rule(suhu['dingin'] & kelembaban['basah'], kecepatan_kipas['lambat'])
rule4 = ctrl.Rule(suhu['hangat'] & kelembaban['kering'], kecepatan_kipas['sedang'])
rule5 = ctrl.Rule(suhu['hangat'] & kelembaban['normal'], kecepatan_kipas['sedang'])
rule6 = ctrl.Rule(suhu['hangat'] & kelembaban['basah'], kecepatan_kipas['cepat'])
rule7 = ctrl.Rule(suhu['panas'] & kelembaban['kering'], kecepatan_kipas['sedang'])
rule8 = ctrl.Rule(suhu['panas'] & kelembaban['normal'], kecepatan_kipas['cepat'])
rule9 = ctrl.Rule(suhu['panas'] & kelembaban['basah'], kecepatan_kipas['cepat'])


# Control system
pengendali_kipas = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
pengendali = ctrl.ControlSystemSimulation(pengendali_kipas)

# Process dataset
kecepatan = []
for data in dataset:
    suhu_input, kelembaban_input = data
    pengendali.input['suhu'] = suhu_input
    pengendali.input['kelembaban'] = kelembaban_input

    # Start the simulation
    pengendali.compute()

    # Get the resulting fan speed
    kecepatan.append(pengendali.output['kecepatan_kipas'])

# Calculate accuracy
target_kecepatan = [55, 55, 55, 55, 161.75, 129.77, 165.07, 165.06, 14.76, 12.5, 102.92, 164.56]
akurasi = 100 - (np.mean(np.abs(np.subtract(target_kecepatan, kecepatan))) / np.mean(target_kecepatan) * 100)

print("Hasil kecepatan kipas:")
print(kecepatan)
print("Akurasi: {}%".format(akurasi))