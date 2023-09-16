# GON by Octaconta

print()
print("Hello! I am GON. I can give you the name of a polygon according to the greek system of naming them.")
sides = str(int(input("Please enter a number of sides from 21 and onward with a maximum of 9 digits (integer):\n")))

digits = list(sides)

name = [""]

for i in range(len(digits)):
    current_digit_prefix = ""
    
    if digits[i] == "0":
        pass
    elif digits[i] == "1":
        pass
    elif digits[i] == "2":
        current_digit_prefix = "di"
    elif digits[i] == "3":
        current_digit_prefix = "tri"
    elif digits[i] == "4":
        current_digit_prefix = "tetra"
    elif digits[i] == "5":
        current_digit_prefix = "penta"
    elif digits[i] == "6":
        current_digit_prefix = "hexa"
    elif digits[i] == "7":
        current_digit_prefix = "hepta"
    elif digits[i] == "8":
        current_digit_prefix = "octa"
    elif digits[i] == "9":
        current_digit_prefix = "ennea"
    
    current_digit_suffix = ""
    
    if len(digits) - 1 - i == 0:
        pass
    elif len(digits) - 1 - i == 1:
        current_digit_suffix = "deca"
    elif len(digits) - 1 - i == 2:
        current_digit_suffix = "heca"
    elif len(digits) - 1 - i == 3:
        current_digit_suffix = "chilia"
    elif len(digits) - 1 - i == 4:
        current_digit_suffix = "myria"
    elif len(digits) - 1 - i == 5:
        current_digit_suffix = "kismyria"
    elif len(digits) - 1 - i == 6:
        current_digit_suffix = "cosakismyria"
    elif len(digits) - 1 - i == 7:
        current_digit_suffix = "chiliakismyria"
    elif len(digits) - 1 - i == 8:
        current_digit_suffix = "myriakismyria"
        
    name.append(current_digit_prefix + "" + current_digit_suffix)

print()
print("A polygon with " + sides + " sides is called:\n" + "".join(name) + "gon")
print()
print("Now, I am GON.")        