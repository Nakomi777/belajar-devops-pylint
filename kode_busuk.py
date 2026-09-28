"""Modul sederhana untuk melakukan operasi penjumlahan dua angka."""


def tambah_dua_angka(angka_pertama, angka_kedua):
    """Menghitung dan menampilkan hasil penjumlahan dua angka.

    Args:
        angka_pertama: Angka pertama yang akan dijumlahkan.
        angka_kedua: Angka kedua yang akan dijumlahkan.

    Returns:
        Hasil penjumlahan angka_pertama dan angka_kedua.
    """
    hasil = angka_pertama + angka_kedua
    print(hasil)
    return hasil


if __name__ == "__main__":
    tambah_dua_angka(1, 2)