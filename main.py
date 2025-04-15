material = input("What material is it? ")
length = float(input("What is its length in cm? "))

waste_type = "trash"

if material == "plastic":
    waste_type = "recycling"

print("Please deposit your item in the " + waste_type + " bin.")
