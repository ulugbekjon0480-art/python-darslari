# # # pyhton_lugat = {"algoritm":"muammoni yechish uchun ketma-ket bajariladigan amallar",
# # #                 "boolean":"true yoki false qiymatni qabul qiluvchi ma'lumot turi",
# # #                 "for":"takrorlanuvchi amallarni bajarish uchun sikl",
# # #                 "if":"shartni tekshirish operatori",
# # #                 "list":"bir nechta elementlarni saqlovchi ma'lumot turi",
# # # #                 "lugat":"kalit va qiymatdan tashkil topgan ma'lumot turi",
# # # #                 "print":"ma'lumotlarni konsolga chiqarish funksiyasi",
# # # #                 "string":"matnli ma'lumot turi",
# # # #                 "tuple":"o'zgarmas ruyxat turi",
# # # #                 "while":"shart bajarilguncha ishlaydigan sikl"}
# # # # for kalit in sorted(pyhton_lugat):
# # # #     print(f"{kalit.title()}-{pyhton_lugat[kalit]}")
# # # davlatlar={"O'zbekiston": "Toshkent",
# # #            "Qozog'iston": "Astana",
# # #            "Qirg'izston": "Bishkek",
# # #            "Tojikiston":  "Dushanbe",
# # #            "Turkmaniston": "Ashxobod",
# # #            "Rossiya": "Moskva",
# # #            "Xitoy": "Pekin",
# # #            "AQSH": "Washington",
# # #            "Fransiya": "Parij",
# # #            "Germaniya": "Berlin"}
# # # alifbo="abcdefghijklmnopqrstuvwxyzo'qrg' stxyz"
# # # print("davlat (alifbo buyicha):")
# # # for harf in alifbo:
# # #     for davlat in davlatlar:
# # #         if davlat.upper().startswith(harf):
# # #             print(davlat)
# # #             print("\npoytaxtlar(alifbo buyicha):")
# # #             for harf in alifbo:
# # #                 for poytaxt in davlatlar.values():
# # #                     if poytaxt.upper().startswith(harf):
# # #                         print(poytaxt)  
                       
# # # davlatlar={"O'zbekiston": "Toshkent",
# #         #    "Qozog'iston": "Astana",
# #         #    "Qirg'izston": "Bishkek",
# #         #    "Tojikiston":  "Dushanbe",
# #         #    "Turkmaniston": "Ashxobod",
# #         #    "Rossiya": "Moskva",
# #         #    "Xitoy": "Pekin",
# # #            "AQSH": "Washington",
# # #            "Fransiya": "Parij",
# # #            "Germaniya": "Berlin"}
# # # davlat=input("davlat nomi kirit:").lower()
# # # if davlat in davlatlar:
# # #     print(f"{davlat.title()} poytaxti -{davlatlar[davlat]}")
# # # else:
# # # #     print("bizda bunday ma'lumot yuq")
# # # menu={
# # #     "osh": 30000,
# #     # "shashlik": 50000,
# #     # "somsa": 7000,
# #     # "mant":40000,
# #     # "norin": 60000,
# #     # "mastava": 25000,
# # #     "ayron":10000}
# # # for i in range(3):
# # #     ovqat=input("buyurtma qilmoqchi bulgan taomni kiriting:").lower()
# # #     if ovqat in menu:
# #     #     print(f"{ovqat}narxi: {menu[ovqat]} so'm")
# #     # else:
# #     #     print("bizda bunday taom yuq")i"
# #     # "shurva": 35000,
# #     # "jizz":180000,
# #     # "lagmon":60000,

#   116 amaliyot
#   shaxslar=[{"ism":"Alisher Navoiy",
#               "tugilgan_yili":1441,
#               "mashhur": "Xamsa"},
#               {"ism":"Albert Einstein",
#                "soha":"Ilm-fan",
#                "tugilgan_yili":1879,
#   "mashhur":"Nisbiylik nazariyasi"},
#  {"ism":"Leonardo da vinci",
#  "soha":"San'at",
#   "tugilgan_yili":1452,
#  "mashhur":"Mona liza"},
#  {"ism":"Mark Zuckenberg",
#  "soha":"Internet",
#   "tugilgan_yili":1984,
#   "mashhur":"Facebook"}]
#  for i in range(4):
#      print("ismi:", shaxslar[i]["ism"])
#      print("soha:", shaxslar[i]["soha"])
#       print("tugilgan_yili:", shaxslar[i]["tugilgan_yili"])
#       print("mashhur:", shaxslar[i]["mashhur"])
#     print("_"*25)

