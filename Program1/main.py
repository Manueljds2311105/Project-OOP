from data.mahasiswa import DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

data = DataMahasiswa()

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == 'l':
        ViewMahasiswa.tampilkan_daftar(data.tampilkan_semua())
    elif pilihan == 't':
        nama, nim, tugas, uts, uas = InputForm.input_data()
        data.tambah(nama, nim, tugas, uts, uas)
    elif pilihan == 'u':
        nama_lama = input("Masukkan Nama Lama: ")
        if nama_lama in data.tampilkan_semua():
            nama_baru, nim, tugas, uts, uas = InputForm.input_data()
            data.ubah(nama_lama, nama_baru, nim, tugas, uts, uas)
        else:
            print("Data dengan Nama tersebut tidak ditemukan!")
    elif pilihan == 'h':
        nama = input("Masukkan Nama: ")
        if nama in data.tampilkan_semua():
            data.hapus(nama)
            print("Data berhasil dihapus!")
        else:
            print("Data dengan Nama tersebut tidak ditemukan!")
    elif pilihan == 'k':
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid, silakan pilih menu yang tersedia.")
