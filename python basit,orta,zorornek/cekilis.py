import random
liste=[]
print("cekilisi baslatmak icin 'baslat' basınız,\n iptal etmek icin 'iptal' yaz.")
while True:
    try:
        giris=input("cekilese katılacak kisiler")
        if giris=="iptal":
            sor=input("kisiyi mi iptal edeceksin (kisi)yoksa cekilisi  iptal edeceksin (cekilis)")
            if sor=="kisi":
                sor_1=input("kimi iptal edeceksiniz")
                if sor_1 in liste:
                    yer=liste.index(sor_1)
                    liste.pop(yer)
                    print(liste)
                else:
                    print("listede girdiginiz kisi yok")
                    print(liste)

            elif sor== "cekilis":
                try:
                    while True:
                        liste.pop()
                except:
                    print("cekilis iptal edilmistir")

        elif giris=="baslat":
            sor_2=int(input("kac kimi kazanacak"))
            sonuc=random.sample(liste,sor_2)

            if len(liste)<sor_2 :
                print("kazanılacak kisi sayısı girilen sayidan fazla olamaz")
                print("tekrar deneyin")

            else:
             print("kazananlar:",sonuc)
        else:
            liste.append(giris)
    except:
        print("hatalı giris yaptınız Lutfern tekrar deneyin")