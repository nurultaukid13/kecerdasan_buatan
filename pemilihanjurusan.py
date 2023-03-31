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
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat? (ya/tidak)") == "ya":
                bakat ="feb"
            else:
                bakat = "ulang"
        
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat??? (ya/tidak)") == "ya":
                bakat ="feb"
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
                bakat ="ft"
            elif input("Apakah kamu memiliki kemampuan memanajemen produksi dan operasional industri? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk penanganan limbah industri? (ya/tidak)") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk pengolahan dan penilitian produk pangan? (ya/tidak)") == "ya":
                bakat ="ft"
            else:
                bakat = "ulang"
        
        elif "bioproses" in minat and "lingkungan" not in minat:
            if input("Apakah kamu memiliki kemampuan memproses zat kimia untuk bahan industri? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu memiliki kemampuan memanajemen produksi dan operasional industri? (ya/tidak) ") == "ya":
                bakat ="ft"
            else:
                bakat = "ulang"
                
        elif "bioproses" not in minat and "lingkungan" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk penanganan limbah industri? (ya/tidak)") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk pengolahan dan penilitian produk pangan? (ya/tidak)") == "ya":
                bakat ="ft"
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
            elif input("Apakah kamu memiliki keterampilan dalam menafsirkan teks bahasa Indonesia seperti sastra atau dokumen sejarah? (ya/tidak) ") == "ya":
                bakat ="fisip"
            else:
                bakat = "ulang"

    elif nilai == "biologi":
        if "pertanian" in minat and "lingkungan" in minat:
            if input("Apakah Anda memiliki kemampuan untuk melakukan perencanaan dan manajemen bisnis dalam industri pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki bakat dalam merancang dan mengembangkan teknologi pengelolahan hasil pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan analitis yang baik dan menyelesaikan masalah yang berkaitan dengan lingkungan? (ya/tidak)") == "ya":
                bakat ="ft"
            else:
                bakat = "ulang"
        
        elif "pertanian" in minat and "lingkungan" not in minat:
            if input("Apakah Anda memiliki kemampuan untuk melakukan perencanaan dan manajemen bisnis dalam industri pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki bakat dalam merancang dan mengembangkan teknologi pengelolahan hasil pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            else:
                bakat = "ulang"
                
        elif "pertanian" not in minat and "lingkungan" in minat:
            if input("Apakah kamu memiliki kemampuan analitis yang baik dan menyelesaikan masalah yang berkaitan dengan lingkungan? (ya/tidak)") == "ya":
                bakat ="ft"
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

def preferensi_kerja(nilai, minat, bakat):
    if nilai == "matematika":
        if "teknologi" in minat and "bisnis" not in minat and "kontruksi" not in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
                else:
                    jurusan = "ulang"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Mesin"
                else:
                    jurusan = "ulang"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    bakat ="Desain Komunikasi Visual"
                else:
                    jurusan = "ulang"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    bakat ="Agroteknologi"
                else:
                    jurusan = "ulang"

        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" not in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
                else:
                    jurusan = "ulang"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="teknik mesin"
                else:
                    jurusan = "ulang"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    bakat ="Desain Komunikasi Visual"
                else:
                    jurusan = "ulang"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    bakat ="Agroteknologi"
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    bakat ="agribisnis"
                else:
                    jurusan = "ulang"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    bakat ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Kewirausahaan"
                else:
                    jurusan = "ulang"
        
        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
                else:
                    jurusan = "ulang"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="teknik mesin"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                else:
                    jurusan = "ulang"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    bakat ="Desain Komunikasi Visual"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    bakat ="Arsitektur"
                else:
                    jurusan = "ulang"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    bakat ="Agroteknologi"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    bakat ="agribisnis"
                else:
                    jurusan = "ulang"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    bakat ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Kewirausahaan"
                else:
                    jurusan = "ulang"
        
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" in minat:
            if bakat == "ft":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                else:
                    jurusan = "ulang"
            elif bakat == "fad":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    bakat ="Arsitektur"
                else:
                    jurusan = "ulang"
            elif bakat == "faperta":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    bakat ="agribisnis"
                else:
                    jurusan = "ulang"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    bakat ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Kewirausahaan"
                else:
                    jurusan = "ulang"
                
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" not in minat:
            if bakat == "faperta":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    bakat ="agribisnis"
                else:
                    jurusan = "ulang"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    bakat ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Kewirausahaan"
                else:
                    jurusan = "ulang"
                
        elif "teknologi" not in minat and "bisnis" not in minat and "kontruksi" in minat:
            if bakat == "ft":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                else:
                    jurusan = "ulang"
            elif bakat == "fad":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    bakat ="Arsitektur"
                else:
                    jurusan = "ulang"
                
        elif "teknologi" in minat and "bisnis" not in minat and "kontruksi" in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
                else:
                    jurusan = "ulang"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="teknik mesin"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                else:
                    jurusan = "ulang"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    bakat ="Desain Komunikasi Visual"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    bakat ="Arsitektur"
                else:
                    jurusan = "ulang"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    bakat ="Agroteknologi"
                else:
                    jurusan = "ulang"
    
    elif nilai == "fisika":
        if "murni" in minat and "kontruksi" in minat:
            if bakat == "fad":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Arsitektur"
                else:
                    jurusan = "ulang"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Fisika"
                elif input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                else:
                    jurusan = "ulang"
    
        elif "murni" in minat and "kontruksi" not in minat:
            if bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Fisika"
                else:
                    jurusan = "ulang"
                    
        elif "murni" not in minat and "kontruksi" in minat:
            if bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                else:
                    jurusan = "ulang"
                    
            elif bakat == "fad":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Arsitektur"
                else:
                    jurusan = "ulang"
    
    elif nilai == "kimia":
        if "bioproses" in minat and "lingkungan" in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Kimia"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Industri"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Lingkungan"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknologi Pangan"
                else:
                    jurusan = "ulang"
    
        elif "bioproses" in minat and "lingkungan" not in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Kimia"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Industri"
                else:
                    jurusan = "ulang"
                    
        elif "bioproses" not in minat and "lingkungan" in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Lingkungan"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="Teknologi Pangan"
                else:
                    jurusan = "ulang"
                    
    if(jurusan == "ulang"):
        print("=========================================================")
        print("Maaf anda mungkin harus mengulangi di tahap bakat karena tidak memiliki jurusan yang sesuai di "+bakat)
    else:
        print("=========================================================")
        print("Dari nilai akademik, minat, bakat dan preferensi kerja anda kami merekomendasikan anda untuk memilih jurusan "+jurusan)
    
    return jurusan

nilai=nilai_akademik()
minat= minat(nilai)
bakat= bakat(nilai, minat)
preferensi_kerja(nilai, minat, bakat)
