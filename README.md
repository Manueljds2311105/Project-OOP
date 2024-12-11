# Project-OOP

Nama: Manuel Johansen Dolok Saribu

Kelas: Ti.24.A.5

NIM: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.

Mata Kuliah: Bahasa Pemograman

## Penjelasan 
1. Class Mahasiswa
Penjelasan:
- Class ini digunakan untuk merepresentasikan data individu mahasiswa, dengan atribut dan method sebagai berikut:
  - Atribut:
    - nama: Nama mahasiswa.
    - nim: Nomor Induk Mahasiswa.
    - tugas: Nilai tugas mahasiswa.
    - uts: Nilai Ujian Tengah Semester.
    - uas: Nilai Ujian Akhir Semester.
  - Method:
    - hitung_nilai_akhir(): Menghitung nilai akhir berdasarkan formula:
      ```python
      nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
      ```
2. Class DataMahasiswa
- Penjelasan: Class ini bertindak sebagai wadah (container) untuk mengelola data mahasiswa dalam bentuk dictionary.
  - Atribut:
    - data_mahasiswa: Dictionary untuk menyimpan data mahasiswa dengan struktur:
    ```python
    {
    "Nama": Mahasiswa(nama, nim, tugas, uts, uas)
    }
    ```
  - Method:
    - tambah(nama, nim, tugas, uts, uas): Menambahkan data mahasiswa baru ke dictionary.
    - hapus(nama): Menghapus data mahasiswa berdasarkan nama.
    - ubah(nama_lama, nama_baru, nim, tugas, uts, uas): Mengubah data mahasiswa (termasuk nama, jika diperlukan).
    - tampilkan_semua(): Mengembalikan seluruh data mahasiswa.
3. Class InputForm
- Penjelasan: Class ini menyediakan method untuk mengambil input data mahasiswa dari pengguna.
  - Method:
    -input_data(): Mengambil input nama, NIM, nilai tugas, UTS, dan UAS, lalu mengembalikan data tersebut sebagai tuple.
4. Class ViewMahasiswa
- Penjelasan: Class ini digunakan untuk menampilkan data mahasiswa dalam format tabel di konsol.
  - Method:
    - tampilkan_daftar(data_mahasiswa): Menampilkan data mahasiswa dalam format tabel jika ada data. Jika tidak, menampilkan pesan bahwa data kosong.
5. File main.py
- Penjelasan: File ini adalah program utama yang menghubungkan seluruh class di atas.
  - Fitur:
    - Menu:
      - (L)ihat: Menampilkan daftar data mahasiswa.
      - (T)ambah: Menambahkan data mahasiswa baru.
      - (U)bah: Mengubah data mahasiswa yang ada.
      - (H)apus: Menghapus data mahasiswa berdasarkan nama.
      - (K)eluar: Keluar dari program.
  - Implementasi:
    - Menggunakan loop untuk memberikan menu pilihan kepada pengguna.
    - Setiap pilihan memanggil method yang sesuai dari class DataMahasiswa, InputForm, dan ViewMahasiswa.
## Hasil Eksekusi
![foto](https://github.com/Manueljds2311105/foto/blob/9f95b3790df7d85fc34470426800fd57d285961c/main.py%20-%20Program1%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2012_11_2024%2011_32_47%20AM.png)
![foto](https://github.com/Manueljds2311105/foto/blob/9f95b3790df7d85fc34470426800fd57d285961c/main.py%20-%20Program1%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2012_11_2024%2011_34_15%20AM.png)
## Diagram Class
![foto](https://github.com/Manueljds2311105/foto/blob/cc265bec61dbca3351d7da52aa25a21d2d6c2cdd/DataMahasiswa_ClassDiagram.png)
## Flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/88e09d3843bd69e519573af4172ff3c263253713/lab8.drawio.png)
