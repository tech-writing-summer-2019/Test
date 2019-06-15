#Calculates the total price of a book order using the number and price of
#books, tax, and  shipping charge

priceOfBook = float(input("Book Price: $")) #User inputs price
numBooks = int(input("Number of Books: ")) #User inputs number
tax = .075 #7.5 percent
ship = 2 #Shipping charge

totBookPrc = priceOfBook*numBooks #Calc total book price
taxChrg = tax*totBookPrc #Calc tax charge
shipChrg = ship*numBooks #Calc shipping charge
price = totBookPrc+taxChrg+shipChrg #Calc total price

print("Order Price: $", round(price, 2), sep = "") #Print total price
