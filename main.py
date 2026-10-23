from src.kutuphane.kitap import Kitap

kitap1 = Kitap("Sefiller", "Victor Hugo", 487, "978-975-07-0001-1")
kitap2 = Kitap("Suç ve Ceza", "Dostoyevski", 950,"978-975-07-0002-8")

print(kitap1)
print(kitap2)
kitap1.odunc_ver()
kitap1.odunc_ver()   # ikinci kez dene
print(kitap1)
kitap1.iade_al()
print(kitap1)
