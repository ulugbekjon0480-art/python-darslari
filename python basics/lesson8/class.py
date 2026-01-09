students_ortacha={}  




students={
    "Ulugbek":[55,40,87,33,],
    "Aziz":[98,78,56,34],
    "Begi":[23,11,43,65]}
for key, value in students.items():
    students_ortacha[key]=sum(value)// len(value)
    print(students_ortacha)



