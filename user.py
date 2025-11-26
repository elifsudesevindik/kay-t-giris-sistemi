class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sifre_degistir(self, yeni_sifre):
        self.password = yeni_sifre

    def kullanici_adi_degistir(self, yeni_username):
        self.username = yeni_username
