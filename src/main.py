from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from src.models import DaftarMahasiswa, Mahasiswa

console = Console()
db = DaftarMahasiswa()


def tampilkan_menu():
    """Tampilkan menu utama."""
    menu_text = (
        "[bold cyan]Sistem Informasi Mahasiswa[/]\n\n"
        "1. Tambah Mahasiswa\n"
        "2. Tampilkan Semua Mahasiswa\n"
        "3. Cari Mahasiswa (NIM)\n"
        "4. Hapus Mahasiswa\n"
        "0. Keluar"
    )
    console.print(Panel(menu_text, title="Menu", border_style="cyan"))


def tambah_mahasiswa():
    """Form tambah mahasiswa baru."""
    console.print("\n[bold]Tambah Mahasiswa Baru[/]")
    nim = console.input("  NIM: ").strip()
    nama = console.input("  Nama: ").strip()
    prodi = console.input("  Program Studi: ").strip()

    try:
        angkatan = int(console.input("  Angkatan: "))
        ipk = float(console.input("  IPK: "))

        mhs = Mahasiswa(nim, nama, prodi, angkatan, ipk)
        db.tambah(mhs)
        console.print(f"  [green]Berhasil: {nama} ditambahkan[/]\n")
    except ValueError as e:
        console.print(f"  [red]Gagal: {e}[/]\n")


def tampilkan_semua():
    """Tampilkan seluruh data dalam tabel."""
    if not db.data:
        console.print("\n[yellow]Belum ada data mahasiswa.[/]\n")
        return

    table = Table(title=f"Daftar Mahasiswa (Total: {db.jumlah})")
    table.add_column("NIM", style="cyan")
    table.add_column("Nama")
    table.add_column("Program Studi")
    table.add_column("Angkatan", justify="right")
    table.add_column("IPK", justify="right")

    for m in db.data:
        table.add_row(
            m.nim, m.nama, m.program_studi, str(m.angkatan), f"{m.ipk:.2f}"
        )

    console.print(table)
    console.print()


def cari_mahasiswa():
    """Cari mahasiswa berdasarkan NIM."""
    console.print("\n[bold]Cari Mahasiswa[/]")
    nim = console.input("  Masukkan NIM: ").strip()
    mhs = db.cari(nim)

    if mhs:
        console.print("\n[green]Data Ditemukan:[/]")
        console.print(f"  NIM           : [cyan]{mhs.nim}[/]")
        console.print(f"  Nama          : {mhs.nama}")
        console.print(f"  Program Studi : {mhs.program_studi}")
        console.print(f"  Angkatan      : {mhs.angkatan}")
        console.print(f"  IPK           : {mhs.ipk:.2f}\n")
    else:
        console.print(
            f"  [red]Mahasiswa dengan NIM '{nim}' tidak ditemukan.[/]\n"
        )


def hapus_mahasiswa():
    """Hapus mahasiswa berdasarkan NIM."""
    console.print("\n[bold]Hapus Mahasiswa[/]")
    nim = console.input("  Masukkan NIM yang akan dihapus: ").strip()

    if db.hapus(nim):
        console.print(
            f"  [green]Mahasiswa dengan NIM '{nim}' berhasil dihapus.[/]\n"
        )
    else:
        console.print(
            f"  [red]Gagal: NIM '{nim}' tidak ditemukan.[/]\n"
        )


def main():
    """Loop utama aplikasi."""
    while True:
        tampilkan_menu()
        pilihan = console.input("\nPilih [0-4]: ").strip()

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "0":
            console.print("[bold]Sampai jumpa![/]")
            break
        else:
            console.print("[red]Pilihan tidak valid![/]\n")


if __name__ == "__main__":
    main()