# # # shaxslar=[
# #     # {"ism":"Alisher Navoiy",
# #         #   "soha":"Adabiyot",
# #         #   "asarlar":["xamsa","mahbub ul-qulub"]},
# # # {"ism": "Isak nyuton",
# # #  "soha":"ilm-fan",
# # #  "asarlar":["Principia","Opticks"]},
# # # {"ism": "Leonardo da vinci",
# # #  "soha":"san'at",
# # #  "asarlar":["mona liza"]},
# # # {"ism": "mark zuckenberg",
# # #  "soha": "internet",
# # #  "asarlar":["facebook"]}
# # # for shaxs in shaxslar:
# #     # print("muallif:", shaxs["ism"])
# #     # print("mashhur asarlari:")
# #     # for asar in shaxs["asarlar"]:
# #         # print("-", asar)
# #     # print("----------------")

# # # sevimli_kinolar={}
# # # for i in range(3):
# #     # ism=input(f"{i+1}-dustingiz(yoki oila azoingiz)ismini kiriting:")
# #     # kinolar=[]
# #     # for i in range(3):
# #         # kino=input(f"{ism}ning{i+1}-sevimli kino/serialini kiriting:")
# #         # kinolar.append(kino)
# #         # sevimli_kinolar[ism]=kinolar
# #         # print("\nnatija:")
# #         # for ism in sevimli_kinolar:
# #         #     print(f"\n{ism}ning sevimli kinolari:")
# #         #     for kino in sevimli_kinolar[ism]:
# #         #         print(f"-{kino}")

# # davlatlar = {
# #     "O'zbekiston": {
# #         "poytaxt": "Toshkent",
# #         "aholi": "36 mln",
# #         "til": "O'zbek tili"
# #     },
# #     "AQSh": {
# #         "poytaxt": "Vashington",
# #         "aholi": "335 mln",
# #         "til": "Ingliz tili"
# #     },
# #     "Yaponiya": {
# #         "poytaxt": "Tokio",
# #         "aholi": "125 mln",
# #         "til": "Yapon tili"
# #     }
# # }

# # # davlat_nomi = ["O'zbekiston", "AQSh", "Yaponiya"]

# # # for i in range(3):
# #     # nom = davlat_nomi[i]
# #     # print("\nDavlat:", nom)

# #     # kalitlar = ["poytaxt", "aholi", "til"]
# #     # for j in range(3):
# #     #     kalit = kalitlar[j]
# #     #     print(kalit, ":", davlatlar[nom][kalit])


# davlatlar = {
#     "O'zbekiston": {
#         "poytaxt": "Toshkent",
#         "aholi": "36 mln",
#         "til": "O'zbek tili"
#     },
#     "AQSh": {
#         "poytaxt": "Vashington",
#         "aholi": "335 mln",
#         "til": "Ingliz tili"
#     },
#     "Yaponiya": {
#         "poytaxt": "Tokio",
#         "aholi": "125 mln",
#         "til": "Yapon tili"
#     }
# }

# davlat_nomi = ["O'zbekiston", "AQSh", "Yaponiya"]
# kalitlar = ["poytaxt", "aholi", "til"]
# foydalanuvchi_davlat = input("Davlat nomini kiriting: ")

# topildi = False 

# for i in range(3):
#     if davlat_nomi[i] == foydalanuvchi_davlat:
#         topildi = True
#         print("\nDavlat:", davlat_nomi[i])
#         for j in range(3):
#             print(kalitlar[j], ":", davlatlar[davlat_nomi[i]][kalitlar[j]])

# if not topildi:
#     print("Bizda bu davlat haqida malumot yuq")

# 120-bet AMALIYOT
sevimli_kitoblar = []

while True:
    kitob = input("Yaxshi ko‘rgan kitobingizni kiriting (to‘xtatish uchun 'stop' yozing): ")
    
    if kitob.lower() == "stop":
        break
    else:
        sevimli_kitoblar.append(kitob)

print("\nSizning sevimli kitoblaringiz:")
for kitob in sevimli_kitoblar:
    print(f"- {kitob}")

while true:
    age=input("yoshizni k:")
    if age.lower()=="exit" or age.lower()=="quit":