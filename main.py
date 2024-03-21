welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = "2"

print("******************************")
print(f"** {welcome_message} **")
print("******************************")

nama_user = input("masukkan nama anda: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini
|_| |_| |_| |_|
''')

pilihan_user = input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4 /]: ")

print(f"pilihan kamu adalah {pilihan_user}")


if pilihan_user == cuypy_position:
    print("SELAMAT KAMU MENANG!")
else: 
    print("KAMU KALAH! cuypuy bukan berada disitu!")   
