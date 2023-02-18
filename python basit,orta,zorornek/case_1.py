print("kullanıcı adı oluşturma programına hoşgeldiniz.")
print ("nasıl bir kulanıcı adı istediğinizi seçeneklerde belirtin.")
"""
1) isim,soyisim ve sanslı sayısını içeren bir kullanıcı adı
2)ugurlu rakam ve bir kahraman içeren
3)en sevdiği hayvan ve doğum yılı
"""
secenek=int(input("lütden bir secenek giriniz :"))

if secenek == 1:
    isim = input("isminizi girin")
    soy_isim = input("soyisminizi girin")
    sans_sayi = input("sanslı ssayinizi giriniz.")
    kullanici_adi= isim+'_'+soy_isim+'.'+sans_sayi
    print( kullanici_adi)

elif secenek == 2:
    kahraman =input("sevdiginiz bir kahraman girin")
    ugur_sayi =input("ugurlu sayinizi girin")
    kullanici_adi = kahraman+'_'+ugur_sayi
    print( kullanici_adi)

elif   secenek == 3:
    hayvan=input("sevdiginiz bir hayvan girin")
    dogum_yili=input("dogum yilinizi girin")
    kullanici_adi = hayvan+'_' + dogum_yili
    print(kullanici_adi)

else:
    print("dogru secenek girmediniz.Lutfen tekrar deneyiniz.")


