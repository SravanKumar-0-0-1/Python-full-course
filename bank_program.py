#Simple Bank Program:
#This program is a simple bank program which performs the following operations:
#1. Show Balance    2. Deposit    3. Withdraw    4. Exit
#The program will keep running until the user chooses to exit.

def showbalance():
    print("------------------------------")
    print(f"Your current balance is :Rs {balance:.2f}/-")
    print("------------------------------")

def deposit():
    print("------------------------------")
    amount=float(input("Enter your amount to deposit: "))
    print("------------------------------")
    if amount<0:
        print("please enter a valid amount")
        return 0
    else:
        return amount

def withdraw():
    print("------------------------------")
    amount=float(input("Enter your amount to withdraw:"))
    print("------------------------------")
    if amount>balance:
        print("Insufficient balance")
        return 0
    elif amount<0:
        print("please enter a valid amount")
        return 0
    else:
        return amount
    
def exit():
    pass
balance=0
while True:
    print("------------------------------")
    print("----Sravan National Bank-----")
    print("------------------------------")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("------------------------------")
    choice=int(input("Enter your choice:"))
    if choice==1:
        showbalance()
    elif choice==2:
        balance+=deposit()
        print("------------------------------")
        print(f"Your current balance is : Rs {balance:.2f}/-")
        print("------------------------------")
    elif choice==3:
       balance-=withdraw()
       print("------------------------------")
       print(f"Your current balance is : Rs {balance:.2f}/-")
       print("------------------------------")
    elif choice==4:
        exit()
        break
    else:
        print("------------------------------")
        print("Invalid choice")
        print("------------------------------")

print("------------------------------")
print("Thank You! Have a nice day!")
print("------------------------------")

