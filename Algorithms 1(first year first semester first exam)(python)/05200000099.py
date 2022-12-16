# Arda Bozkurt - 05200000099
# Sabit Değerlerin Yazımı
ASGARİ_ÜCRET = 2324.70  #Asgari ücret
TABAN_DEĞER = 1     # Danışman sayısı kontrolü için kullanılan değer
KOTA_FARKI = 10     # Komisyon hesaplaması için kota yüzdesi
TABAN_BEDEL = 1     # Satış ve kiralama bedeli için kontrol sabiti ayrıca ortalama için kullanılan sabit
YÜZDE = 100      # Yüzde hesabı için sabit
KOMİSYON_SATIŞ_DEĞERİ = 4       # Satış bedelinin komisyon için yüzdesi
PRİM_DEĞERİ = 10        # Komisyon hesabının prim için yüzdesi
İKRAMİYE = ASGARİ_ÜCRET / 2     # İkramiye için asgari ücretin yarısı
KİRA_ADEDİ_SINIR = 10       # 10dan fazla kiralanmış emlak sabiti
KİRA_BEDELİ_SINIR = 25000   #25000tlden fazla kiralanmış emlak sabiti
# Değişken Değerlerin Yazımı
danışman_sayacı = 0     # Kaç danışman olduğunu sayan değişken
genel_konut_satılma_sayısı = 0      # Bütün konutların satılma sayısını hesaplayan değişken
genel_arsa_satılma_sayısı = 0       # Bütün arsaların satılma sayısını hesaplayan değişken
genel_işyeri_satılma_sayısı = 0     # Bütün iş yerlerinin satılma sayısını hesaplayan değişken
genel_konut_kiralanma_sayısı = 0    # Bütün konutların kiralanma sayısını hesaplayan değişken
genel_arsa_kiralanma_sayısı = 0     # Bütün arsaların kiralanma sayısını hesaplayan değişken
genel_işyeri_kiralanma_sayısı = 0   # Bütün iş yerlerinin kiralanma sayısını hesaplayan değişken
genel_konut_satılma_bedeli = 0      # Bütün konutların satılma bedelini hesaplayan değişken
genel_arsa_satılma_bedeli = 0       # Bütün arsaların satılma bedelini hesaplayan değişken
genel_işyeri_satılma_bedeli = 0     # Bütün iş yerlerinin satılma bedelini hesaplayan değişken
genel_en_yüksek_satış = 0       # En yüksek bedelli satışın bedelini veren değişken
genel_en_yüksek_satışı_yapan = ''    # En yüksek bedelli satışı kimin yaptığını veren değişken
genel_en_yüksek_satılan_emlak = ''   # En yüksek bedelli satışın hangi emlak türü olduğunu veren değişken
genel_en_yüksek_konut_kira = 0      # En yüksek kiralı konutun kira bedelini veren değişken
genel_en_yüksek_konut_kira_yapan = ''   # En yüksek kiralı konutu kimin kiraladığını vereen değişken
asgariden_yüksek_bedelli_kira_konut_sayısı = 0  # Asgari ücretten fazla kiralı olan konutların sayısını veren değişken
hiç_satamayan_danışman = 0      # Hiç emlak satamayan danışmanların sayısını veren değişken
en_yüksek_toplam_satış_bedeli = 0   # En fazla toplam bedelli satış yapan danışmanın yaptığı satış bedeli
en_yüksek_toplam_satış_bedeli_danışman = '' # En fazla toplam bedelli satış yapan danışmanın adı
en_yüksek_toplam_satış_bedeli_adedi = 0 # En fazla toplam bedelli satış yapan danışmanın yaptığı satış adedi
en_yüksek_toplam_satış_adedi = 0    # En fazla toplam adetli satışı yapan danışmanın satış adedi
en_yüksek_toplam_satış_adedi_danışman = ''  # En fazla toplam adetli satışı yapan danışmanın adı
en_yüksek_toplam_satış_adedi_bedeli = 0 # En fazla toplam adetli satışı yapan danışmanın yaptığı toplam satış bedeli
kotayı_dolduran_sayacı = 0  # Kotayı dolduran danışmanları sayan değişken
primi_fazla_olanlar = 0     # Primi maaşından fazla olan danışmanalrı sayan değişken
fazla_kiralayan_danışmanlar = 0  # KİRA_ADEDİ_SINIR veya KİRA_BEDELİ_SINIR sınırlarını geçen danışmanları sayan değişken
en_yüksek_prim = 0      # En yüksek primi hesaplayan değişken
en_yüksek_primi_alan_danışman = ''    # En yüksek primi kimin aldığını söyleyen değişken
en_yüksek_primi_alan_danışmanın_maaşı = 0     # En yüksek primi alan danışmanın aldığı maaşı veren değişken
en_yüksek_primi_alan_danışmanın_toplam_ücreti = 0  # En yüksek primi alan danışmanın aldığı toplam ücreti veren değişken
en_düşük_prim = None        # En düşük prim için başlangıç değeri
en_düşük_primi_alan_danışman = ''       # En düşük primi alan danışmanın adinı veren değişken
en_düşük_primi_alan_danışmanın_maaşı = 0    # En düşük primi alan danışmanın aldığı maaşı veren değişken
en_düşük_primi_alan_danışmanın_toplam_ücreti = 0   # En düşük primi alan danışmanın aldığı toplam ücreti veren değişken
acentenin_ödeyeceği_toplam_Ücret = 0    # Acentenin danışmanlarına ödeyeceği toplam ücreti hesaplayan değişken
genel_emlak_komisyonu = 0       # Emlak acentesinin kazanacağı toplam komisyonu hesaplayan değişken


