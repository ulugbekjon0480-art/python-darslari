# x=1
# yigindi=0
# while x< 6:
    # user_raqam = float(input("raqam k;"))
    # yigindi += user_raqam
    # x += 1
    # print(yigindi)
familya=[]

n=int(input(" nechta familiya kiritmoqchisiz"))
for i in range(n):
    fam=input(f"{i+1}-familiyani kirit:")
    familya.append(fam)

for fam in familya:
    if fam[-1].lower() =="a":
        print(f"{fam}-> qiz bola")
    else:
        print(f"{fam}-> ogil bola")
qizlar=[]
bolalar=[]
x=0
while x < 4:
    x += 1
    familiya =input("familiya k:")
    if familiya[-1].lower()  == "a":
        qizlar.append(familiya)
    elif familiya[-1].lower()=="v":
        bolalar.append(familiya)
        print(f"qizlar: {qizlar}")
        print(f"ogil bolalar {bolalar}")



