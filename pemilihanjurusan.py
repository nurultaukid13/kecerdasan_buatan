def nilai_akademik():

    mata_pelajaran = {
        "Apakah kamu memiliki nilai matematika yang bagus?": {
            "ya": "Apakah kamu memiliki nilai fisika yang bagus?",
            "tidak": "Apakah kamu memiliki nilai seni yang bagus?"
        },
        "Apakah kamu memiliki nilai fisika yang bagus?": {
            "ya": "fisika",
            "tidak": "Apakah kamu memiliki nilai kimia yang bagus?"
        },
        "Apakah kamu memiliki nilai kimia yang bagus?": {
            "ya": "kimia",
            "tidak": "Apakah kamu memiliki nilai ekonomi yang bagus?"
        },
        "Apakah kamu memiliki nilai ekonomi yang bagus?": {
            "ya": "ekonomi",
            "tidak": "matematika"
        },
        "Apakah kamu memiliki nilai seni yang bagus?": {
            "ya": "seni",
            "tidak": "Apakah kamu memiliki nilai pkn yang bagus?"
        },
        "Apakah kamu memiliki nilai pkn yang bagus?": {
            "ya": "pkn",
            "tidak": "Apakah kamu memiliki nilai bahasa yang bagus?"
        },
        "Apakah kamu memiliki nilai bahasa yang bagus?": {
            "ya": "bahasa",
            "tidak": "Apakah kamu memiliki nilai biologi yang bagus?"
        },
        "Apakah kamu memiliki nilai biologi yang bagus?": {
            "ya": "biologi",
            "tidak": "Maaf kami tidak bisa merekomendasikan jurusan apapun"
        }
    }

    pertanyaan = "Apakah kamu memiliki nilai matematika yang bagus?"
    while pertanyaan in mata_pelajaran:
        jawaban = input(pertanyaan + " (ya/tidak) ")
        pertanyaan = mata_pelajaran[pertanyaan][jawaban] if jawaban in mata_pelajaran[pertanyaan] else None
        if pertanyaan and pertanyaan != "Maaf kami tidak bisa merekomendasikan jurusan apapun":
            nilai_akademik = pertanyaan

    return nilai_akademik

