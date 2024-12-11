class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitung_nilai_akhir(self):
        return (self.tugas * 0.3) + (self.uts * 0.35) + (self.uas * 0.35)

class DataMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, nama, nim, tugas, uts, uas):
        self.data_mahasiswa[nama] = Mahasiswa(nama, nim, tugas, uts, uas)

    def hapus(self, nama):
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]

    def ubah(self, nama_lama, nama_baru, nim, tugas, uts, uas):
        if nama_lama in self.data_mahasiswa:
            del self.data_mahasiswa[nama_lama]
            self.data_mahasiswa[nama_baru] = Mahasiswa(nama_baru, nim, tugas, uts, uas)

    def tampilkan_semua(self):
        return self.data_mahasiswa