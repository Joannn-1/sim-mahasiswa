import os
import re


# =====================================================================
# SOAL 1: Analisis kalimat (string)
# =====================================================================
def soal_1():
    print("\n=== SOAL 1: ANALISIS KALIMAT ===")
    kalimat = input("Masukkan sebuah kalimat: ").strip()

    if not kalimat:
        print("Kalimat tidak boleh kosong.")
        return

    kata_list = kalimat.split()

    # (a) jumlah kata
    jumlah_kata = len(kata_list)

    # (b) jumlah karakter (dengan dan tanpa spasi)
    jumlah_karakter = len(kalimat)
    jumlah_tanpa_spasi = len(kalimat.replace(" ", ""))

    # (c) kata terpanjang (tanda baca di tepi kata dibuang)
    kata_bersih = [k.strip(".,;:!?\"'()[]{}-") for k in kata_list]
    kata_terpanjang = max(kata_bersih, key=len)

    # (d) title case
    judul = kalimat.title()

    print(f"(a) Jumlah kata                 : {jumlah_kata}")
    print(f"(b) Jumlah karakter             : {jumlah_karakter} "
          f"(tanpa spasi: {jumlah_tanpa_spasi})")
    print(f"(c) Kata terpanjang             : {kata_terpanjang} "
          f"({len(kata_terpanjang)} huruf)")
    print(f"(d) Title case                  : {judul}")


# =====================================================================
# SOAL 2: Analisis nilai mahasiswa (list + dictionary)
# =====================================================================
def tentukan_kategori(nilai):
    """Skala: A >= 85, B >= 70, C >= 60, D >= 50, E < 50."""
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    return "E"


def soal_2():
    print("\n=== SOAL 2: ANALISIS NILAI MAHASISWA ===")
    teks = input("Masukkan nilai (pisahkan dengan spasi atau koma): ")

    try:
        nilai = [float(x) for x in re.split(r"[,\s]+", teks.strip()) if x]
    except ValueError:
        print("Input tidak valid. Gunakan angka saja.")
        return

    if not nilai:
        print("Tidak ada nilai yang dimasukkan.")
        return

    # (a) rata-rata
    rata_rata = sum(nilai) / len(nilai)

    # (b) tertinggi & terendah
    tertinggi = max(nilai)
    terendah = min(nilai)

    # (c) kelompokkan ke kategori
    kategori_list = [tentukan_kategori(n) for n in nilai]

    # (d) frekuensi kategori dengan dictionary
    frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for k in kategori_list:
        frekuensi[k] += 1

    print(f"\n(a) Rata-rata        : {rata_rata:.2f}")
    print(f"(b) Nilai tertinggi  : {tertinggi}")
    print(f"    Nilai terendah   : {terendah}")
    print("(c) Kategori tiap nilai:")
    for n, k in zip(nilai, kategori_list):
        print(f"      {n:>6} -> {k}")
    print("(d) Frekuensi kategori:")
    for k, jml in frekuensi.items():
        print(f"      {k}: {jml} {'*' * jml}")
    print(f"    Dictionary: {frekuensi}")