def ortalamaBulma(veri1, veri2, yüzde):     # Ortalama ve yüzde hesaplamaları için kullanılan fonksiyon
    ortalama = veri1/veri2*yüzde    # Ortalama hesaplanır
    return ortalama     # İşleme katılması için geri döndürülür


def yanlışVeriKontorlü(alt_sınır, veri):    # "Yanlış veri girildi mi?" diye bakan fonksiyon
    while veri < alt_sınır:     # Girilen değerin alt ve üst sınırlar içinde olup olmadığına bakılır
        veri = int(input("Hatalı veri girdiniz tekrar deneyin:"))   # Değer uymuyorsa kullanıcıdan tekrar istenir
    return veri


emlak_danışmanı_sayısı = int(input("Acentede çalışan danışman sayısını giriniz."))  # Kullanıcıdan danışman sayısı alınır
emlak_danışmanı_sayısı = yanlışVeriKontorlü(TABAN_DEĞER, emlak_danışmanı_sayısı)     # Veri fonksiyon ile kontrol edilir
for i in range(emlak_danışmanı_sayısı):     # Girilen danışman sayısı kadar döndürülmesi için döngü olurşuturulur
    # Her döngüde değişmesi gereken değişkenler
    bireysel_kira_konut_sayacı = 0  # Danışmana özel kiralanan konut sayacı
    bireysel_kira_konut_toplam = 0  # Danışmana özel kiralanan toplam konut bedeli değişkeni
    bireysel_en_yüksek_konut_kira = 0   # Danışmana özel kiralanan en pahalı konutun bedelini veren değişken
    bireysel_konut_toplam = 0   # Danışmana özel satılan konutların bedelleri toplamı
    bireysel_arsa_toplam = 0    # Danışmana özel satılan arsaların bedelleri toplamı
    bireysel_işyeri_toplam = 0  # Danışmana özel satılan iş yerlerinin bedelleri toplamı
    bireysel_satış_toplam = 0   # Danışmana özel satılan emlakların bedelleri toplamı
    bireysel_kira_toplam = 0    # Danışmana özel kiralanan emlakalrın bedelleri toplamı
    bireysel_satılan_sayısı = 0     # Danışmana özel satılan emlakların sayısı
    bireysel_kiralanan_sayısı = 0   # Danışmana özel kiralanan emlakların sayısı
    başka_emlağı_var_mı = 'e'       # Bir sonraki döngünün devamı için gerekli olan değer
    danışman_sayacı += 1        # Danışmanları sayan değişken
    ad = input(str(danışman_sayacı) + ". çalışanın adını ve soyadını giriniz: ")   # Kullanıcıdan isim için alınan girdi
    maaş = int(input(str(ad) + " isimli çalışanın aylık maaşını giriniz(Asgari ücret veya daha fazlası)(TL):"))     # Kullanıcıdan maaş için alınan girdi
    maaş = yanlışVeriKontorlü(ASGARİ_ÜCRET, maaş)      # Maaş girdisinin kontrolünü yapan fonksiyon
    KOTAKONTROL = maaş * KOTA_FARKI     # Kota sınırı için hesaplanan değer
    kota = int(input(str(ad) + " isimli çalışanın kota değerini giriniz(Maaşının 10 katı veya daha büyük)(TL):"))   # Kullanıcıdan alınan kota değeri
    kota = yanlışVeriKontorlü(KOTAKONTROL, kota)   # Kota girdisinin kontrolünü yapan fonksiyon
    while başka_emlağı_var_mı == 'e':   # İkinci döngü
        emlak_tipi = input("Emlak tipini giriniz(Konut = k/K, İş Yeri = İ/i, Arsa = A/a):")     # Emlak tipi alınan girdi
        while emlak_tipi not in ['K', 'k', 'A', 'a', 'İ', 'i']:     # Yanlış girdi kontorlü (Hatalıysa tekrar istenir)
            emlak_tipi = input("Hatalı veri girdiniz.Tekrar deneyin (Konut = k/K, İş Yeri = İ/i, Arsa = A/a):")
        işlem_türü = input("Emlak tipine uyguladığınız işlem türünü giriniz(Satış = S/s, Kiralama = K/k):")     # İşlem türü alınan girdi
        while işlem_türü not in ['S', 's', 'K', 'k']:   # Yanlış girdi kontorlü (Hatalıysa tekrar istenir)
            işlem_türü = input("Hatalı veri girdiniz.Tekrar deneyin (Satış = S/s, Kiralama = K/k):")
        if işlem_türü == 'S' or işlem_türü == 's':
            bireysel_satılan_sayısı += 1    # Danışmana özel danışmanın sattığı toplam emlak sayacı
            satış_bedeli = int(input("Emlağın satış bedelini giriniz(TL):"))    # Satış bedeli alınan girdi
            satış_bedeli = yanlışVeriKontorlü(TABAN_BEDEL, satış_bedeli)   # Satış bedeli için yanlış veri kontorlü
            bireysel_satış_toplam += satış_bedeli   # Danışmana özel danışmanın sattığı toplam emlak bedeli hesaplaması
            if emlak_tipi in ['k', 'K']:
                emlak_tipi = "Konut"
                genel_konut_satılma_bedeli += satış_bedeli  # Genel satılan toplam konut bedeli sayacı
                genel_konut_satılma_sayısı += 1  # Danışmana özel danışmanın sattığı toplam konut sayacı
                bireysel_konut_toplam += satış_bedeli   # Danışmana özel danışmanın sattığı toplam konut bedeli hesaplaması
            elif emlak_tipi in ['İ', 'i']:
                emlak_tipi = "İş yeri"
                genel_işyeri_satılma_bedeli += satış_bedeli  # Genel satılan toplam iş yeri bedeli sayacı
                genel_işyeri_satılma_sayısı += 1    # Danışmana özel danışmanın sattığı toplam iş yeri sayacı
                bireysel_işyeri_toplam += satış_bedeli  # Danışmana özel danışmanın sattığı toplam iş yeri bedeli hesaplaması
            else:
                emlak_tipi = "Arsa"
                genel_arsa_satılma_bedeli += satış_bedeli    # Genel satılan toplam arsa bedeli sayacı
                genel_arsa_satılma_sayısı += 1  # Danışmana özel danışmanın sattığı toplam arsa sayacı
                bireysel_arsa_toplam += satış_bedeli  # Danışmana özel danışmanın sattığı toplam arsa bedeli hesaplaması
            if satış_bedeli > genel_en_yüksek_satış:    # En yüksek bedelli satılan emlağın bulunması
                genel_en_yüksek_satış = satış_bedeli       # En yüksek bedelli satılan emlağın bedeli
                genel_en_yüksek_satılan_emlak = emlak_tipi  # En yüksek bedelli satılan emlağın tipi
                genel_en_yüksek_satışı_yapan = ad   # En yüksek bedelli satılan emlağı satan danışmanın adı
            if bireysel_satılan_sayısı > en_yüksek_toplam_satış_adedi:  # Danışmana özel en fazla sayıda satılan emlakların bulunması
                en_yüksek_toplam_satış_adedi = bireysel_satılan_sayısı  # En fazla sayıda satılan emlakların sayısı
                en_yüksek_toplam_satış_adedi_danışman = ad  # En fazla sayıda satılan emlakları satan danışmanın adı
                en_yüksek_toplam_satış_adedi_bedeli = bireysel_satış_toplam  # En fazla sayıda satılan emlakların bedeli
            if bireysel_satış_toplam > en_yüksek_toplam_satış_bedeli:   # Danışmana özel en yüksek bedelli satılan emlağın bulunması
                en_yüksek_toplam_satış_bedeli = bireysel_satış_toplam   # Bu danışmanın sattıklarının toplam bedeli
                en_yüksek_toplam_satış_bedeli_adedi = bireysel_satılan_sayısı   # Bu danışmanın sattığı emlak sayısı
                en_yüksek_toplam_satış_bedeli_danışman = ad     # Bu danışmanın adı
        elif işlem_türü == 'K' or işlem_türü == 'k':
            bireysel_kiralanan_sayısı += 1  # Danışmana özel danışmanın kiraladığı toplam emlak sayacı
            kiralama_bedeli = int(input("Emlağın kiralama bedelini giriniz(TL):"))  # Kira bedeli alınan girdi
            kiralama_bedeli = yanlışVeriKontorlü(TABAN_BEDEL, kiralama_bedeli)    # Kira bedeli için yanlış veri kontorlü
            bireysel_kira_toplam += kiralama_bedeli  # Danışmana özel danışmanın kiraladığı toplam emlak bedeli hesaplaması
            if emlak_tipi in ['k', 'K']:
                genel_konut_kiralanma_sayısı += 1   # Genel kiralanan toplam konut adedi sayacı
                bireysel_kira_konut_sayacı += 1  # Danışmana özel danışmanın kiraladığı toplam konut sayacı
                bireysel_kira_konut_toplam += kiralama_bedeli   # Danışmana özel danışmanın kiraladığı toplam konut bedeli hesaplaması
                if kiralama_bedeli > bireysel_en_yüksek_konut_kira:     #  Danışmana özel en yüksek bedelli konutun kira bedelinin bulunması
                    bireysel_en_yüksek_konut_kira = kiralama_bedeli
                if kiralama_bedeli > genel_en_yüksek_konut_kira:    # Genel en yüksek bedelli konutun kira bedelinin bulunması
                    genel_en_yüksek_konut_kira = kiralama_bedeli
                    genel_en_yüksek_konut_kira_yapan = ad       # En yüksek bedelli konutun kiralamasını yapan danışman
                if kiralama_bedeli > ASGARİ_ÜCRET:  # Asgari ücretten fazla bedelli olan konutların sayacı
                    asgariden_yüksek_bedelli_kira_konut_sayısı += 1
            elif emlak_tipi in ['A', 'a']:
                genel_arsa_kiralanma_sayısı += 1    # Genel kiralanan toplam arsa adedi sayacı
            else:
                genel_işyeri_kiralanma_sayısı += 1  # Genel kiralanan toplam iş yeri adedi sayacı
        başka_emlağı_var_mı = input("Bu ay sattığı/kiraladığı başka emlağı var mı?(E/e/H/h):")  # Döngünün devamlılığını belirleyen girdi
        while başka_emlağı_var_mı not in ['E', 'e', 'H', 'h']:  # Girdi hata kontrolü
            başka_emlağı_var_mı = input("Hatalı veri lütfen tekrar giriniz(E/e/H/h): ")
    if bireysel_satılan_sayısı == 0:  # Hiç satış yapamayan danışman sayacı
        hiç_satamayan_danışman += 1
    bireysel_emlak_komisyonu = bireysel_satış_toplam * KOMİSYON_SATIŞ_DEĞERİ / YÜZDE + bireysel_kira_toplam     # Danışmana özel emlak komisyonu hesaplanması
    genel_emlak_komisyonu += bireysel_emlak_komisyonu   # Genel emlak komisyonu hesaplaması
    prim = bireysel_emlak_komisyonu * PRİM_DEĞERİ / YÜZDE   # Danışmana özel prim hesaplaması
    bireysel_konut_kira_ortalama = bireysel_kira_konut_toplam / bireysel_kira_konut_sayacı  # Danışmana özel konut kira bedellerinin ortalaması
    if bireysel_kiralanan_sayısı >= KİRA_ADEDİ_SINIR or bireysel_kira_toplam >= KİRA_BEDELİ_SINIR:  # KİRA_ADEDİ_SINIR veya KİRA_BEDELİ_SINIR sınırlarını geçen danışmanların sayımı
        fazla_kiralayan_danışmanlar += 1
    if bireysel_emlak_komisyonu > kota:  # Kotanın dolup dolmadığını veren hesap
        kota_doldu_mu = 'Doldurdu.'
        kotayı_dolduran_sayacı += 1     # Kotayı dolduran danışman sayacı
    else:    # Kotanın dolup dolmadığını veren hesap
        kota_doldu_mu = 'Dolduramadı.'
    if prim > maaş:     # Primi maaşından fazla olan kullanıcı sayacı
        primi_fazla_olanlar += 1
    print("Çalışanın adı: ", ad)
    print("O ay sattığı emlak adedi: ", bireysel_satılan_sayısı, "sattığı emlak oranı: %", format((ortalamaBulma(bireysel_satılan_sayısı, (bireysel_satılan_sayısı + bireysel_kiralanan_sayısı), YÜZDE)), '.2f'), " kiraladığı emlak adedi:", bireysel_kiralanan_sayısı, "kiraladığı emlak oranı: %", format((ortalamaBulma(bireysel_kiralanan_sayısı, (bireysel_kiralanan_sayısı + bireysel_satılan_sayısı), YÜZDE)), '.2f'))
    print("Çalışanın sattığı konutların toplam bedeli(TL): ", format((bireysel_konut_toplam), ',.2f'), "sattığı arsaların toplam bedeli(TL):", format((bireysel_arsa_toplam), ',.2f'), "sattığı iş yerlerinin toplam bedeli(TL):", format((bireysel_işyeri_toplam), ',.2f'))
    print("Çalışanın o ay kiraladığı konutların ortalama kira bedeli(TL) ", format((bireysel_konut_kira_ortalama), ',.2f'))
    print("O ay en yüksek bedelle kiraladığı konutun kira bedeli(TL): ", format((bireysel_en_yüksek_konut_kira), ',.2f'))
    print("O ayki maaşı(TL): ", format((maaş), ',.2f'))
    print("O ayki primi(TL): ", format((prim), ',.2f'))
    print("O ayki kotası(TL): ", format((kota), ',.2f'))
    print("O ay acenteye kazandırdığı toplam komisyon tutarı(TL): ", format((bireysel_emlak_komisyonu), ',.2f'))
    print("O ay kotasını doldurup doldurmadığı: ", kota_doldu_mu)
    if kota_doldu_mu == 'Doldurdu.':      # Kota doldurulmuşsa toplam ücrete ikramiye ekleyen hesap
        print("O ay kotasını doldurduğu için alacağı ikramiye(TL): ", format((İKRAMİYE), ',.2f'))
        toplam_ücret = maaş + prim + İKRAMİYE
    else:       # Kota doldurulmamışsa ücreti ikramiye eklenmemiş haliyele veren hesap
        print("O ay kotasını dolduramadığı için ikramiye alamayacak..")
        toplam_ücret = maaş + prim
    if prim > en_yüksek_prim:   # En yüksek primi alan kişinin bulunması
        en_yüksek_prim = prim   #En yüksek prim
        en_yüksek_primi_alan_danışman = ad  # En yüksek primi alan danışman
        en_yüksek_primi_alan_danışmanın_maaşı = maaş    # En yüksek primi alan danışmanın maaşı
        en_yüksek_primi_alan_danışmanın_toplam_ücreti = toplam_ücret    # En yüksek primi alan danışmanın toplam ücreti
    if en_düşük_prim == None:   # İlk değer olarak en düşük primi alan kişinin bulunması
        en_düşük_prim = en_yüksek_prim   # En düşük prim
        en_düşük_primi_alan_danışman = ad   # En düşük primi alan danışmanın maaşı
        en_düşük_primi_alan_danışmanın_maaşı = maaş  # En düşük primi alan danışmanın maaşı
        en_düşük_primi_alan_danışmanın_toplam_ücreti = toplam_ücret # En düşük primi alan danışmanın toplam ücreti
    elif prim < en_düşük_prim:  # En düşük primi alan kişinin bulunması
        en_düşük_prim = prim
        en_düşük_primi_alan_danışman = ad
        en_düşük_primi_alan_danışmanın_maaşı = maaş
        en_düşük_primi_alan_danışmanın_toplam_ücreti = toplam_ücret
    acentenin_ödeyeceği_toplam_Ücret += toplam_ücret  # Acentanın ödeyeceği toplam ücretin hesaplanması
    print("O ay toplam ücreti(TL): ", format((toplam_ücret), ',.2f'))
