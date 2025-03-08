#Exception handling in python: An Event that interrupts the flow of a programm
#There are three types of exceptions in python:
#1. ZeroDivisionError : Occurs when we divide a number by zero
#2. ValueError : Occurs when we pass an invalid value to a function 
#3. Exception : Occurs when we pass an invalid value to a function
#  1.try block: The code that can raise an exception is placed inside the try block
#  2.except block: The code that will handle the exception is placed inside the except block
#  3.finally block: The code that will be executed regardless of the exception is placed inside the finally block

while True:
    try:
        number=int(input("Enter a number:"))
        print(1/number)
    except ZeroDivisionError:
        print("You can't divide by zero IDIOT!")
    except ValueError:
        print("You must enter a number!")
    except Exception:

        print("something went wrong!")
    finally:
        print("This will be clean up")