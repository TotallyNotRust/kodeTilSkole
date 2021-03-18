import random, keyboard
from datetime import datetime
from time import sleep

now = datetime.now

timeNow = now()

time = random.randint(1, 11)

print("Get ready...")

failed = False

while (now() - timeNow).seconds < time:
    if keyboard.is_pressed("enter"):
        print("You pressed too early")
        failed = True
        break

p1done, p2done = False, False

if not failed:
    print("0")
    start = now()
    while not p1done and  not p2done:
        if not keyboard.is_pressed("enter"):
            delta = now() - start
            print(f"P1: {round(delta.microseconds/1000)}")
            p1done = True
        if not keyboard.is_pressed("space"):
            delta = now() - start
            print(f"P1: {round(delta.microseconds/1000)}")
            p2done = True
