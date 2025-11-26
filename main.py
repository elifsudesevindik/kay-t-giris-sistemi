from database import Database

db = Database()

while True:
    secenekler = input("1-kayıt\n2-giriş\n3-listeleme\n4-sifre değiştirme\n5-isim değiştirme\n6-kayıt silme\n7-çıkış\nseçiminiz: ")
    if secenekler == "1":
        username = input("Kullanıcı adı ")
        password = input("Şifre: ")
        
        if db.ekleme(username, password):
            print("Kayıt başarılı")
        else:
            print("Kullanıcı adı zaten var")
    
    elif secenekler == "2":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")

        if db.giris(username, password):
            print (f"Hoş geldin {username}!")
        else:
            print("Kullanıcı adı veya şifre yanlış")
    
    elif secenekler == "3":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        if not db.giris(username, password):
            print("Kullanıcı adı veya şifre yanlış")
            continue
        else:
            kullanicilar = db.arama()
            print("\n--- Kayıtlı kullanıcılar---")
            for k in kullanicilar:
                print(f"ID: {k[0]}, Kullanıcı Adı: {k[1]}")

    elif secenekler == "4":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        if db.giris(username, password):
            new_password = input("Yeni şifre: ")
            db.guncelle_sifre(username, new_password)
            print("Şifre başarıyla güncellendi.")
        else:
            print("Kullanıcı adı veya şifre yanlış")

    elif secenekler == "5":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        if db.giris(username, password):
            kullanicilar = db.arama()
            print("\n--- Kayıtlı kullanıcılar---")
            for k in kullanicilar:
                print(f"ID: {k[0]}, Kullanıcı Adı: {k[1]}")
            user_id = int(input("Değiştirmek istediğiniz kullanıcının ID'si: "))
            new_username = input("Yeni kullanıcı adı: ")
            db.guncelle_kullanici_adi(user_id, new_username)
            print("Kullanıcı adı başarıyla güncellendi.")
        else:
            print("Kullanıcı adı veya şifre yanlış")

    elif secenekler == "6":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        if db.giris(username, password):
            db.silme(username, password)
            print("Kullanıcı başarıyla silindi.")
        else:
            print("Kullanıcı adı veya şifre yanlış")

    elif secenekler == "7":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.")