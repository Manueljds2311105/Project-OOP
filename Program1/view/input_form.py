class InputForm:
    @staticmethod
    def input_data():
        nama = input("Nama: ")
        nim = input("NIM: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        return nama, nim, tugas, uts, uas
