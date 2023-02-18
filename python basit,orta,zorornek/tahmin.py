from random import choice
while True:
    print("#" * 80)
    print("#" * 30 + "Kelime Tahmin Oyunu" + "#" * 29)
    print("#" * 80)

    kelime=choice(["almanya","turkiye","ispanya","irlanda","kuba","meksika","rusya","fransa","ingiltre","mısır","japonya","kore"])
    kelime=kelime.upper()
    harf_sayisi=len(kelime)
    print("kelimeniz {} harflidir".format(harf_sayisi))

    tahminler = []
    hata= []
    deneme=7

    while deneme > 0 :
        tabela= ""
        for harf in kelime :
            if harf in tahminler:
                tabela = tabela + harf
            else:
                tabela = tabela + "_"

        if tabela == kelime:
            print("kelimeyi buldunuz tebrikler")
            break

        print("Kelimeyi Tahmin Ediniz", tabela)
        print(deneme, "CANIN VAR!")

        tahmin = input("Bir Harf Giriniz\n>>>>")
        tahmin = tahmin.upper()

        if tahmin== kelime:
            print("dogru bildin")
            break

        if tahmin in tahminler or tahmin in hata:

            print("{} daha önce söylendi. Lütfen başka bir harf söyleyin.".format(tahmin))

        elif tahmin in kelime:
            rpt=kelime.count(tahmin)
            print("Doğru!, {0} harfi kelimemiz içerisinde {1} kere geçiyor.".format(tahmin, rpt))
            tahminler.append(tahmin)
        else:
            print("Yanlış!, Kelimede bu harf yok. ")
            hata = hata.append(tahmin)
            deneme=deneme-1
    if deneme == 0:
            print("Hiç Hakkınız Kalmadı. Başaramadın. ")
            print("Kelimemiz {}".format(kelime))

    print("Oyundan Çıkmak İstiyorsanız \n',' Tuşuna Basınız.\Devam Etmek İçin Herhangi Bir Başka Tuşa Basınız.")
    devam=input("<<>>>")
    devam=devam.upper()
    if devam=="," :
        break
    else:
        continue