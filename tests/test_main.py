import pytest
from src.models import DaftarMahasiswa, Mahasiswa


class TestMahasiswa:
    def test_buat_mahasiswa_valid(self):
        mhs = Mahasiswa(
            "2024SI001", "Andi Pratama", "Sistem Informasi", 2024, 3.50
        )
        assert mhs.nim == "2024SI001"
        assert mhs.ipk == 3.50

    def test_nim_tidak_valid(self):
        with pytest.raises(ValueError):
            Mahasiswa("abc", "Test", "SI", 2024, 3.0)

    def test_ipk_diluar_range(self):
        with pytest.raises(ValueError):
            Mahasiswa("2024SI002", "Test", "SI", 2024, 5.0)


class TestDaftarMahasiswa:
    def test_tambah_dan_cari(self):
        db = DaftarMahasiswa()
        mhs = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        db.tambah(mhs)
        assert db.cari("2024SI001") == mhs
        assert db.jumlah == 1

    def test_nim_duplikat(self):
        db = DaftarMahasiswa()
        m1 = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        m2 = Mahasiswa("2024SI001", "Budi", "SI", 2024)
        db.tambah(m1)
        with pytest.raises(ValueError):
            db.tambah(m2)  