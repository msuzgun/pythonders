import os
rehber = {
    "Murat":"5553332266",
    "Mehmet":"5056663322",
    "Ali":"5352223355",
}

def ekle():  
    ad=input("İsim:")
    tel=input("Telefon:")
    rehber.update({ad:tel})
    print(ad," Eklendi...")
    #print (rehber)
def sil():
    ad=input("İsim:")
    if ad in rehber:
        rehber.pop(ad)
        print(ad," Silindi...")
    else :
        print("Böyle bir kullanıcı yok.")
    #print(rehber)
def ara():
    ad=input("İsim:")
    if ad in rehber:
        print("Telefon Numarası:",rehber.get(ad))
    else :
        print("Böyle bir kullanıcı yok")
def liste():
    print("İsim   |   Telefon")
    for x in rehber:
        print(x,rehber.get(x))
    print(len(rehber),"kişi listelendi...")
    
    
while True:
    os.system('cls')
    print("""
    Telefon Rehberi
    Ekle -1
    Ara  -2
    Sil  -3
    Liste-4
    """)
    sec=input("Seçiminiz:")
    if sec=="1":
        ekle()
    elif sec=="2":
        ara()
    elif sec=="3":
        sil()
    elif sec=="4":
        liste()
    input("Devam etmek için enter...")
