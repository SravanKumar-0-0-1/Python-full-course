#While loop: A while loop execute some code WHILE some condition remains true.

#a simple compound intrest program:
#this program will calculate the simple interest if the principal amount, rate of interest and time in years are given.
#it will also calculate the principal amount, rate of interest and time in years if the simple interest is given.      
p=0
r=0
t=0
SI=0
while True:
    while True:
        SI_input = input("enter the simple interest (leave empty if unknown): ")
        if SI_input == "":
            SI = 0
            break
        else:
            SI = float(SI_input)
        p_input = input("enter the principal amount (leave empty if unknown): ")
        if p_input == "":
            p = 0
            break
        else:
            p = float(p_input)
            if p <= 0:
                print("Enter a value greater than 0:")
            else:
                break
    while True:
        r_input = input("enter the interest rate (leave empty if unknown): ")
        if r_input == "":
            r = 0
            break
        else:
            r = float(r_input)
            if r <= 0:
                print("Enter a value greater than 0:")
            else:
                break
    while True:
        t_input = input("enter the time in years (leave empty if unknown): ")
        if t_input == "":
            t = 0
            break
        else:
            t = int(t_input)
            if t<= 0:
                print("Enter a value greater than 0:")
            else:
             break
    if SI == 0:
        SI = (p * t * r) / 100
        print(f"The simple interest in {t} years is: {SI}")
    else:
        if p == 0:
            p = (SI * 100) / (r * t)
            print(f"The principal amount is: {p}")
        if r == 0:
            r = (SI * 100) / (p * t)
            print(f"The interest rate is: {r}")
        if t == 0:
            t = (SI * 100) / (p * r)
            print(f"The time in years is: {t}")

