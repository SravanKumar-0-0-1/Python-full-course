#FOR loops: Execute a block of code a fixed numberr of times.
#           You can iterate over a range ,string,sequence,etc.

#Nested loop: A loop within another loop(outer,inner)
  #           outer loop
  #           inner loop


#*- pattern in  reverse triangular form
for x in range(5):
    for y in range(5,x,-1):
        print("*", end="")
    print()

#*-pattern for right angulat triangle
for x in range (5):
    for y in range(x+1):
        print("*",end="")
    print()

#Inverted pyramid pattern
for x in range(5):
    for y in range(x+1):
        print(" ", end="")
    for y in range(2*(5-x)-1):
        print("*", end="")
    print()
    
#full pyramid

for x in range(1,6):
    for y in range(5-x):
        print(" ",end="")
    for k in range(1,2*x):
        print("*",end="")
    print()

for x in range(1,6):
    for y in range(5-x):
        print(" ",end="")
    for y in range(x):
        print("*",end="")
    print()