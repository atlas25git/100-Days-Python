ht = input("Enter your height in m: ")
wt = input("enter your wt in kg: ")

wt=int(wt)
ht=float(ht)

print("BMI: " + str(wt/(ht**2)))