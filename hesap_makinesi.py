print("Hesap Makinesine Hoş Geldiniz")
while True:
 sayi1=int(input("Birinci Sayıyı Gir:"))
 sayi2=int(input("İkinci Sayıyı Gir:"))
 toplam=sayi1+sayi2
 print("Toplamı:",toplam)
 cıkar=sayi1-sayi2
 print("Fark:",cıkar)
 carp=sayi1*sayi2
 print("Çarpımı:",carp)
 if sayi2 != 0 :
  bol=sayi1/sayi2
  print("Bölme:",bol)
  print("")
 else:
     print("İkinci Sayı 0'a Bölünemez")
     print("")

