class Kitap:

    def __init__(self, baslik, yazar, isbn):  #yapıcı metot constructure
        self.baslik = baslik
        self.yazar = yazar
        self.isbn = isbn
        self.odunc_verildi_mi = False
        #self: şu anda üzerinde çalışılan nesnenin kendisi

    def odunc_ver(self):
        if self.odunc_verildi_mi:
            print(f"'{self.baslik}' zaten ödünçte.")
        else:
            self.odunc_verildi_mi = True
            print(f"'{self.baslik}' ödünç verildi.")

    def iade_al(self):
        if not self.odunc_verildi_mi:
            print(f"'{self.baslik}' zaten rafta.")
        else:
            self.odunc_verildi_mi = False
            print(f"'{self.baslik}' iade alındı.")

    def __str__(self):
        durum = "Ödünçte" if self.odunc_verildi_mi else "Rafta"
        return f"{self.baslik} - {self.yazar}  ({durum})"
     