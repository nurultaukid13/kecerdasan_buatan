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
        ],
        "pkn": [
            {"hukum": "Apakah kamu menyukai kegiatan yang berhubungan dengan hukum? (ya/tidak) "},
            {"ilmu_sosial": "Apakah kamu menyukai kegiatan yang berhubungan dengan ilmu sosial? "}
        ],
        "bahasa": [
            {"ilmu_sosial": "Apakah kamu menyukai kegiatan yang berhubungan dengan ilmu sosial? "}
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
                bakat ="fik"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            else:
                bakat = "ulang"

        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="fik"
            elif input("Apakah kamu memiliki kemampuan untuk mengelola waktu dengan baik dan mampu mengatur jadwal dengan efektif? (ya/tidak)") =="ya":
                bakat ="fisip"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat? (ya/tidak)") == "ya":
                bakat ="feb"
            else:
                bakat = "ulang"
                
        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="fik"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"
        
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"
                
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat??? (ya/tidak)") == "ya":
                bakat ="feb"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            else:
                bakat = "ulang"
                
        elif "teknologi" not in minat and "bisnis" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"
                
        elif "teknologi" in minat and "bisnis" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="fik"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            else:
                bakat = "ulang"
                
    elif nilai == "fisika":
        if "murni" in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan menyelesaikan permasalahan fisika secara toeristis? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"
        
        elif "murni" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan menyelesaikan permasalahan fisika secara toeristis? (ya/tidak) ") == "ya":
                bakat ="ft"
            else:
                bakat = "ulang"
        
        elif "murni" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
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

    elif nilai == "ekonomi":
        if "bisnis" in minat and "administrasi" in minat:
            if input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat?? (ya/tidak) ") == "ya":
                bakat ="feb"
            elif input("Apakah kamu memiliki bakat dalam mengelola keuangan dan membuat laporan keuangan yang akurat? (ya/tidak) ") == "ya":
                bakat ="feb"
            elif input("Apakah kamu memiliki kemampuan dalam mengorganisir tugas dan pekerjaan dengan baik? (ya/tidak)") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam hal manajemen keuangan publik dan pengelolaan anggaran? (ya/tidak)") == "ya":
                bakat ="fisip"
            else:
                bakat = "ulang"
        
        elif "bisnis" in minat and "administrasi" not in minat:
            if input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat?? (ya/tidak) ") == "ya":
                bakat ="feb"
            elif input("Apakah kamu memiliki bakat dalam mengelola keuangan dan membuat laporan keuangan yang akurat? (ya/tidak) ") == "ya":
                bakat ="feb"
            else:
                bakat = "ulang"
                
        elif "bisnis" not in minat and "administrasi" in minat:
            if input("Apakah kamu memiliki kemampuan dalam mengorganisir tugas dan pekerjaan dengan baik? (ya/tidak)") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam hal manajemen keuangan publik dan pengelolaan anggaran? (ya/tidak)") == "ya":
                bakat ="fisip"
            else:
                bakat = "ulang"

    elif nilai == "seni":
        if "konstruksi" in minat and "teknologi" in minat:
            if input("Apakah kamu memiliki kemampuan untuk menggambar dengan akurat dan membuat model 3D? (ya/tidak) ") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki kemampuan mengelola software desain seperti Adobe Illustrator, Photoshop, dll? (ya/tidak) ") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan untuk mengubah tata letak dan dekorasi suatu ruangan? (ya/tidak)") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"
        
        elif "konstruksi" in minat and "teknologi" not in minat:
            if input("Apakah kamu memiliki kemampuan untuk menggambar dengan akurat dan membuat model 3D? (ya/tidak) ") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan untuk mengubah tata letak dan dekorasi suatu ruangan? (ya/tidak)") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"
                
        elif "konstruksi" not in minat and "teknologi" in minat:
            if input("Apakah kamu memiliki kemampuan mengelola software desain seperti Adobe Illustrator, Photoshop, dll? (ya/tidak) ") == "ya":
                bakat ="fad"
            else:
                bakat = "ulang"

    elif nilai == "pkn":
        if "hukum" in minat and "ilmu_sosial" in minat:
            if input("Apakah kamu memiliki nilai integritas yang tinggi, serta dapat mempertahankan kebeneran dan keadilan? (ya/tidak) ") == "ya":
                bakat ="hukum"
            elif input("Apakah kamu memiliki keterampilan komunikasi yang baik dan mampu berbicara dalam beberapa bahasa? (ya/tidak) ") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam merencanakan dan mengkoordinasi perjalanan wisata, mulai dari transportasi, akomodasi, hingga kegiatan? (ya/tidak)") == "ya":
                bakat ="fisip"
            else:
                bakat = "ulang"
        
        elif "hukum" in minat and "ilmu_sosial" not in minat:
            if input("Apakah kamu memiliki nilai integritas yang tinggi, serta dapat mempertahankan kebeneran dan keadilan? (ya/tidak) ") == "ya":
                bakat ="hukum"
            else:
                bakat = "ulang"
                
        elif "hukum" not in minat and "ilmu_sosial" in minat:
            if input("Apakah kamu memiliki keterampilan komunikasi yang baik dan mampu berbicara dalam beberapa bahasa? (ya/tidak) ") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam merencanakan dan mengkoordinasi perjalanan wisata, mulai dari transportasi, akomodasi, hingga kegiatan? (ya/tidak)") == "ya":
                bakat ="fisip"
            else:
                bakat = "ulang"

    elif nilai == "bahasa":
        if "ilmu_sosial" in minat:
            if input("Apakah kamu memiliki kemampuan komunikasi yang baik secara lisan dan tertulis? (ya/tidak) ") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki kemampuan mengelola software desain seperti Adobe Illustrator, Photoshop, dll? (ya/tidak) ") == "ya":
                bakat ="fisip"
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
