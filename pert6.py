"""
====================================================================
FILE UTAMA: main.py
Solusi Latihan Praktik Pemrograman Python (Soal 1 - 5)
Menggunakan modul bawaan Python (Tanpa dependencies eksternal)
====================================================================
"""

import math
import statistics
import json
import urllib.request

# ==================================================================
# SOAL 1: Fungsi hitung_statistik()
# ==================================================================
def hitung_statistik(angka_list: list) -> dict:
    """
    Menghitung mean, median, modus, range (max-min), dan standard deviation
    menggunakan library bawaan (statistics, math).
    """
    if not angka_list:
        raise ValueError("List angka tidak boleh kosong.")
    
    mean_val = statistics.mean(angka_list)
    median_val = statistics.median(angka_list)
    
    try:
        modus_val = statistics.mode(angka_list)
    except statistics.StatisticsError:
        modus_val = "Tidak ada modus tunggal"
        
    range_val = max(angka_list) - min(angka_list)
    std_dev_val = statistics.stdev(angka_list) if len(angka_list) > 1 else 0.0
    
    return {
        "mean": mean_val,
        "median": median_val,
        "modus": modus_val,
        "range": range_val,
        "standard_deviation": std_dev_val
    }


# ==================================================================
# SOAL 2: Fungsi validasi_data()
# ==================================================================
def validasi_data(data: dict, schema: dict, *args, **kwargs) -> tuple:
    """
    Validasi dictionary data berdasarkan schema (tipe data & rentang).
    Mengembalikan tuple (is_valid: bool, errors: list).
    """
    errors = []
    
    for field, rules in schema.items():
        if field not in data:
            errors.append(f"Field '{field}' wajib ada.")
            continue
            
        value = data[field]
        expected_type = rules.get("type")
        min_val = rules.get("min")
        max_val = rules.get("max")
        
        # Validasi Tipe Data
        if expected_type and not isinstance(value, expected_type):
            errors.append(f"Field '{field}' harus bertipe {expected_type.__name__}.")
            continue
        
        # Validasi Rentang (Angka)
        if isinstance(value, (int, float)):
            if min_val is not None and value < min_val:
                errors.append(f"Field '{field}' bernilai {value}, kurang dari batas minimum {min_val}.")
            if max_val is not None and value > max_val:
                errors.append(f"Field '{field}' bernilai {value}, melebihi batas maksimum {max_val}.")

    # Fleksibilitas tambahan (*args & **kwargs)
    if args:
        print(f"   [Info Opsional *args]: {args}")
    if kwargs:
        print(f"   [Info Opsional **kwargs]: {kwargs}")

    is_valid = len(errors) == 0
    return is_valid, errors


# ==================================================================
# SOAL 3: Modul Utilitas Akademik (Fungsi-Fungsi Akademik)
# ==================================================================
def konversi_nilai_huruf(nilai_angka: float) -> str:
    if nilai_angka >= 85:
        return 'A'
    elif nilai_angka >= 70:
        return 'B'
    elif nilai_angka >= 55:
        return 'C'
    elif nilai_angka >= 40:
        return 'D'
    else:
        return 'E'

def hitung_ipk(daftar_matkul: list) -> float:
    total_bobot = sum(m['sks'] * m['nilai'] for m in daftar_matkul)
    total_sks = sum(m['sks'] for m in daftar_matkul)
    if total_sks == 0:
        return 0.0
    return total_bobot / total_sks

def generate_transkrip(nama: str, daftar_matkul: list) -> str:
    ipk = hitung_ipk(daftar_matkul)
    transkrip = f"--- TRANSKRIP NILAI MAHASISWA: {nama} ---\n"
    for matkul in daftar_matkul:
        huruf = konversi_nilai_huruf(matkul['nilai'] * 25) # Asumsi skala 4 ke 100
        transkrip += f"- {matkul.get('nama', 'Mata Kuliah')} (SKS: {matkul['sks']}): Nilai {matkul['nilai']} [{huruf}]\n"
    transkrip += f"IPK Total: {ipk:.2f}"
    return transkrip


# ==================================================================
# SOAL 4: Sistem Informasi (Simulasi Package & Service CRUD In-Memory)
# ==================================================================
class MahasiswaModel:
    """Representasi Model Mahasiswa"""
    def __init__(self, nim: str, nama: str, jurusan: str):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def to_dict(self):
        return {"nim": self.nim, "nama": self.nama, "jurusan": self.jurusan}


