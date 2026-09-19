import random

nama = input("Masukin nama karakter lu: ")
player = {"nama": nama, "hp": 100, "gold": 0} 


while True:
    print(f"Selamat datang {player['nama']} di Dungeon!")
    print(f"HP {player['nama']}: {player['hp']} | Gold {player['nama']}: {player['gold']}")
    print("-----------------------")

    def jalan_1():
        damage = random.randint(7, 20)
        print(f"kena lava! - {damage} HP")
        player["hp"] -= damage
    
    def jalan_2():
        gold = random.randint(10, 30)
        print(f"ini ruang harta + {gold} gold ")
        player["gold"] += gold
    
    def jalan_3():
        damage = random.randint(2, 15)
        print(f"kena paku -{damage}HP")
        player["hp"] -= damage
    
    pilihan = input("pilih mana(1,2,3) : ")

    if pilihan == "1" :
        jalan_1()
        print("yah ketemu monster lava")
    elif pilihan == "2" :
        jalan_2()
        print("mantap dapet harta")
    elif pilihan == "3" :
        jalan_3()
        print("yah kena paku")
    else :
        print("jangan pilih ngasal")
    
    print(f"HP {player['nama']}: {player['hp']} | Gold {player['nama']}: {player['gold']}")
    print("--------------------------------------------")

    def toko_goa_aneh():
        while True:
            print("\n=== TOKO PEDAGANG ANEH ===")
            print(f"Gold kamu: {player['gold']}")
            print("1. Potion +30 HP = 15 Gold")
            print("2. Ramuan +50 HP = 25 Gold") 
            print("3. Keluar toko")
        
            beli = input("Mau beli nomer berapa? ")
        
            if beli == "1":
                harga = 15
                if player["gold"] >= harga:
                    player["gold"] -= harga
                    player["hp"] += 30
                    print("Berhasil! HP +30")
                else:
                    print("Gold kurang bro!")
            elif beli == "2":
                harga = 25
                if player["gold"] >= harga:
                    player["gold"] -= harga
                    player["hp"] += 50
                    print("Berhasil! HP +50")
                else:
                    print("Gold kurang bro!")
            elif beli == "3":
                print("Keluar toko")
                break
            else:
                print("Pilihan gak ada")

    def goa_tambang():
        damage = random.randint(2, 7)
        print(f"kena paku tambang -{damage} HP")
        player["hp"] -= damage
    
    def goa_danau():
        damage = random.randint(3, 10)
        print(f"digigit ikan -{damage} HP")
        player["hp"] -= damage
    
    def goa_aneh():
        gold = random.randint(7, 28)
        print(f"nemu pedagang +{gold} gold")
        player["gold"] += gold
        toko_goa_aneh()

    print("sekarang lu harus pilih jalan lagi")
    pilih = input("pilih goa mana (1 tambang, 2 danau, 3 aneh) : ")

    if pilih == "1" :
        goa_tambang() 
        print("hati hati")
    elif pilih == "2" :
        goa_danau()
        print("banyak hewan aneh")
    elif pilih == "3" :
        goa_aneh()
        print("beli apa tadi??")
    else:
        print("salah input")
    
    if player["gold"] > 200:
        print("selamat anda menang kaya")
        break
 
    elif player["hp"] < 0:
        print("anda kalah darah abis")
        break
            
    print(f"\nSTATUS AKHIR")
    print(f"HP {player['nama']}: {player['hp']} |     Gold {player['nama']}: {player['gold']}")
    print("----------------------------------------------------------")