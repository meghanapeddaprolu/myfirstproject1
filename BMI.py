weight=float(input("enter your weight in kg "))
height=float(input("enter your height in cm "))
meters=height/100
BMI=weight/meters**2
print(BMI)
if BMI<= 18.5:
    print("Underweight")
elif BMI<= 25:
    print("Normal Weight")
elif BMI <=30:
    print("overweight")
else:
    print("Obese")