def minat(nilai):
    pertanyaan = {
        "matematika": [
            {"teknologi":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan teknologi ? (ya/tidak) "},
            {"bisnis": "Apakah kamu menyukai kegiatan yang berhubungan langsung dengan bisnis ? (ya/tidak) "},
            {"kontruksi":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan kontruksi ? (ya/tidak) "}
        ],
        "fisika": [
            {"murni": "Apakah kamu menyukai kegiatan yang berhubungan dengan fisika secara teori (murni) ? (ya/tidak) "},
            {"kontruksi":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan kontruksi ? (ya/tidak) "}
        ],
        "kimia": [
            {"bioproses":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan pabrik kimia atau bioproses ? (ya/tidak) "},
            {"lingkungan": "Apakah kamu menyukai kegiatan yang berhubungan pemanfaatan sumber daya alam ? (ya/tidak) "}
        ],
        "ekonomi": [
            {"bisnis": "Apakah kamu menyukai kegiatan yang berhubungan dengan bisnis secara langsung ? (ya/tidak) "},
            {"administrasi":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan administrasi? (ya/tidak) "}
        ],
        "seni": [
            {"kontruksi":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan kontruksi? (ya/tidak) "},
            {"teknologi":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan teknologi? (ya/tidak) "},
            {"ilmu_sosial":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan ilmu sosial? (ya/tidak) "}
        ],
        "pkn": [
            {"hukum": "Apakah kamu menyukai kegiatan yang berhubungan dengan hukum? (ya/tidak) "},
            {"ilmu_sosial": "Apakah kamu menyukai kegiatan yang berhubungan dengan ilmu sosial? "}
        ],
        "bahasa": [
            {"ilmu_sosial": "Apakah kamu menyukai kegiatan yang berhubungan dengan ilmu sosial? "},
            {"bisnis": "Apakah kamu menyukai kegiatan yang berhubungan langsung dengan bisnis ? (ya/tidak) "}
        ],
        "biologi": [
            {"pertanian":
                "Apakah kamu menyukai kegiatan yang berhubungan dengan pertanian ? (ya/tidak) "},
            {"lingkungan":
                "Apakah kamu menyukai kegiatan yang berhubungan pemanfaatan sumber daya alam  ? (ya/tidak) "}
        ]
    }
    minat = []
    for pilihan in pertanyaan.get(nilai):
        for bidang, text in pilihan.items():
            while True:
                jawaban = input(text)
                if jawaban == "ya":
                    minat.append(bidang)
                    break
                elif jawaban == "tidak":
                        break
                else:
                    print("Jawaban tidak valid, silakan masukkan 'ya' atau 'tidak'")
    if minat:
        return minat
    else:
        print("Maaf anda mungkin harus mengulangi di tahap nilai akademik karena tidak memiliki minat di bidang " + nilai)
        return ["ulang"]
    
def bakat(nilai, minat):
    if nilai == "matematika":
        if "teknologi" in minat and "bisnis" not in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="logika"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="agro"
            else:
                bakat = "ulang"

        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="logika"
            elif input("Apakah kamu memiliki kemampuan untuk mengelola waktu dengan baik dan mampu mengatur jadwal dengan efektif? (ya/tidak)") =="ya":
                bakat ="administrasi"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="agro"
            elif input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat??? (ya/tidak)") == "ya":
                bakat ="manajemen"
            else:
                bakat = "ulang"
                
        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="logika"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="agro"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            else:
                bakat = "ulang"
        
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="agro"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            else:
                bakat = "ulang"
                
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat??? (ya/tidak)") == "ya":
                bakat ="manajemen"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="agro"
            else:
                bakat = "ulang"
                
        elif "teknologi" not in minat and "bisnis" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            else:
                bakat = "ulang"
                
        elif "teknologi" in minat and "bisnis" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            elif input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="logika"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="agro"
            else:
                bakat = "ulang"
                
    elif nilai == "fisika":
        if "murni" in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan menyelesaikan permasalahan fisika secara toeristis? (ya/tidak) ") == "ya":
                bakat ="fisika"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            else:
                bakat = "ulang"
        
        elif "murni" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan menyelesaikan permasalahan fisika secara toeristis? (ya/tidak) ") == "ya":
                bakat ="fisika"
            else:
                bakat = "ulang"
        
        elif "murni" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="teknis"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="desain"
            else:
                bakat = "ulang"
                
    elif nilai == "kimia":
        if "bioproses" in minat and "lingkungan" in minat:
            if input("Apakah kamu memiliki kemampuan memproses zat kimia untuk bahan industri? (ya/tidak) ") == "ya":
                bakat ="tek_kimia"
            elif input("Apakah kamu memiliki kemampuan memanajemen produksi dan operasional industri? (ya/tidak) ") == "ya":
                bakat ="tek_industri"
            elif input("Apakah kamu mempunyai kemampuan untuk penanganan limbah industri? (ya/tidak)") == "ya":
                bakat ="tek_lingkungan"
            elif input("Apakah kamu mempunyai kemampuan untuk pengolahan dan penilitian produk pangan? (ya/tidak)") == "ya":
                bakat ="tek_pangan"
            else:
                bakat = "ulang"
        
        elif "bioproses" in minat and "lingkungan" not in minat:
            if input("Apakah kamu memiliki kemampuan memproses zat kimia untuk bahan industri? (ya/tidak) ") == "ya":
                bakat ="tek_kimia"
            elif input("Apakah kamu memiliki kemampuan memanajemen produksi dan operasional industri? (ya/tidak) ") == "ya":
                bakat ="tek_industri"
            else:
                bakat = "ulang"
                
        elif "bioproses" not in minat and "lingkungan" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk penanganan limbah industri? (ya/tidak)") == "ya":
                bakat ="tek_lingkungan"
            elif input("Apakah kamu mempunyai kemampuan untuk pengolahan dan penilitian produk pangan? (ya/tidak)") == "ya":
                bakat ="tek_pangan"
            else:
                bakat = "ulang"
        
    if(bakat == "ulang"):
        pesan = "Maaf anda mungkin harus mengulangi di tahap minat karena tidak memiliki bakat di bidang "
        if len(minat) == 1:
            pesan += minat[0]
        else:
            for i, nama in enumerate(minat):
                if i == len(minat) - 1:
                    pesan += "dan " + nama
                else:
                    pesan += nama + ", "
        print(pesan)
    
    return bakat


nilai=nilai_akademik()
minat= minat(nilai)
bakat(nilai, minat)
