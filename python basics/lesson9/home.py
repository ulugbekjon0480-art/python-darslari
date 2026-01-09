# def kopaytma(*sonlar):
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija
# print(kopaytma(2, 3, 4))      
# print(kopaytma(5, 10))       
# print(kopaytma(1, 2, 3, 4)) 
# def talaba_malumot(ism, familiya, **malumotlar):
#     talaba = {
#         "ism": ism,
# #         "familiya": familiya
# #     }
# #     talaba.update(malumotlar)
# #     return talaba
# # print(talaba_malumot(
# #     "Ali",
# #     "Valiyev",
#     yosh=20,
#     kurs=2,
#     fakultet="AT"
# ))
# buyurtmalar = []

# while True:
#     mahsulot = input("Mahsulot nomini kiriting (stop - tugatish): ").lower()
#     if mahsulot == "stop":
#         break
#     buyurtmalar.append(mahsulot)

# print("Buyurtmalar ro‘yxati:", buyurtmalar)
# ebozor = {}

# while True:
#     mahsulot = input("E-bozor mahsulotini kiriting (stop - tugatish): ").lower()
#     if mahsulot == "stop":
#         break

#     narx = int(input(f"{mahsulot} narxini kiriting: "))
#     ebozor[mahsulot] = narx

# print("E-bozor mahsulotlari:", ebozor)
# def birinchi_harf_bosh(matnlar):
#     yangi_royxat = []
#     for matn in matnlar:
#         yangi_royxat.append(matn.capitalize())
#     return yangi_royxat
# royxat = ["salom", "dunyo", "python dasturlash"]
# natija = birinchi_harf_bosh(royxat)
# print(natija)
# def bahola(malumot):
#     ism = malumot[0]          
#     baholar = malumot[1:]    
#     ortacha = sum(baholar) / len(baholar)
#     return {ism: ortacha}
# royxat = ["Ali", 5, 4, 5, 3]
# natija = bahola(royxat)
# print("Asl ro'yxat:", royxat)
# print("Natija:", natija)
        # 180 AMALIYOT
# kupaytir_10 = lambda x: x * 10
# print(kupaytir_10(5))

# yigindi = lambda a, b: a + b
# print(yigindi(3, 5))
# import random
# sonlar = random.sample(range(0, 1000), 10)
# print(sonlar)