print("O ay satılan toplam konut sayısı: ", genel_konut_satılma_sayısı, ", toplam arsa sayısı:", genel_arsa_satılma_sayısı, ", toplam iş yeri sayısı:", genel_işyeri_satılma_sayısı,)
print("O ay kiralanan toplam konut sayısı: ", genel_konut_kiralanma_sayısı, ", toplam arsa sayısı:", genel_arsa_kiralanma_sayısı, ", toplam iş yeri sayısı:", genel_işyeri_kiralanma_sayısı)
print("Konutların satılma oranı: %", format((ortalamaBulma(genel_konut_satılma_sayısı, (genel_konut_satılma_sayısı + genel_konut_kiralanma_sayısı), YÜZDE)), '.2f'))
print("Arsaların satılma oranı: %", format((ortalamaBulma(genel_arsa_satılma_sayısı, (genel_arsa_satılma_sayısı + genel_arsa_kiralanma_sayısı), YÜZDE)), '.2f'))
print("İş yerlerinin satılma oranı: %", format((ortalamaBulma(genel_işyeri_satılma_sayısı, (genel_işyeri_kiralanma_sayısı + genel_işyeri_satılma_sayısı), YÜZDE)), '.2f'))
print("Satılan bütün konutların bedelleri toplamı(TL):", format((genel_konut_satılma_bedeli), ',.2f'), ", bütün arsaların bedelleri toplamı(TL):", format((genel_arsa_satılma_bedeli), ',.2f'), ", bütün iş yerlerinin bedelleri toplamı(TL):", format((genel_işyeri_satılma_bedeli), ',.2f'))
print("Satılan bütün konutların bedelleri ortalaması: ", format((ortalamaBulma(genel_konut_satılma_bedeli, genel_konut_satılma_sayısı, TABAN_BEDEL)), ',.2f'))
print("Satılan bütün arsaların bedelleri ortalaması: ", format((ortalamaBulma(genel_arsa_satılma_bedeli, genel_arsa_satılma_sayısı, TABAN_BEDEL)), ',.2f'))
print("Satılan bütün iş yerlerinin bedelleri ortalaması: ", format((ortalamaBulma(genel_işyeri_satılma_bedeli, genel_işyeri_satılma_sayısı, TABAN_BEDEL)), ',.2f'))
print("O ay en yüksek bedelle satılan emlağın tipi:", genel_en_yüksek_satılan_emlak, ", satış bedeli(TL):", format((genel_en_yüksek_satış), ',.2f'), ", satışı yapan danışman:", genel_en_yüksek_satışı_yapan)
print("O ay en yüksek bedelle kiralanan konutun kira bedeli(TL):", format((genel_en_yüksek_konut_kira), ',.2f'), ", kiralayan danışmanın adı:", genel_en_yüksek_konut_kira_yapan)
print("O ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı:", asgariden_yüksek_bedelli_kira_konut_sayısı, "\n  Diğer bütün konutlara oranı: %", format((ortalamaBulma(asgariden_yüksek_bedelli_kira_konut_sayısı, genel_konut_kiralanma_sayısı, YÜZDE)), '.2f'))
print("O ay hiç satış yapamayan danışmanların sayısı:", hiç_satamayan_danışman, ", tüm danışmanlar arasındaki oranı: %", format((ortalamaBulma(hiç_satamayan_danışman, danışman_sayacı,YÜZDE)), '.2f'))
print("O ay satış bedeli olarak en fazla bedele sahip danışmanın ismi: ", en_yüksek_toplam_satış_bedeli_danışman, ", sattıkları emlak sayıları: ", en_yüksek_toplam_satış_bedeli_adedi, ", toplam satış bedeli(TL): ", format((en_yüksek_toplam_satış_bedeli), ',.2f'))
print("O ay satış adedi olarak en fazla adede sahip danışmanın ismi: ", en_yüksek_toplam_satış_adedi_danışman, ", sattıkları emlak sayıları: ", en_yüksek_toplam_satış_adedi, ", toplam satış bedeli(TL): ", format((en_yüksek_toplam_satış_adedi_bedeli), ',.2f'))
print("O ay kotasını dolduran danışman sayısı:", kotayı_dolduran_sayacı, ", tüm danışmanlar içindeki oranı: %", format((ortalamaBulma(kotayı_dolduran_sayacı, danışman_sayacı, YÜZDE)), '.2f'))
print("O at primi maaşından yüksek olan danışman sayısı: ", primi_fazla_olanlar, ", tüm danışmanlar içindeki oranı: %", format((ortalamaBulma(primi_fazla_olanlar, danışman_sayacı, YÜZDE)), '.2f'))
print("O ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışman sayısı:", fazla_kiralayan_danışmanlar)
print("O ay en yüksek primi alan danışman: ", en_yüksek_primi_alan_danışman, ", maaşı(TL): ", format((en_yüksek_primi_alan_danışmanın_maaşı), ',.2f'), ", primi(TL): ", format((en_yüksek_prim), ',.2f'), " ve aylık toplam ücreti(TL): ", format((en_yüksek_primi_alan_danışmanın_toplam_ücreti), ',.2f'))
print("O ay en düşük primi alan danışman: ", en_düşük_primi_alan_danışman, ", maaşı(TL): ", format((en_düşük_primi_alan_danışmanın_maaşı), ',.2f'), ", primi(TL): ", format((en_düşük_prim), ',.2f'), " ve aylık toplam ücreti(TL): ", format((en_düşük_primi_alan_danışmanın_toplam_ücreti), ',.2f'))
print("O ay tüm emlak danışmanlarına ödenecek toplam ücretlerin toplamı(TL): ", format((acentenin_ödeyeceği_toplam_Ücret), ',.2f') , " ve kişi başına düşen ortalama(TL): ", format((ortalamaBulma(acentenin_ödeyeceği_toplam_Ücret, danışman_sayacı, TABAN_BEDEL)), ',.2f'))
print("O ay acentenin kazandığı toplam komisyon(TL): ", format((genel_emlak_komisyonu), ',.2f'))
