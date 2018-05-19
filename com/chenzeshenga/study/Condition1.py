height = float(input("height:"))
weight = float(input("weight:"))

print("height --> %.2f ,weight --> %.2f" % (height, weight))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("1")
elif bmi >= 18.5:
    print("2")
