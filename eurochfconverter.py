# 1 chf = 1.02 euors

chf_input = int(input("Please enter the value of chf to convert in euros: "))

def chf_euros(chf):
    if chf * 1.02 > 100000 :
        print("this is a lot of money!")
    return chf * 1.02

print(str(chf_input) + " CHF is equals to " + str(chf_euros(chf_input)) + " euros.")




