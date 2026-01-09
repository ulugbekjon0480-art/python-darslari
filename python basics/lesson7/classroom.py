 # "ism":"Ali",
    # "yosh":45,
    # "familiya":"valiyev,"}
# from.home import dict_
# print(len(dict_))
# print(dict_["karta raqam"])
# print(dict_.get("ism","karta raqam mavjud emas"))
# dict_["karta raqam"]= "9860......2627"
# print(dict_)
# dict_.update({
    # "username":"ali01",
    # "prof_pic":"https://example.com/user_1"})
# dict_["ism"]="vali"
# print(dict_)

# my_dict={
    # 5:"besh",
    # "ism":"ali",
    # 3.4:"3 butun 4",
    # true:"true",
    # (12,34,"ali"):Tuple,
# {5:"besh","ism":"Ali"}:"assadxs"}





# menyu={
    # "osh":35000,
    # "shashlik":50000,
    # "manti": 6000,
    # "somsa": 7000,
    # "mastava":25000,
    # "norin": 60000}   
# while True:
#  ovqat=input("nima yeysiz:")
# if ovqat_nomi == "stop":
    #  print("osh bulsin!")
# Break
# print(menyu.get(ovqat_nomi,f"bizda{ovqat_nomi} yo'q"))

my_list=["Ali","Vali","Ali","Vali","Vali","Oysha"]
my_dict={}
for ism in my_list:
    my_dict[ism]=my_list.count(ism)
    print(my_dict)
    import time
    start=time.time()
    for ism in my_list:
        if my_dict.get(ism):
            my_dict[ism]+=1
        else:
            my_dict[ism]=1
            print(my_dict)
            end=time.time()
            print(f"mening kodim{end-start}vaqt oldi")
            a={
                "Ali":2,
                "Vali":3,
                "Oysha":1}












   
