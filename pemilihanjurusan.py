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
            "tidak": "ulang"
        }
    }

    pertanyaan = "Apakah kamu memiliki nilai matematika yang bagus?"
    while pertanyaan in mata_pelajaran:
        jawaban = input(pertanyaan + " (ya/tidak) ")
        if jawaban not in ["ya", "tidak"]:
            print("Jawaban tidak valid, silakan jawab dengan ya atau tidak.")
            nilai_akademik = "ulang"
            break
        pertanyaan = mata_pelajaran[pertanyaan][jawaban] if jawaban in mata_pelajaran[pertanyaan] else None
        if pertanyaan and pertanyaan != "ulang":
            nilai_akademik = pertanyaan
        else:
            print("===================================================================")
            print("Maaf kami tidak bisa merekomendasikan jurusan apapun")
            print("Mohon mengulangi tahap ini lagi dan memilih salah satu mata pelajaran yang anda sukai")
            nilai_akademik = "ulang"

    return nilai_akademik

def fungsi_minat(nilai):
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
    minat=[]
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
        print("===================================================================")
        print("Maaf anda mungkin harus mengulangi di tahap nilai akademik karena tidak memiliki minat di bidang " + nilai)
        return "ulang"

def fungsi_bakat(nilai, minat):
    bakat = "ulang"
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

        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="fik"
            elif input("Apakah kamu memiliki kemampuan untuk mengelola waktu dengan baik dan mampu mengatur jadwal dengan efektif? (ya/tidak)") =="ya":
                bakat ="fisip"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat? (ya/tidak)") == "ya":
                bakat ="feb"
                
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
        
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat??? (ya/tidak)") == "ya":
                bakat ="feb"
                
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat??? (ya/tidak)") == "ya":
                bakat ="feb"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
                
        elif "teknologi" not in minat and "bisnis" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
                
        elif "teknologi" in minat and "bisnis" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan memecahkan masalah logika dengan baik? (ya/tidak) ") == "ya":
                bakat ="fik"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
            elif input("Apakah kamu mempunyai kemampuan untuk membuat sistem pertanian?? (ya/tidak)") == "ya":
                bakat ="faperta"
                
    elif nilai == "fisika":
        if "murni" in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan menyelesaikan permasalahan fisika secara toeristis? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
        
        elif "murni" in minat and "kontruksi" not in minat:
            if input("Apakah kamu memiliki kemampuan menyelesaikan permasalahan fisika secara toeristis? (ya/tidak) ") == "ya":
                bakat ="ft"
        
        elif "murni" not in minat and "kontruksi" in minat:
            if input("Apakah kamu memiliki kemampuan teknis yang kuat? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk menggambar dan mendesain dengan baik?? (ya/tidak)") == "ya":
                bakat ="fad"
                
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
        
        elif "bioproses" in minat and "lingkungan" not in minat:
            if input("Apakah kamu memiliki kemampuan memproses zat kimia untuk bahan industri? (ya/tidak) ") == "ya":
                bakat ="ft"
            elif input("Apakah kamu memiliki kemampuan memanajemen produksi dan operasional industri? (ya/tidak) ") == "ya":
                bakat ="ft"
                
        elif "bioproses" not in minat and "lingkungan" in minat:
            if input("Apakah kamu mempunyai kemampuan untuk penanganan limbah industri? (ya/tidak)") == "ya":
                bakat ="ft"
            elif input("Apakah kamu mempunyai kemampuan untuk pengolahan dan penilitian produk pangan? (ya/tidak)") == "ya":
                bakat ="ft"

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
        
        elif "bisnis" in minat and "administrasi" not in minat:
            if input("Apakah kamu memiliki keterampilan kepemimpinan dan manajemen yang kuat?? (ya/tidak) ") == "ya":
                bakat ="feb"
            elif input("Apakah kamu memiliki bakat dalam mengelola keuangan dan membuat laporan keuangan yang akurat? (ya/tidak) ") == "ya":
                bakat ="feb"
                
        elif "bisnis" not in minat and "administrasi" in minat:
            if input("Apakah kamu memiliki kemampuan dalam mengorganisir tugas dan pekerjaan dengan baik? (ya/tidak)") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam hal manajemen keuangan publik dan pengelolaan anggaran? (ya/tidak)") == "ya":
                bakat ="fisip"

    elif nilai == "seni":
        if "konstruksi" in minat and "teknologi" in minat:
            if input("Apakah kamu memiliki kemampuan untuk menggambar dengan akurat dan membuat model 3D? (ya/tidak) ") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki kemampuan mengelola software desain seperti Adobe Illustrator, Photoshop, dll? (ya/tidak) ") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan untuk mengubah tata letak dan dekorasi suatu ruangan? (ya/tidak)") == "ya":
                bakat ="fad"
        
        elif "konstruksi" in minat and "teknologi" not in minat:
            if input("Apakah kamu memiliki kemampuan untuk menggambar dengan akurat dan membuat model 3D? (ya/tidak) ") == "ya":
                bakat ="fad"
            elif input("Apakah kamu memiliki keterampilan untuk mengubah tata letak dan dekorasi suatu ruangan? (ya/tidak)") == "ya":
                bakat ="fad"
                
        elif "konstruksi" not in minat and "teknologi" in minat:
            if input("Apakah kamu memiliki kemampuan mengelola software desain seperti Adobe Illustrator, Photoshop, dll? (ya/tidak) ") == "ya":
                bakat ="fad"

    elif nilai == "pkn":
        if "hukum" in minat and "ilmu_sosial" in minat:
            if input("Apakah kamu memiliki nilai integritas yang tinggi, serta dapat mempertahankan kebeneran dan keadilan? (ya/tidak) ") == "ya":
                bakat ="hukum"
            elif input("Apakah kamu memiliki keterampilan komunikasi yang baik dan mampu berbicara dalam beberapa bahasa? (ya/tidak) ") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam merencanakan dan mengkoordinasi perjalanan wisata, mulai dari transportasi, akomodasi, hingga kegiatan? (ya/tidak)") == "ya":
                bakat ="fisip"
        
        elif "hukum" in minat and "ilmu_sosial" not in minat:
            if input("Apakah kamu memiliki nilai integritas yang tinggi, serta dapat mempertahankan kebeneran dan keadilan? (ya/tidak) ") == "ya":
                bakat ="hukum"
                
        elif "hukum" not in minat and "ilmu_sosial" in minat:
            if input("Apakah kamu memiliki keterampilan komunikasi yang baik dan mampu berbicara dalam beberapa bahasa? (ya/tidak) ") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki bakat dalam merencanakan dan mengkoordinasi perjalanan wisata, mulai dari transportasi, akomodasi, hingga kegiatan? (ya/tidak)") == "ya":
                bakat ="fisip"

    elif nilai == "bahasa":
        if "ilmu_sosial" in minat:
            if input("Apakah kamu memiliki kemampuan komunikasi yang baik secara lisan dan tertulis? (ya/tidak) ") == "ya":
                bakat ="fisip"
            elif input("Apakah kamu memiliki keterampilan dalam menafsirkan teks bahasa Indonesia seperti sastra atau dokumen sejarah? (ya/tidak) ") == "ya":
                bakat ="fisip"

    elif nilai == "biologi":
        if "pertanian" in minat and "lingkungan" in minat:
            if input("Apakah Anda memiliki kemampuan untuk melakukan perencanaan dan manajemen bisnis dalam industri pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki bakat dalam merancang dan mengembangkan teknologi pengelolahan hasil pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki kemampuan analitis yang baik dan menyelesaikan masalah yang berkaitan dengan lingkungan? (ya/tidak)") == "ya":
                bakat ="ft"
        
        elif "pertanian" in minat and "lingkungan" not in minat:
            if input("Apakah Anda memiliki kemampuan untuk melakukan perencanaan dan manajemen bisnis dalam industri pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
            elif input("Apakah kamu memiliki bakat dalam merancang dan mengembangkan teknologi pengelolahan hasil pertanian? (ya/tidak) ") == "ya":
                bakat ="faperta"
                
        elif "pertanian" not in minat and "lingkungan" in minat:
            if input("Apakah kamu memiliki kemampuan analitis yang baik dan menyelesaikan masalah yang berkaitan dengan lingkungan? (ya/tidak)") == "ya":
                bakat ="ft"
    
    if bakat != "ulang":
        return bakat
    else:
        print("===================================================================")
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
    jurusan = "ulang"
    if nilai == "matematika":
        if "teknologi" in minat and "bisnis" not in minat and "kontruksi" not in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Mesin"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    jurusan ="Desain Komunikasi Visual"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    jurusan ="Agroteknologi"

        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" not in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="teknik mesin"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    jurusan ="Desain Komunikasi Visual"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    jurusan ="Agroteknologi"
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    jurusan ="agribisnis"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    jurusan ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Kewirausahaan"
        
        elif "teknologi" in minat and "bisnis" in minat and "kontruksi" in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="teknik mesin"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    jurusan ="Desain Komunikasi Visual"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    jurusan ="Arsitektur"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    jurusan ="Agroteknologi"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    jurusan ="agribisnis"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    jurusan ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Kewirausahaan"
        
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" in minat:
            if bakat == "ft":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
            elif bakat == "fad":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    jurusan ="Arsitektur"
            elif bakat == "faperta":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    jurusan ="agribisnis"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    jurusan ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    bakat ="Kewirausahaan"
                
        elif "teknologi" not in minat and "bisnis" in minat and "kontruksi" not in minat:
            if bakat == "faperta":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kemampuan untuk mengelola keuangan dan memantau kinerja bisnis pertanian? (ya/tidak)") == "ya":
                    jurusan ="agribisnis"
            elif bakat == "feb":
                if input("Apakah Anda lebih tertarik bekerja pada pengembangan ekonomi yang berfokus pada pemerataan pembangunan? (ya/tidak)") == "ya":
                    jurusan ="Ekonomi Pembangunan"
                elif input("Apakah Anda tertarik bekerja pada manajemen strategis yang berfokus pada pengembangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Manajemen"
                elif input("Apakah Anda lebih suka bekerja dengan angka-angka dan data keuangan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Akuntansi Manajemen"
                elif input("Apakah Anda suka bekerja secara mandiri dalam mengelola ide baru dalam bisnis dan mengambil risiko yang diperlukan untuk mencapai tujuan bisnis?  (ya/tidak)") == "ya":
                    jurusan ="Kewirausahaan"
                
        elif "teknologi" not in minat and "bisnis" not in minat and "kontruksi" in minat:
            if bakat == "ft":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
            elif bakat == "fad":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    jurusan ="Arsitektur"
                
        elif "teknologi" in minat and "bisnis" not in minat and "kontruksi" in minat:
            if bakat == "fik":
                if input("Apakah Anda lebih tertarik untuk bekerja pada proyek-proyek pengembangan perangkat lunak dan infrastrukturnya? (ya/tidak) ") == "ya":
                    jurusan ="informatika"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada software bisnis? (ya/tidak) ") == "ya":
                    jurusan ="Sistem informasi"
                elif input("Apakah Anda lebih tertarik untuk bekerja pada sebagai analis data? (ya/tidak) ") == "ya":
                    jurusan ="Sains Data"
            elif bakat == "ft":
                if input("Apakah anda tertarik pada pekerjaan yang terkait dengan otomotif? (ya/tidak) ") == "ya":
                    jurusan ="teknik mesin"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
            elif bakat == "fad":
                if input("Apakah kamu tertarik bekerja pada proyek desain yang bersifat digital? (ya/tidak)") == "ya":
                    jurusan ="Desain Komunikasi Visual"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    jurusan ="Arsitektur"
            elif bakat == "faperta":
                if input("Apakah Anda lebih suka bekerja pada teknologi pertanian yang berbasis pada teknologi digital dan mekanik? (ya/tidak)") == "ya":
                    jurusan ="Agroteknologi"
    
    elif nilai == "fisika":
        if "murni" in minat and "kontruksi" in minat:
            if bakat == "fad":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    jurusan ="Arsitektur"
            elif bakat == "ft":
                if input("Apakah Anda lebih tertarik bekerja di laboratorium dalam bidang riset fisika? (ya/tidak) ") == "ya":
                    jurusan ="Fisika"
                elif input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
    
        elif "murni" in minat and "kontruksi" not in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih tertarik bekerja di laboratorium dalam bidang riset fisika? (ya/tidak) ") == "ya":
                    jurusan ="Fisika"
                    
        elif "murni" not in minat and "kontruksi" in minat:
            if bakat == "ft":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan keahlian teknis dalam merancang, membangun, dan mengelola infrastruktur fisik? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Sipil"
                    
            elif bakat == "fad":
                if input("Apakah Anda tertarik pada pekerjaan yang memerlukan kreativitas dalam merancang bangunan yang berfungsi dan estetis? (ya/tidak)") == "ya":
                    jurusan ="Arsitektur"
    
    elif nilai == "kimia":
        if "bioproses" in minat and "lingkungan" in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih tertarik bekerja dalam pengolahan bahan kimia untuk kebutuhan industri?(ya/tidak) ") == "ya":
                    jurusan ="Teknik Kimia"
                elif input("Apakah Anda lebih tertarik bekerja di departemen produksi dalam sektor industri? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Industri"
                elif input("Apakah Anda lebih menyukai pekerjaan yang melibatkan pengembangan teknologi lingkungan atau lebih suka bekerja pada perencanaan kebijakan lingkungan? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Lingkungan"
                elif input("Apakah anda tertarik pada pekerjaan pengembangan produk pangan serta pengolahannya? (ya/tidak) ") == "ya":
                    jurusan ="Teknologi Pangan"
    
        elif "bioproses" in minat and "lingkungan" not in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih tertarik bekerja dalam pengolahan bahan kimia untuk kebutuhan industri?(ya/tidak) ") == "ya":
                    jurusan ="Teknik Kimia"
                elif input("Apakah Anda lebih tertarik bekerja di departemen produksi dalam sektor industri? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Industri"
                    
        elif "bioproses" not in minat and "lingkungan" in minat:
            if bakat == "ft":
                if input("Apakah Anda lebih menyukai pekerjaan yang melibatkan pengembangan teknologi lingkungan atau lebih suka bekerja pada perencanaan kebijakan lingkungan? (ya/tidak) ") == "ya":
                    jurusan ="Teknik Lingkungan"
                elif input("Apakah anda tertarik pada pekerjaan pengembangan produk pangan serta pengolahannya? (ya/tidak) ") == "ya":
                    jurusan ="Teknologi Pangan"

    elif nilai == "ekonomi":
        if "bisnis" in minat and "administrasi" in minat:
            if bakat == "feb":
                if input("Apakah Anda ingin bekerja di industri tertentu seperti perbankan, ritel, manufaktur, ataupun teknologi?(ya/tidak) ") == "ya":
                    jurusan ="Menejemen"
                elif input("Apakah Anda ingin bekerja di industri perencanaan keuangan dan pelaporan keuangan dalam pekerjaan akuntansi? (ya/tidak) ") == "ya":
                    jurusan ="Akutansi"
            
            elif bakat == "fisip":
                if input("Apakah Anda ingin bekerja di lembaga pemerintah, organisasi nirlaba, atau sektor swasta yang bergerak di bidang publik? (ya/tidak) ") == "ya":
                    jurusan ="Administrasi Publik"
                elif input("Apakah Anda tertarik bekerja pada bidang keuangan ataupun pemasaran? (ya/tidak) ") == "ya":
                    jurusan ="Administrasi Bisnis"
        
        elif "bisnis" in minat and "administrasi" not in minat:
            if bakat == "feb":
                if input("Apakah Anda ingin bekerja di industri tertentu seperti perbankan, ritel, manufaktur, ataupun teknologi?(ya/tidak) ") == "ya":
                    jurusan ="Menejemen"
                elif input("Apakah Anda ingin bekerja di industri perencanaan keuangan dan pelaporan keuangan dalam pekerjaan akuntansi? (ya/tidak) ") == "ya":
                    jurusan ="Akutansi"
                
        elif "bisnis" not in minat and "administrasi" in minat:
            if bakat == "fisip":
                if input("Apakah Anda ingin bekerja di lembaga pemerintah, organisasi nirlaba, atau sektor swasta yang bergerak di bidang publik? (ya/tidak) ") == "ya":
                    jurusan ="Administrasi Publik"
                elif input("Apakah Anda tertarik bekerja pada bidang keuangan ataupun pemasaran? (ya/tidak) ") == "ya":
                    jurusan ="Administrasi Bisnis"

    elif nilai == "pkn":
        if "hukum" in minat and "ilmu_sosial" in minat:
            if bakat == "hukum":
                if input("Apakah Anda lebih tertarik pada pekerjaan yang berhubungan dengan penerapan hukum dan pembuatan kebijakan hukum? (ya/tidak) ") == "ya":
                    jurusan ="Ilmu Hukum"

            elif bakat == "fisip":
                if input("Apakah Anda lebih tertarik pada pekerjaan di industri pariwisata seperti wisata budaya atau wisata petualangan? (ya/tidak) ") == "ya":
                    jurusan = "Pariwisata"
                elif input("Apakah Anda lebih tertarik pada pekerjaan yang melibatkan diplomasi multilateral dan diplomasi bilateral? (ya/tidak)") == "ya":
                    jurusan ="Hubungan Internasional"

        elif "hukum" in minat and "ilmu_sosial" not in minat:
            if bakat == "hukum":
                if input("Apakah Anda lebih tertarik pada pekerjaan yang berhubungan dengan penerapan hukum dan pembuatan kebijakan hukum? (ya/tidak) ") == "ya":
                    jurusan ="Ilmu Hukum"
                
        elif "hukum" not in minat and "ilmu_sosial" in minat:
            if bakat == "fisip":
                if input("Apakah Anda lebih tertarik pada pekerjaan di industri pariwisata seperti wisata budaya atau wisata petualangan? (ya/tidak) ") == "ya":
                    jurusan ="Pariwisata"
                elif input("Apakah Anda lebih tertarik pada pekerjaan yang melibatkan diplomasi multilateral dan diplomasi bilateral? (ya/tidak)") == "ya":
                    jurusan ="Hubungan Internasional"

    elif nilai == "seni":
        if "konstruksi" in minat and "teknologi" in minat:
            if bakat == "fad":
                if input("Apakah anda tertarik pada pembuatan desain rumah tinggal dan bangunan yang berkelanjutan? (ya/tidak) ") == "ya":
                    jurusan ="arsitektur"
                elif input("Apakah anda tertarik pada desain digital dan desain grafis? (ya/tidak) ") == "ya":
                    jurusan ="desain komunikasi visual"
                elif input("Apakah anda tertarik pada desain interior rumah dan desain komersial? (ya/tidak)") == "ya":
                    jurusan ="interior desain"

        elif "konstruksi" in minat and "teknologi" not in minat:
            if bakat == "fad":
                if input("Apakah anda tertarik pada pembuatan desain rumah tinggal dan bangunan yang berkelanjutan? (ya/tidak) ") == "ya":
                    jurusan ="arsitektur"
                elif input("Apakah anda tertarik pada desain interior rumah dan desain komersial? (ya/tidak)") == "ya":
                    jurusan ="interior desain"

        elif "konstruksi" not in minat and "teknologi" in minat:
            if bakat == "fad":
                if input("Apakah anda tertarik pada desain digital dan desain grafis? (ya/tidak) ") == "ya":
                    jurusan ="desain komunikasi visual"

        elif nilai == "bahasa":
            if "ilmu_sosial" in minat:
                if bakat == "fisip":
                    if input("Apakah anda tertarik pada industri jurnalistik dan media massa? (ya/tidak) ") == "ya":
                        jurusan ="ilmu komunikasi"
                    elif input("Apakah anda tertarik pada pembelajaran dan pengajaran bahasa indonesia? (ya/tidak) ") == "ya":
                        jurusan ="linguistik indonesia"
                    else:
                        jurusan = "ulang"

        elif nilai == "biologi":
            if "pertanian" in minat and "lingkungan" in minat:
                if bakat == "faperta":
                    if input("Apakah anda tertarik pada pengembangan usaha dan manajemen bisnis pada bidang pertanian? (ya/tidak) ") == "ya":
                        jurusan ="agribisnis"
                    elif input("Apakah anda tertarik pada industri pengolahan bahan baku pertanian? (ya/tidak) ") == "ya":
                        jurusan ="agroteknologi"
                    else:
                        jurusan = "ulang"

            elif bakat == "ft":
                if input("Apakah anda tertarik pada pengelolaan limbah dan pengelolaan polusi? (ya/tidak)") == "ya":
                    jurusan ="teknik lingkungan"
        
        elif "pertanian" in minat and "lingkungan" not in minat:
            if bakat == "faperta":
                if input("Apakah anda tertarik pada pengembangan usaha dan manajemen bisnis pada bidang pertanian? (ya/tidak) ") == "ya":
                    jurusan ="agribisnis"
                elif input("Apakah anda tertarik pada industri pengolahan bahan baku pertanian? (ya/tidak) ") == "ya":
                    jurusan ="agroteknologi"
                
        elif "pertanian" not in minat and "lingkungan" in minat:
            if bakat == "ft":
                if input("Apakah anda tertarik pada pengelolaan limbah dan pengelolaan polusi? (ya/tidak)") == "ya":
                    jurusan ="teknik lingkungan"
                else:
                    jurusan= "ulang"

    if jurusan != "ulang":
        print("===================================================================")
        print("Dari nilai akademik, minat, bakat dan preferensi kerja anda, kami merekomendasikan anda untuk memilih jurusan "+jurusan)
        print("===================================================================")
        return jurusan
    else:
        print("===================================================================")
        print("Maaf anda mungkin harus mengulangi di tahap bakat karena tidak memiliki jurusan yang sesuai di "+bakat)
        return jurusan


#main program
minat = nilai = bakat = jurusan =''
while True:
    if(nilai == "ulang"):
        print("===================================================================")
        print(" ")
    nilai = nilai_akademik()
    if nilai != "ulang":
        while True:
            if(minat == "ulang"):
                print("===================================================================")
                print(" ")
                nilai = nilai_akademik()
            minat = fungsi_minat(nilai)
            if minat != "ulang":
                while True:
                    if(bakat == "ulang"):
                        print("===================================================================")
                        print(" ")
                        minat = fungsi_minat(nilai)
                    bakat=fungsi_bakat(nilai, minat)
                    if bakat != "ulang":
                        while True:
                            if(jurusan == "ulang"):
                                print("===================================================================")
                                print(" ")
                                bakat = fungsi_bakat(nilai, minat)
                            jurusan=preferensi_kerja(nilai, minat, bakat)
                            if jurusan != "ulang":
                                break
                        break
                break
        break