class Kitap:

    def __init__(self,name,writer):
        self.name=name
        self.writer=writer

    def __str__(self):
        return f"{self.name} - {self.writer}"
    
kitaplarsss=[]

def kitapEkle(kitapName, yazar):
    p1=Kitap(kitapName,yazar)
    kitaplarsss.append(p1)
    
def kitaplarıListele():

    if len(kitaplarsss)<1:
        print("Henüz listelenecek bir kitap yok!")
    else:
        for i in range(len(kitaplarsss)):
            print(f"{i+1} - {kitaplarsss[i]}")

def kitapSil():
    if len(kitaplarsss)<1:
        print("Henüz silenecek bir kitap yok!")
    
    else:
        print("Hangi kitabı silmek istiyorsunuz?")

        sayac=1
        for i in kitaplarsss:
            print(f"{sayac} - {kitaplarsss[sayac-1]}")

            sayac+=1

        while True:
            x=input()

            try:
                silinecekKitap=int(x)

                if(0<silinecekKitap<=len(kitaplarsss)):
                    break
            except Exception:
                pass

        
        del kitaplarsss[silinecekKitap-1] # indexi ile o kitabı sildik
        print("Kitap başarıyla silindi!")

def kitapAra():

    if len(kitaplarsss)<1:
        print("Kütüphanede mevcut kitap yok!")
    
    else:
        aranacakKitap=input("Aranacak kitap: ")

        varMı=False

        for x in kitaplarsss:
            if aranacakKitap.lower()==x.name.lower():
                varMı=True
        
        if varMı:
            print("Aradığınız kitap mevcut!")
        else:
            print("maalesef aradağınız kitap mevcut değil!")

def kitapGuncelle():

    if len(kitaplarsss)<1:
        print("Güncellenecek kitap yok!")
    
    else:
        kitaplarıListele()
        print("Hangi kitabı güncellemek istersiniz?")

        while True:
                x=input()

                try:
                    guncellenecekKitap=int(x)

                    if(0<guncellenecekKitap<=len(kitaplarsss)):
                        break
                except Exception:
                    pass
        
        guncellenecekİsim=input(f"Kitabın ismi ne ile değiştirilsin({kitaplarsss[guncellenecekKitap-1].name}): ")
        guncellenecekYazar=input(f"Kitabın yazarı ne ile değiştirilsin({kitaplarsss[guncellenecekKitap-1].writer}): ")

        kitaplarsss[guncellenecekKitap-1].name=guncellenecekİsim
        kitaplarsss[guncellenecekKitap-1].writer=guncellenecekYazar

        print("Kitap başarı ile güncellendi!")
    



# menü
while True:

    print("Kütüphanemize hoşgeldiniz!".center(51,"*"))

    print("[1] - Kitap Ekle\n[2] - Kitap Sil\n[3] - Kitapları Listele\n[4] - Kitap Ara\n[5] - Kitap Güncelle\n[6] - Çıkış")



    while True:
        x=input()

        try:
            secim=int(x)

            if not 0<secim<7:
                continue

            break
        except Exception:
            pass

    if secim==1:
        kitapName=input("Kitap ismi: ")
        yazar=input("Yazar ismi: ")
        kitapEkle(kitapName,yazar)
    if secim==2:
        kitapSil()
    if secim==3:
        kitaplarıListele()
    if secim==4:
        kitapAra()
    if secim==5:
        kitapGuncelle()
    if secim==6:
        print("Görüşmek üzere!")
        break

