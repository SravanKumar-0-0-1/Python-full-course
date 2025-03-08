#collections: single "variable" used to store multiple values.
#            list [] : ordered and changable,duplicate ok
#            set{}: unordered and immutatble ,but add/remove ok,no duplicates
#            Tuple(): ordered and unchangable.Duplicates ok ,faster

# Shopping-cart program is a simple program based on learning about lists,set,tuples.
#          This is like a menu in cinema /canteen and counting the output as bill.
print("---- MENU ----")
print("Items        prices")
print("1.Pizza      200")
print("2.Burger     100")
print("3.pasta      150")
print("4.hotdog      50")

foods=[]
prices=[]
total=0

while True:
    food=input("enter the item 'q' to quit): " )
    if food.lower()== "q":
        break
    else:     
     price=float(input("Enter the price of the item: "))
     foods.append(food)
     prices.append(price)
     total+=price
print("Items in your cart")
for item in foods:
  print(item,end=" ")
print()
for item in prices:
   print(item,end=" ")
print()
print("total price:",total)
    