# =====================================================================
# SOAL 3: Operasi set pada penerima beasiswa (Studi Kasus Kampus)
# =====================================================================
def soal_3():
    print("\n=== SOAL 3: OPERASI SET BEASISWA ===")
    print("Simulasi Seleksi Penerima Beasiswa Mahasiswa")
    print("1. Gunakan Data Sampel (Simulasi database prodi)")
    print("2. Input Data NIM Mandiri")
    pilihan_mode = input("Pilih mode [1/2, default 1]: ").strip()

    if pilihan_mode == "2":
        teks_a = input("Masukkan NIM penerima Beasiswa PPA (pisahkan koma/spasi): ")
        teks_b = input("Masukkan NIM penerima Beasiswa Subsidi (pisahkan koma/spasi): ")
        beasiswa_a = [x.strip() for x in re.split(r"[,\s]+", teks_a) if x.strip()]
        beasiswa_b = [x.strip() for x in re.split(r"[,\s]+", teks_b) if x.strip()]
    else:
        # Data sampel realistis dengan NIM format prodi dan beberapa duplikat data mentah
        beasiswa_a = [
            "2023-IF-012", "2023-SI-045", "2023-TI-009", 
            "2023-IF-012", "2023-SI-088", "2023-DKV-021", "2023-SI-045"
        ]
        beasiswa_b = [
            "2023-SI-045", "2023-TI-009", "2023-SI-088", 
            "2023-AK-003", "2023-MN-014", "2023-IF-099"
        ]
        print("\nMenggunakan data sampel database beasiswa...")

    set_a = set(beasiswa_a)
    set_b = set(beasiswa_b)

    print(f"\n[Data Mentah]")
    print(f"- Beasiswa PPA (Peningkatan Prestasi Akademik) [Entry: {len(beasiswa_a)}]: {beasiswa_a}")
    print(f"- Beasiswa Subsidi UKT [Entry: {len(beasiswa_b)}]: {beasiswa_b}\n")

    print(f"[Analisis Unik (Set)]")
    print(f"- Penerima Unik PPA (Set A)        : {len(set_a)} mahasiswa")
    print(f"- Penerima Unik Subsidi (Set B)    : {len(set_b)} mahasiswa\n")

    # (a) menerima kedua beasiswa -> irisan
    kedua = set_a & set_b
    print(f"(a) Menerima Kedua Beasiswa (Irisan A & B):")
    print(f"    Jumlah: {len(kedua)} mahasiswa")
    print(f"    Daftar NIM: {sorted(kedua) if kedua else 'Tidak ada'}")

    # (b) hanya A -> selisih A - B
    hanya_a = set_a - set_b
    print(f"\n(b) Hanya Menerima PPA Saja (Selisih A - B):")
    print(f"    Jumlah: {len(hanya_a)} mahasiswa")
    print(f"    Daftar NIM: {sorted(hanya_a) if hanya_a else 'Tidak ada'}")

    # (c) B tetapi bukan A -> selisih B - A
    hanya_b = set_b - set_a
    print(f"\n(c) Hanya Menerima Subsidi Saja (Selisih B - A):")
    print(f"    Jumlah: {len(hanya_b)} mahasiswa")
    print(f"    Daftar NIM: {sorted(hanya_b) if hanya_b else 'Tidak ada'}")

    # (d) semua mahasiswa unik -> gabungan
    semua_unik = set_a | set_b
    print(f"\n(d) Total Keseluruhan Penerima Unik (Gabungan A | B):")
    print(f"    Jumlah total: {len(semua_unik)} mahasiswa")
    print(f"    Daftar lengkap: {sorted(semua_unik)}")


# =====================================================================
# SOAL 4: Inventaris toko (dictionary + tuple)
# =====================================================================
inventaris = {
    "Beras 5kg": (65000, 20),
    "Minyak Goreng 1L": (18000, 35),
    "Gula 1kg": (16000, 40),
    "Telur 1kg": (28000, 15),
    "Kopi Bubuk": (12000, 50),
}


def tambah_barang(nama, harga, stok):
    """(a) Menambah barang baru."""
    if nama in inventaris:
        print(f"'{nama}' sudah ada. Gunakan update_stok untuk mengubah stok.")
        return False
    inventaris[nama] = (harga, stok)
    print(f"Barang '{nama}' berhasil ditambahkan.")
    return True


def update_stok(nama, stok_baru):
    """(b) Mengupdate stok (tuple immutable, jadi dibuat ulang)."""
    if nama not in inventaris:
        print(f"Barang '{nama}' tidak ditemukan.")
        return False
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)
    print(f"Stok '{nama}' diperbarui menjadi {stok_baru}.")
    return True


def cari_by_harga(harga_min, harga_max):
    """(c) Mencari barang dengan harga dalam rentang tertentu."""
    return {
        nama: (harga, stok)
        for nama, (harga, stok) in inventaris.items()
        if harga_min <= harga <= harga_max
    }


def total_nilai_inventaris():
    """(d) Total nilai inventaris = jumlah (harga x stok)."""
    return sum(harga * stok for harga, stok in inventaris.values())


def tampilkan_inventaris():
    print(f"{'Nama Barang':<20}{'Harga':>12}{'Stok':>8}")
    print("-" * 40)
    for nama, (harga, stok) in inventaris.items():
        print(f"{nama:<20}{harga:>12,}{stok:>8}")


