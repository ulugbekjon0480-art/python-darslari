#  137-bet AMALIYOT
#  son = float(input("Juft son kiriting: "))
#  if son % 2 == 0:
#      print("Rahmat! Son juft.")
#  else:
#      print("Bu son juft emas.")

# yosh = int(input("Yoshingiz nechida? "))
# if yosh <= 4 or yosh >= 60:
#     narx = 0
# elif yosh < 18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Chipta {narx} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
    # print(f"{x} = {y}")
# elif x < y:
    # print(f"{x} < {y}")
# else:
    # print(f"{x} > {y}")

# mahsulotlar = [
#     'un', 'yog', 'sovun', 'tuxum', 'piyoz',
#     'kartoshka', 'olma', 'banan', 'uzum', 'qovun'
# ]

# savat = []

# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")

# users = ['alisher1983', 'aziza', 'yasina', 'umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz!") 

# students_ortacha = {}

# students = {
#     'ali': [75, 80, 72, 65],
#     'vali': [98, 88, 90, 97],
#     'oysha': [56, 60, 58, 70]
# }

# for key, value in students.items():
#     jami = 0
#     for b in value:
#         jami += b
#     students_ortacha[key] = jami / len(value)
# print("O'rtacha baholar:", students_ortacha)
# for ism, ortacha in students_ortacha.items():
#     if 56 < ortacha <= 71:
#         baho = 3
#     elif 71 < ortacha <= 86:
#         baho = 4
#     elif 86 < ortacha <= 100:
#         baho = 5
#     else:
#         baho = "Baholanmadi"
# print(f"{ism} ning o'rtacha bahosi {ortacha:.2f} → yakuniy baho: {baho}")
                    #    156-AMALIYOT

# def tugilgan_yilini_hisobla(ism, yosh):
#     joriy_yil = 2026
#     return f"{ism}, siz {joriy_yil - yosh}-yilda tug‘ilgansiz."
# natija = tugilgan_yilini_hisobla("Ulug‘bek", 26)
# print(natija)
# def kvadrat_va_kub():
#     try:
#         son = float(input("Son kiriting: "))
#         print(f"{son} ning kvadrati: {son**2}")
#         print(f"{son} ning kubi: {son**3}")
#     except ValueError:
#         print("son kiriting!")
# kvadrat_va_kub
# def juft_toki_son():
#     try:
#         son = int(input("Son kiriting: "))
#         if son % 2 == 0:
#             print(f"{son} juft son")
#         else:
#             print(f"{son} toq son")
#     except ValueError:
#         print("Iltimos, butun son kiriting!")
# juft_toki_son()
# def daraja_hisobla():
#     try:
#         x = float(input("X sonini kiriting: "))
#         n = int(input("N darajasini kiriting: "))
#         natija = x ** n
#         print(f"{x} ning {n}-darajasi: {natija}")
#     except ValueError:
#         print("sonlarni kiriting!")
# daraja_hisobla()
# def daraja_hisobla(x, n=2):
#     """
#     x sonini n-darajaga ko'taradi.
#     n standart qiymati 2 (kvadrat).
#     """
#     natija = x ** n
#     print(f"{x} ning {n}-darajasi: {natija}")
# daraja_hisobla(5)    
# daraja_hisobla(3, 3) 
# def qoldiqsiz_bolinish():
#     try:
#         son = int(input("Son kiriting: "))
#         for i in range(2, 11): 
#             if son % i == 0:
#                 print(f"{son} {i} ga qoldiqsiz bo'linadi")
#             else:
#                 print(f"{son} {i} ga bo'linmaydi")
#     except ValueError:
#         print("butun son kiriting!")
# qoldiqsiz_bolinish()