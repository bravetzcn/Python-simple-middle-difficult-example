import random
secenek = ["tas", "kagit", "makas"]
tas = secenek[0]
kagit = secenek[1]
makas = secenek[2]
print("tas ,kagıt,makas oyununa hosgeldiniz")
print("oyunu bitirmek için e tuşuna basın")
while True:
    secim = input("lutfen bir el hareketi secin :")
    bil_sec = random.choice(secenek)
    if secim == tas:
        if bil_sec == tas:
            print("bilgisayarın secimi tastır.")
            print("Berabere")
        elif bil_sec == kagit:
            print("bilgisayarın secimi kagıtdır.")
            print("kaybettiniz")
        else:
            print("bilgisayarın secimi makastır.")
            print("kazandınız")

    if secim == kagit:
        if bil_sec == tas:
            print("bilgisayarın secimi tastır.")
            print("kazandın")
        elif bil_sec == kagit:
            print("bilgisayarın secimi kagıtdır.")
            print("berabere")
        else:
            print("bilgisayarın secimi makastır.")
            print("kaybettin")

    if secim == makas:
        if bil_sec == tas:
            print("bilgisayarın secimi tastır.")
            print("kaybettin")
        elif bil_sec == kagit:
            print("bilgisayarın secimi kagıtdır.")
            print("kazandın")
        else:
            print("bilgisayarın secimi makastır.")
            print("berabere")

    if secim == "e":
        print("oyundan cıktınız.")
        break


