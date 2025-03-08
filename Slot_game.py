# This Python Slot Machine Game is a simple gambling simulation where the player places bets and spins a virtual slot machine with emojis as symbols.
#  The goal is to match three symbols in a row to win a payout.
#How the Game Works:
# Player Deposits Money – The user enters an initial balance.
# Placing Bets – The player enters a bet amount before spinning.
# Spinning the Slot Machine – Three random symbols are generated from a predefined list.
# Winning Conditions – If all three symbols match, the player wins a multiplier payout based on the symbol.
# Balance Update – The balance is adjusted based on the bet and winnings.
# Play Again Option – The player can choose to continue or exit the game.

import random

def spin_row():
  symbols=["😒","❤️","☠️","😎","🤣"]
  return [random.choice(symbols) for _ in range(3)]

def print_row(row):
  print("-------------------------------")
  print(" | ".join(row))
  print("-------------------------------")
  
def get_payment(row,bet):
  if row[0]==row[1]==row[2]:
    if row[0]=="😒":
      return bet*3
    elif row[0]=="❤️":
      return bet*5
    elif row[0]=="☠️":
      return bet*5 
    elif row[0]=="😎":
      return bet*10
    elif row[0]=="🤣":
      return bet*20
  return 0 

balance=int(input("Enter your amount to add to your account:"))
print("------------------------------")
print("----Welcome to Slot Game-----")
print("Symbols:🤣 😎 ☠️ 😒 ❤️")
print("------------------------------")
while True:
  if balance>0:
    print(f"Your current balance is : Rs{balance:.2f}")
    bet=input("Enter Your Bet:")
    if not bet.isdigit():
      print("Enter  a valid amount")
      continue
    bet=int(bet)
    if bet>balance:
      print("Insufficient balance")
      continue
    if bet<=0:
      print("Bet must be greater than 0")
      continue
      
    balance-=bet
    row=spin_row()
    print_row(row)
    payout=get_payment(row,bet)
    if payout>0:
      print(f"Congratulations! You won Rs{payout}")
    
    else:
      print("Better luck next time")
    
    balance+=payout
    if play_again:=input("Do you want to play again? (y/n): ").lower():
      if play_again=="n":
        break
    
  