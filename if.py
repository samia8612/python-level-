#output to user
conversion_choice = input("1)lb to kg, 2)kg to lb...")

#if user chooses lb to kg:
if(conversion_choice == "1"):
    pounds= int(input("How many lb do you want to convert?"))
    print("This is ", pounds/2.204, "kg")
else:
    kilos= int(input("How many kg do you want to convert?"))
    print("This is ", kilos*2.204, "lb")
  