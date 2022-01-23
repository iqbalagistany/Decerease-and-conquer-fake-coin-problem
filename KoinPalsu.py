from random import randrange

#Input dari user untuk jumlah koin yang akan digunakan
while True:
    n_coins = 0
    try:
        n_coins = int(input("Masukkan Jumlah Koin Anda: "))
    except: pass
    if n_coins > 1:
        break
    else:
        print("Masukkan Jumlah koin lebih dari 1")


#Membuat koin yang diinputkan user serta memberi berat pada masing" koin
coins={}
for coin in range (1, n_coins+1):
    coins[coin] = 2

random_coin = randrange(1, n_coins)
coins[random_coin] = 1

print(f"Anda memasukkan {n_coins} Koin. Satu diantaranya palsu dengan berat kurang dari koin asli")


# Membagi koin ke dalam 3 grup/bagian
def group(current_coins):
	group_1, group_2, group_3 = {}, {}, {}
	#kalau jumlah koin != 2
	if len(current_coins) != 2:
		a = len(current_coins) // 3    # 10 // 3 = 3
		b = len(current_coins) // 3		# 10 // 3 = 3
		if len(current_coins) % 3 == 0:		# 10 % 3 != 0
			c = len(current_coins) // 3
		else:								# 10 % 3 = 1
			c = len(current_coins) // 3 + len(current_coins) % 3 		# 10 // 3 + 10 % 3 = 3 + 1 = 4
	# Jumlah koin = 2		
	else:
		a, b, c = 1, 1, 0
		
		# a=3, b=3, c=4
		 
# Misal ada 10 koin
# koin dan berat >> {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2}
	for coin in current_coins:
		if list(current_coins.keys()).index(coin) + 1 <= a:		# a = 3. Yang masuk grup_1 = {1:2, 2:2, 3:2} 
			group_1[coin] = current_coins[coin]
		elif list(current_coins.keys()).index(coin) + 1 <= a+b:	# a+b = 6. Yang masuk grup_2 = {4:2, 5:2, 6:2}
			group_2[coin] = current_coins[coin]
		elif list(current_coins.keys()).index(coin) + 1 <= a+b+c:	#a+b+c = 10. Yang masuk grup_3 = {7:2, 8:1, 9:2, 10:2}
			group_3[coin] = current_coins[coin]
	return group_1, group_2, group_3


# function untuk menimbang berat koin
# Membandingkan grup 1 & 2, grup 3 disimpan dulu.
def weigh(group_1, group_2, group_3):
	weight_1, weight_2 = 0, 0
	
	weight_1 = sum(group_1.values()) #nilai grup_1 = 6
	weight_2 = sum(group_2.values()) #nilai grup_2 = 6

	if len(group_3) == 0:
		#sisa yang belum ditimbang
		sisa = 0
	else:
		#sisa yang belum ditimbang
		sisa = f"{len(group_3)}"	#lenght = 4
	#untuk memberikan spasi di tampilan timbangan sehingga sesuai
	spasi = 15 - len(str(len(group_1))) 

#jika berat grup 1 > grup 2
	if weight_1 > weight_2:
		print(" |---LEBIH BERAT-||-------------|")
		print("/\               ||             /\ ")
		print(str(len(group_1)) + spasi * " " + " " + " " + "||" + spasi * " " + str(len(group_2)))
		print("                 ||               ")
		print("                 ||               ")
		print("               ======        ")
		print("Sisa: ", sisa)
		group_name = "KANAN"
		print(f"Pilih bagian {group_name} untuk langkah selanjutnya.")
		print("\n")
		return "1"
#jika berat grup 1 < grup 2
	elif weight_1 < weight_2:
		print(" |-------------||--LEBIH BERAT-|")
		print("/\             ||              /\ ")
		print(str(len(group_1)) + spasi * " " + "||" + spasi * " " + str(len(group_2)))
		print("               ||               ")
		print("               ||               ")
		print("             ======        ")
		print("Sisa: ", sisa)
		group_name = "KIRI"
		print(f"Pilih bagian {group_name} untuk langkah selanjutnya.")
		print("\n")
		return "2"
#jika berat grup 1 == grup 2
	else:
		print(" |-------------||-------------|")
		print("/\             ||             /\ ")
		print(str(len(group_1)) + spasi * " " + "||" + spasi * " " + str(len(group_2)))
		print("               ||               ")
		print("               ||               ")
		print("           SEIMBANG     ")
		print("Sisa: ", sisa)
		group_name = "TIDAK DITIMBANG"
		print(f"Pilih bagian yang {group_name} untuk langkah selanjutnya.")
		print("\n")
		return "="

#memasukkan koin yang diinpiutkan ke dalam variabel current_coins untuk diproses lebih lanjut
current_coins = coins
#langkah pencarian
steps = 0

print("\n")

# Selama koin palsu belum ditemukan
while len(current_coins) != 1:
	steps += 1
	print(f"STEP: [{steps}]")
	group_1, group_2, group_3 = group(current_coins)
	
	w_result = weigh(group_1, group_2, group_3)
	if w_result == "=":
		current_coins = group_3
	elif w_result == "1":
		current_coins = group_2
	elif w_result == "2":
		current_coins = group_1

# Ketika koin palsu sudah ditemukan
fake = list(current_coins.keys())[0]
print(f"*************************************\n\nKoin palsu ada di koin nomor {fake}.\nButuh {steps} langkah untuk menemukan koin palsu.")