# kom_num=random.randint(1, 10)
# print(kom_num)
# n = 1
# while n < 6:
#     user_guess = int(input(f"{n}- taxmin raqamni kiriting:"))
#     if user_guess == kom_num:
    #     print(f"{n}-urinishda topdingiz va {(6-n)*10}ball oldiz!")
    #     print("siz yuttiz!!!")
    #     break
    # n+=1
# son=int(input("juft son kiriting:"))
# if son % 2 == 0:
#     print("rahmat!")
# else:
#     print("bu juft son emas")
# yosh=int(input("yoshingizni kiriting:"))
# if yosh < 4 or yosh > 60:
#     print("kirish bepul")
# elif yosh < 18:
#     print("chipta narxi: 10000 so'm")
# else:
#     print("chipta narxi: 20000 so'm")
# son1 = int(input("birinchi sonni kiriting:"))
# son2 = int(input("ikkinchi sonni kiriting:"))
# if son1 == son2:
#     print("sonlar teng")
# elif son1 > son2:
#    print("birinchi son ikkinchi sondan katta")
# else:
#     print("birinchi son ikkinchi sondan kichik")
# mahsulotlar = ["non","yog","tuxum","kalbasa","tvorog",
#                "pishloq","sut","bulochka","murabbo","shakar"]
# savat = []
# print("savatga 5ta mahsulot kirit:")
# for i in range(5):
#     mahsulot = input(f"{i+1}-mahsulot kirit:").lower()
#     savat.append(mahsulot)
    # for mahsulot in savat:
        # if mahsulot in mahsulotlar:
        #     print(mahsulot, "-mahsulot dukonimizda bor")
        # else:
        #     print(mahsulot, "-mahsulot dukonimizda yuq")
# mahsulotlar =["olma","banan","ananas","apelsin","anor",
            #   "shaftoli","avakado","nok","orik","gurdoli"]
# suralgan_mahsulotlar =[]
# print("5ta mahsulot kiriting:")
# for i in ["1","2","3","4","5"]:
#     mahsulot = input(f"{i}-mahsulot:").lower()
#     suralgan_mahsulotlar.append(mahsulot)
#     bor_mahsulotlar=[]
    # mavjud_emas=[]int
    # for mahsulot in suralgan_mahsulotlar:
    #     if mahsulot in mahsulotlar:
    #         bor_mahsulotlar.append(mahsulot)
    #     else:
    #         mavjud_emas.append(mahsulot)
    #         if not mavjud_emas:
    #             print("siz suragan barcha mahsulotlar dukonimizda bor.")
    #         else:
    #             print("quyidagi mahsulotlar dukonimizda yuq:".join(mavjud_emas))
# foydalanuvchilar = ["admin","ali","aziz","temur","olim"]
# yangi_login=input("yangi login tanlang:"
# if yangi_login in foydalanuvchilar:
    # print("login band, yangi login tanlang!")
# else:
    # print("xush kelibsz, {yangi_login}!")
# son=int(input("biror butun son kirit:"))
# for n in range(2,11):
    # if son % n == 0:
        # print(f"{son}soni {n} ga qoldiqsiz bulinadi")
# son1=int(input("birinchi sonni kirit"))
# son2=int(input("ikkinchi sonni kirit"))
# son3=int(input("uchinchi sonni kirit"))
# if son1 == son2 == son3:
    # print("sonlar teng")
# else:
# elif son1 >= son2 and son2 >=son3:

   


# ismlar=["ali","vali","asilbek","anora","asila","olim"]
# for ism in ismlar:
    # if ism[0]== "a":
        # print(ism)
ismlar=["alibek","Ulugbek","anora","vasila","gani"]  
for ism in ismlar:
    if ism[-3:].lower() == "bek":
     print(ism)