class MahasiswaService:
    """Service CRUD dengan In-Memory Storage (Dictionary)"""
    def __init__(self):
        self.db = {}

    def create(self, mhs: MahasiswaModel):
        if mhs.nim in self.db:
            return False, "NIM sudah terdaftar!"
        self.db[mhs.nim] = mhs.to_dict()
        return True, "Data mahasiswa berhasil ditambahkan."

    def read_all(self):
        return list(self.db.values())

    def update(self, nim: str, nama_baru: str, jurusan_baru: str):
        if nim not in self.db:
            return False, "Mahasiswa tidak ditemukan!"
        self.db[nim]["nama"] = nama_baru
        self.db[nim]["jurusan"] = jurusan_baru
        return True, "Data mahasiswa berhasil diperbarui."

    def delete(self, nim: str):
        if nim in self.db:
            del self.db[nim]
            return True, "Data mahasiswa berhasil dihapus."
        return False, "Mahasiswa tidak ditemukan!"


# ==================================================================
# SOAL 5: Pemrosesan REST API (menggunakan urllib.request bawaan)
# ==================================================================
def proses_rest_api():
    """
    Mengambil data user dari JSONPlaceholder API menggunakan urllib, memprosesnya 
    dengan filter, map, sorted (menggunakan lambda), dan menyimpannya ke JSON.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    print("\n[SOAL 5] Mengambil data dari REST API (urllib)...")
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                print(f"Gagal mengambil data. Status code: {response.status}")
                return
            
            data_raw = response.read().decode('utf-8')
            users = json.loads(data_raw)
        
        # 1. Filter: Hanya user dengan domain website .org atau .net
        filtered_users = list(filter(lambda u: u['website'].endswith(('.org', '.net')), users))
        
        # 2. Map: Ambil atribut nama, email, dan website
        mapped_users = list(map(lambda u: {
            "nama": u['name'],
            "email": u['email'],
            "website": u['website']
        }, filtered_users))
        
        # 3. Sorted: Urutkan berdasarkan nama
        sorted_users = sorted(mapped_users, key=lambda u: u['nama'])
        
        # 4. Simpan ke file JSON
        nama_file = "hasil_analisis_user.json"
        with open(nama_file, "w", encoding="utf-8") as f:
            json.dump(sorted_users, f, indent=4)
            
        print(f"   [Berhasil] Data berhasil diproses & disimpan ke '{nama_file}'.")
        print("   Hasil pemrosesan:")
        for index, item in enumerate(sorted_users, 1):
            print(f"   {index}. {item['nama']} | {item['email']} | {item['website']}")
            
    except Exception as e:
        print(f"   Terjadi kesalahan saat memproses REST API: {e}")


# ==================================================================
# RUNNER UTAMA ( testing di main.py )
# ==================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("            PENGUJIAN SELURUH SOAL PRAKTIK")
    print("=" * 60)

    # --- Pengujian Soal 1 ---
    print("\n[SOAL 1] Pengujian Fungsi hitung_statistik()")
    sample_data = [12, 15, 20, 20, 25, 30, 45, 50]
    hasil_stat = hitung_statistik(sample_data)
    for k, v in hasil_stat.items():
        print(f"   - {k.capitalize()}: {v}")

    # --- Pengujian Soal 2 ---
    print("\n[SOAL 2] Pengujian Fungsi validasi_data()")
    schema = {
        "umur": {"type": int, "min": 17, "max": 60},
        "ipk": {"type": float, "min": 0.0, "max": 4.0}
    }
    data_valid = {"umur": 21, "ipk": 3.85}
    is_valid, errs = validasi_data(data_valid, schema, "ModeKetat", debug=True)
    print(f"   Hasil Validasi: {is_valid}, Error: {errs}")

    # --- Pengujian Soal 3 ---
    print("\n[SOAL 3] Pengujian Utilitas Akademik")
    matkul_list = [
        {"nama": "Pemrograman Python", "sks": 3, "nilai": 4.0},
        {"nama": "Struktur Data", "sks": 3, "nilai": 3.5},
        {"nama": "Basis Data", "sks": 4, "nilai": 3.7}
    ]
    transkrip_text = generate_transkrip("Jopan Latue", matkul_list)
    print(transkrip_text)

    # --- Pengujian Soal 4 ---
    print("\n[SOAL 4] Pengujian CRUD Sistem Informasi Mahasiswa (In-Memory)")
    service = MahasiswaService()
    
    # Create
    service.create(MahasiswaModel("2024001", "Ahmad", "Informatika"))
    service.create(MahasiswaModel("2024002", "Siti", "Sistem Informasi"))
    
    # Read
    print("   Data Mahasiswa Saat Ini:", service.read_all())
    
    # Update & Delete
    service.update("2024001", "Ahmad Fauzi", "Teknik Informatika")
    service.delete("2024002")
    print("   Data Mahasiswa Setelah Update & Delete:", service.read_all())

    # --- Pengujian Soal 5 ---
    proses_rest_api()
    
    print("\n" + "=" * 60)
    print("              PENGUJIAN SELESAI")
    print("=" * 60)