def soal_4():
    print("\n=== SOAL 4: INVENTARIS TOKO ===")
    while True:
        print("\n1. Tampilkan inventaris")
        print("2. Tambah barang baru")
        print("3. Update stok")
        print("4. Cari barang berdasarkan rentang harga")
        print("5. Hitung total nilai inventaris")
        print("0. Kembali ke menu utama")
        pilihan = input("Pilih: ").strip()

        try:
            if pilihan == "1":
                tampilkan_inventaris()
            elif pilihan == "2":
                nama = input("Nama barang : ").strip()
                harga = int(input("Harga       : "))
                stok = int(input("Stok        : "))
                tambah_barang(nama, harga, stok)
            elif pilihan == "3":
                nama = input("Nama barang : ").strip()
                stok = int(input("Stok baru   : "))
                update_stok(nama, stok)
            elif pilihan == "4":
                hmin = int(input("Harga minimum: "))
                hmax = int(input("Harga maksimum: "))
                hasil = cari_by_harga(hmin, hmax)
                if hasil:
                    for nama, (harga, stok) in hasil.items():
                        print(f"  {nama}: Rp{harga:,} (stok {stok})")
                else:
                    print("Tidak ada barang pada rentang harga tersebut.")
            elif pilihan == "5":
                print(f"Total nilai inventaris: Rp{total_nilai_inventaris():,}")
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input angka tidak valid.")


# =====================================================================
# SOAL 5: Analisis teks dari file (string, list, set, dict)
# =====================================================================
TEKS_CONTOH = (
    "Python adalah bahasa pemrograman yang populer. Python mudah dipelajari "
    "dan Python banyak digunakan untuk analisis data. Dalam Sistem Informasi, "
    "data adalah aset penting, dan bahasa Python membantu mengolah data "
    "dengan cepat dan efisien. Mahasiswa yang belajar Python akan memahami "
    "struktur data seperti list, tuple, set, dan dictionary."
)


def soal_5():
    print("\n=== SOAL 5: ANALISIS TEKS DARI FILE ===")
    path = input("Masukkan path file teks (kosongkan untuk pakai contoh): ").strip()

    if not path:
        path = "teks_contoh.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEKS_CONTOH)
        print(f"File contoh dibuat: {os.path.abspath(path)}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            teks = f.read()
    except FileNotFoundError:
        print(f"File '{path}' tidak ditemukan.")
        return
    except OSError as e:
        print(f"Gagal membaca file: {e}")
        return

    kata_list = re.findall(r"[a-zA-Z']+", teks.lower())

    if not kata_list:
        print("File tidak berisi kata.")
        return

    frekuensi = {}
    for kata in kata_list:
        frekuensi[kata] = frekuensi.get(kata, 0) + 1

    print(f"\nTotal kata: {len(kata_list)}")
    print(f"(a) Frekuensi seluruh kata ({len(frekuensi)} kata unik):")
    for kata, jml in sorted(frekuensi.items(), key=lambda x: (-x[1], x[0])):
        print(f"      {kata:<20} {jml}")

    top10 = sorted(frekuensi.items(), key=lambda x: (-x[1], x[0]))[:10]
    print("\n(b) 10 kata paling sering muncul:")
    for i, (kata, jml) in enumerate(top10, start=1):
        print(f"      {i:>2}. {kata:<20} {jml}")

    hapax = {kata for kata, jml in frekuensi.items() if jml == 1}
    print(f"\n(c) Hapax legomena ({len(hapax)} kata):")
    print("      " + ", ".join(sorted(hapax)))

    jumlah_unik = len(set(kata_list))
    ttr = jumlah_unik / len(kata_list)
    print(f"\n(d) Type-Token Ratio = {jumlah_unik} / {len(kata_list)} = {ttr:.4f}")


# =====================================================================
# MENU UTAMA
# =====================================================================
def main():
    menu = {
        "1": ("Analisis kalimat", soal_1),
        "2": ("Analisis nilai mahasiswa", soal_2),
        "3": ("Operasi set beasiswa", soal_3),
        "4": ("Inventaris toko", soal_4),
        "5": ("Analisis teks dari file", soal_5),
    }

    while True:
        print("\n" + "=" * 40)
        print("   JAWABAN SOAL PRAKTIK STRUKTUR DATA")
        print("=" * 40)
        for kode, (judul, _) in menu.items():
            print(f"   {kode}. {judul}")
        print("   0. Keluar")

        pilihan = input("Pilih soal: ").strip()
        if pilihan == "0":
            print("Terima kasih!")
            break
        elif pilihan in menu:
            menu[pilihan][1]()
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()