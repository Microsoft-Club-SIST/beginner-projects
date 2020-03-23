#Genin_Projects
#Body_Mass_Index Calculator

print("""The  BMI or Body Mass Index Calculator is a general purpose application used to determine whether a person is overweight, underweight or \n 
perfectly normally weighted according to the MATH that dicatated it""")
def bmicalculator(name, weight_kg, height_m):
    bmi= round(weight_kg/(height_m**2),1)
    while True:
        if bmi<18.5:
            return f"The BMI of {name} is {bmi} which means you need to eat more. The math dictates it ddon't blame me." 
            break
        elif bmi>18.5 and bmi<25:
            return f"{name}, your BMI is {bmi} which is so perfectly normal. The math dictates it."
            break
        elif bmi>25 and bmi<30:
            return f"{name}, your BMI is {bmi} which is well, over the threshold of what the MATH dictates which is probably absolute? So slim down a bit. For the ladies atleast :3"
            break
        elif bmi>30:
            return f"{name}, you're probably a gamer. Your BMI is {bmi} and i understand. I've been there. Whether you believe in the empirical power of math or not, you NEED to slim down."
            break
        else:
            return "Your input is invalid which either means you're not of this world or you did not read the instructions"

name = str(input("The person feeling insecure about his/her weight : "))
weight_kg = float(input("Enter the present weight of that person in kgs: "))
height_m = float(input("Enter the present height of that person in metres: "))
print(bmicalculator(name, weight_kg, height_m))
print("""Some of you may disregard the bmi calculator. Saying they don't care about the parameters \n
determined by the empirical order of mathematics and what they define to be normal and that's ok. Keep your opinion to yourself or just blurt them out as much as you want.""")
