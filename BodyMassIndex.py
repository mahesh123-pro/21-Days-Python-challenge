def calculate_bml(weight, height):
    bml=weight=weight/(height**2)
    return bml
def bml_category(bml):
    if bml<18.5:
        return "Underweight"
    elif 18.5<=bml<24.9:
        return "Normal weight"
    elif 25<=bml<29.9:
        return "Overweight"
    else:
        return "Obesity"
def main():
    weight=float(input("Enter your weight in kg: "))
    height=float(input("Enter your height in meters: "))
    bml=calculate_bml(weight, height)
    category=bml_category(bml)
    print(f"Your BML is: {bml:.2f}")
    print(f"You are classified as: {category}")
if __name__=="__main__":
    main()
# The code calculates the Body Mass Index (BMI) based on user input for weight and height.