## 1 euro = .98 chf

def euro_to_chf(euro):
    return euro * .98

euro = float(input("Please give your amount (euros): "))

print(str(euro) + " euros in chf is " + str(euro_to_chf(euro)) +".")