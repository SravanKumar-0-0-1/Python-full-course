#Multithreading: Used to perform multiple tasks simultaneously
#                Good for I/O bound tasks like reading files,downloading files,fetching files from APIS,Internets,etc
#                threading.Thread(target=function_name,args=(arg1,arg2))
import threading
import time

def play(game):
   time.sleep(8)
   print(f"Then I am playing {game}")
def listen():
   time.sleep(6)
   print("I started listening to music")
def Wake_up(mytime):
   time.sleep(2)
   print(f"I wake up at {mytime}")
def eating(food):
   time.sleep(4)
   print(f"i done eating {food}")

task1=threading.Thread(target=play,args=("pubg",))
task1.start()
task2=threading.Thread(target=listen)
task2.start()
task3=threading.Thread(target=Wake_up,args=("6:00am",))
task3.start()
task4=threading.Thread(target=eating,args=("breakfast",))
task4.start()
task1.join()
task2.join()
task3.join()
task4.join()

print("I am a stupid to all this")