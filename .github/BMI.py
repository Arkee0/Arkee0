name = input("Enter your name: ") 
sex = input("Enter Gender: ")
if sex[0].upper() == "M":
    print(f"Hello Mr. {name}.\nhope you are having a nice day sir.")
if sex[0].upper() == "F":
    print(f"Hello Ms. {name}. \nHope you are having a nice day ma'am.")
weight = input("Please enter your weight:  ")
weight_unit = input("Pounds or Kilogram? ")
height = input("Please enter your height(In meters): ")
if weight_unit[0].upper() == "P":
    con = float(weight) / 2.2
else:
    con = float(weight)
bmi = (con / float(height) ** 2)
print(f"Your Body Mass Index is: {round(bmi, 2)}")
