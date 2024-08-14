# rent calculater 

rent = int(input("Enter your rent exp :"))
food = int(input("Enter your food exp :"))
electricity = int(input("Enter your elc exp :"))
home_exp = int(input("Enter your home expenses :"))
made_exp = int(input("Enter your made expenses :"))

print()
person = int(input("Enter how many person are there in room/flat :"))

total = (rent + food + electricity + home_exp + made_exp) // person
print()

output = print("YOUR total amt you have to pay for this month is =" , total)