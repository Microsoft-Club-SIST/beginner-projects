height = float(input("Your height in metres:"))
weight = float(input("Your weight in kilograms:"))
bmi = round(weight/ (height * height), 1)

if bmi <= 18.5:
     print('Your BMI is', bmi, 'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
     print('Your BMI is', bmi, 'which means you are normal.')

elif bmi > 25 and bmi < 30:
     print('Your BMI is', bmi, 'which means you are overweight.')

elif bmi > 30:
     print('Your BMI is', bmi, 'which means you are obese.')

else:
    print('There is an error with your input')
