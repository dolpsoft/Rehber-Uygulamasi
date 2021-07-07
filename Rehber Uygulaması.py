import time
print ("Rehber Uygulaması v0.1")
print ("-"*70)
print("Kişileriniz:")       
kisiler = {"Mehmet Kaya":["Tel No:0xxx xxx xx xx"], 'Ahmet Dost':["Tel No:0xxx xxx"], 'Tuğçe İskender':["Tel No:0xxx xxx"]}

for key,value in kisiler.items():
    print(key, value)
print("-"*70)
while True:
    sec= int(input("Ne yapmak istiyorsunuz?\n1-Kişi Ekleme\n2-Kişi Silme\n3-Arama Yapma\n4-Rehberi Kapat\n\nYapmak istediğiniz işlemin numarasını buraya yazın: "))
    print ("-"*70)
    if sec== 1:
        isimekle= input("Kişi ekleme işlemini seçtiniz. Eklemek istediğiniz kişinin adını ve telefon numarasını doğru bir şekilde yazın:\nKişi Adı: ")
        telNoekle= input("Tel No: ")
        kisiler[isimekle]=["Tel No:"+""+telNoekle]
        print("-"*70)
        print("Değişiklikler sonucu oluşan yeni kişi listesi: ")
        print("-"*70)
        for key,value in kisiler.items():
          print(key, value)
        print("-"*70)
        print("Bilgi: Oluşturduğunuz yeni kişi, kişilerinize eklendi. Aşağıdan yeni bir işlem yapabilir veya uygulamadan çıkabilirsiniz.")
        print("-"*70)
        
        
    elif sec== 2:
        isimsilme=input("Kişi silme işlemini seçtiniz.\nSilmek İstediğiniz Kişinin Adını Doğru Bir Şekilde Yazınız: ")
        
        kisiler.pop(isimsilme)
        print("-"*70)
        print("Değişiklikler sonucu oluşan yeni kişi listesi: ")
        print("-"*70)
        for key,value in kisiler.items():
          print(key, value)
        print ("-"*70)
        print("Bilgi: Adını yazdığınız kişi rehberinizden kaldırılmıştır. Aşağıdan yeni bir işlem yapabilir veya uygulamadan çıkabilirsiniz.")
        print("-"*70)
        
        
     
    elif sec==3:
        print("Kişileriniz:")
        print("-"*70)
        for key,value in kisiler.items():
          print(key, value)
        print("-"*70)
        
        aranacakKisi=input ("Lütfen aramak istediğiniz kişinin listedeki adını veya listede bulunmayan herhangi bir kişinin numarasını doğru bir şekilde yazınız: ")
     
        
        print(aranacakKisi, "aranıyor...")  
        print("-")
        time.sleep(0.5)
        print("-")
        time.sleep(0.5)
        print("-")
        time.sleep(0.5)
        print(aranacakKisi,"adlı kişiye/numaraya bağlanıldı.")
        aramayiBitir=int(input("Aramayı bitirmek için 1 yazabilirsiniz: "))
        
        
        if aramayiBitir==1:
         print("-"*70)
         print ("Arama bitirildi.Aşağıdan yeni bir işlem yapabilir veya uygulamadan çıkabilirsiniz.")
        
        
    else:
        print("Rehberi kapatmayı seçtiniz. Uygulamadan çıkıldı.")
        break