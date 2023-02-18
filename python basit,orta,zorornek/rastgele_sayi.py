import random
sayi=random.randint(1,10)
count=0
kullanici_verisi=0

while (True):
    kullanici_verisi= input("lütfen bir sayi giriniz.")
    count+=1
    if(kullanici_verisi == "cıkıs"):
        print("oyundan ciktiniz")
        break
    kullanici_verisi=int(kullanici_verisi)
    if(kullanici_verisi>sayi):
        print("tahmininizi azaltın")

    elif(kullanici_verisi < sayi):
        print("tahmininizi arttırın")
    else:
        print("doğru cevabı buldunuz")
        print("tahmin sayisi :", str(count))
        break


