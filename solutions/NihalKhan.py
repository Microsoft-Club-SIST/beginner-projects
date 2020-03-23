import math as m
def bmi(height,weight):
    bmi = weight/(height)**2
    print(m.floor(bmi))
    if bmi <= 18.5:
        print("underweight")
    elif bmi>18.5 and bmi<=24.9:
        print("average")
    elif bmi>24.9  and bmi<= 29.9:
        print("over weight")
    else:
        print("obese")
height = float(input("enter your hright in meters"))
weight = float(input("enter your weight in kgs"))
bmi(height,weight)
