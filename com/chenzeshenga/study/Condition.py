age=int(input("age:"))
sex=input("gender:")

if age>=18 and sex=="Male":
    print("right one")
elif age<17:
    print("wrong")
else:
    pass

#age!=0-->true
#type --> int!=0 -->true
#         string!="" -->true
if age:
    print("age:%s"%age)