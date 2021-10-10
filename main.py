import sqlite3
import time


while True:
    # Parolayla güvenlik denetlemesi
    print("************ coded by YAVUZ YARKIN OKULAR  *************\n")

    # Veritabanı bağlantıları
    con = sqlite3.connect("main.db")
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sifre(social_media TEXT, kullanici_adi TEXT,sifre TEXT)"
    )

    # Verilerin Database e kaydedilmesi
    def veri_yaz(hesap, kullaniciAdi, sifre):
        cursor.execute("INSERT INTO sifre VALUES(?,?,?)", (hesap, kullaniciAdi, sifre))
        con.commit()

    # Verilerin database den çekilmesi
    def veri_al():
        cursor.execute("SELECT * FROM sifre")
        data = cursor.fetchall()
        for i in data:
            print(i)

    # Arayüz ve Kullanıcıdan giriş alma
    print("************  UYGULAMAMA HOŞGELDİNİZ  **************")
    islem_secim = input(
        "Yeni şifre eklemek için 1 'i \n Şifreleri görmek için 2 'i tuşlayınız:"
    )
    if islem_secim == "1":
        hesap_ad = input("Hesabın:")
        kullanici_Ad = input("Kullanıcı adını :")
        sifre = input("Sifrenizi :")
        veri_yaz(hesap_ad, kullanici_Ad, sifre)
        print("\n")
        con.close()
    elif islem_secim == "2":
        print("-------  Kayıtlı Sifreleriniz  -------")
        print(
            "*Hesap ",
            "*Kullanıcı Adı",
            "*Sifre",
        )
        veri_al()
        print("\n")
        con.close()
        time.sleep(1)
        print("************  İYİ GÜNLER DİLERİM *************")
        print("\n")
