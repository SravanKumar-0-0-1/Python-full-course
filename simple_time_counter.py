#Time counter: This is simple program counting the time based on given input
# this is simple example for using for loop and time module.

import time
my_time=int(input("enter the time u need to count : "))

for x in range(my_time,0,-1):
    seconds= x%60
    minutes=(x//60)%60
    hours=x//3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up buddy!")