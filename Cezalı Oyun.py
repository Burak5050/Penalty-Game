import os

print("\t\t\t\t\t\t\tCezalı Oyuna HOŞGELDİNİZ!")

Vote = {"Başla" :1}
print(f"\n\t\t\t\t\t\t\t{Vote}")
Vote_Playing = {"Nasıl Oynanır" :2}

print(f"\n\t\t\t\t\t\t\t{Vote_Playing}")
Vote_Qarition = {"Kurallar" :3}

print(f"\n\t\t\t\t\t\t\t{Vote_Qarition}")
Vote_Excit = {"Çıkış" :4}
try: 
 
 Vote_1  = int(input("\nSeçim: "))

except ValueError :
    print("--"*20)
    print("Hata: STR girmeyin")

if Vote_1 <=0 or Vote_1 >4 :
   print("--")
   print("Hata: Geçerli işlem yapın")


if Vote_1 == 1 :
    print("\nCeza: kullandığınız cihaz kapatılacak")
    print("--"*20)
    try :
     
     Qestion_1 = str(input("Makine diline en yakın dil hangisidir\n"))
    
    except ValueError :
        print("Hata: İNT girmeyin")

    if Qestion_1 == "C++" or Qestion_1 == "c++":
        print("--"*20)
        print("TEBRİKLER! ")
        print("\nYeni soru")

        print("\nCeza: Kullandığınız cihaz YENİDEN BAŞLATILACAK")
        print("--"*20)
        try:
         
         Qestion_2 = int(input("Osmanlı hangi yılda yıkılmıştır\n"))
        
        except ValueError :
           print("Hata: STR girmeyin")

        if Qestion_2 == 1922 :
            print("--"*20)
            print("TEBRİKLER!")
            print("\nYeni Soru")

            print("\nCeza: Uygulamadan çıkış")
            print("--"*20)
            try:
            
             Qestion_3 = int(input("Python hangi yılda çıktı\n"))

            except ValueError :
               print("Hata: STR girmeyin")


            if Qestion_3 == 1991 :
                print("--"*20)
                print("TEBRİKLER!")
                print("\nYeni Soru")

                print("\nCeza: Kullandığınız cihazın Wi-Fi si kapatılacak")
                print("--"*20)
                try:
                   
                   Qestion_4 = int(input("İlk bilgisayar hangi yılda çıktı: "))

                except ValueError :
                   print("Hata: STR girmeyin")


                if Qestion_4 == 1944 :
                   print("--"*20)
                   print("TEBRİKLER!")
                   print("\nYeni Soru")

                   Qestion_5 = int(input(""))

                
                elif Qestion_4 != 1944 :
                   print("--"*20)
                   os.system("ipconfig /release")
                   print("Wi-Fi kapatıldı")


            elif Qestion_3 != 1991 :
                print("--"*20)
                print("Uygulamadan çıkılıyor...")


        elif Qestion_2 != 1922 :
            print("Kullandığın cihaz YENİDEN BAŞLATILACAK")
            os.system("shutdown /r /t 0") 
        
    elif Qestion_1 != "C++" :
        print("\nKapatılıyor")
        os.system("shutdown /s /t 0")
    

elif Vote_1 == 2 :
    print("\t\t\t\t\t\tKURALLAR")

    print("1.Kural :Metin belgesine int girmeyin")
    print("--"*20)
    print("2.Kural :Sayı belgesine str girmeyin")

elif Vote_1 == 3 :
    print("\t\t\t\t\tNasıl Oynanır ?")
    print("--"*20)
    print("1.Adım: Kullanıcıya soru sorulur")
    print("--"*20)
    print("2.Adım: Kullanıcı eğer sorulan soruya DOĞRU cevap verer ise ceza uygulanmaz ve yeni soruya geçilir")
    print("--"*50)
    print("3.Adım: Kullancı eğer sorulan soruya YANLIŞ cevap verir ise ceza uyguşanır ve yeni soruya geçilir")
    print("--"*50)
    print("\t\t\t\t\tUygulanan CEZA'lar")
    print("--"*20)
    print("1.Ceza: Kullanılan cihazı KAPAT")
    print("--"*20)
    print("2.Ceza: Kullandığın cihazı YENİDEN BAŞLAT")
    print("--"*20)
    print("3.Ceza: Kullanılan cihazın Wı-Fi kapatma")
    print("--"*20)
    print("4.Ceza: Arka plandaki uygulamaları kapatma")

elif Vote_1 == 4 :
    print("--"*20)
    print("\nÇıkış yapılıyor...")