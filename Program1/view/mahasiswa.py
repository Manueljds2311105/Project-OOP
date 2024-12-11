class ViewMahasiswa:
    @staticmethod
    def tampilkan_daftar(data_mahasiswa):
        if data_mahasiswa:
            print("\nDaftar Nilai")
            print("=" * 66)
            print("| NO |       NAMA      |    NIM    | TUGAS | UTS | UAS |  AKHIR  |")
            print("=" * 66)
            for no, (nama, mahasiswa) in enumerate(data_mahasiswa.items(), start=1):
                nilai_akhir = mahasiswa.hitung_nilai_akhir()
                print(f"| {no:<2} | {nama:<15} | {mahasiswa.nim:<8} | {mahasiswa.tugas:<5.0f} | {mahasiswa.uts:<3.0f} | {mahasiswa.uas:<3.0f} | {nilai_akhir:<7.2f} |")
            print("=" * 66)
        else:
            print("\nDaftar Nilai")
            print("=" * 61)
            print("| NO |    NAMA    |    NIM    | TUGAS | UTS | UAS |  AKHIR  |")
            print("=" * 61)
            print("|                       TIDAK ADA DATA                      |")
            print("=" * 61)