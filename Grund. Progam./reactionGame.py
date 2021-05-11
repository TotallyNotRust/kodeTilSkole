try:
    import random, keyboard
    from datetime import datetime
except NameError:
    print("Please run this command")
    print("python -m pip install -r requirements.txt")
    input()
    exit()

timeNow = datetime.now()

time = random.randint(1, 11)

print("Get ready...")

class Player:
    done = False
    def __init__(self, name: str):
        self.name = name
    def calcLen(self, start, end, **kw): 
        """Calculates the amount of time it takes the player to press their button"""
        delta = end - start
        print(f"{self.name}: {round(delta.microseconds/1000)}")
        self.done = True
    

p1, p2 = Player("Player 1"), Player("Player 2")

while (datetime.now() - timeNow).seconds < time:
    if keyboard.is_pressed("enter"):
        print("Player 1 pressed too early")
        p1.done = True
    elif keyboard.is_pressed("space"):
        print("Player 2 pressed too early")
        p2.done = True

print("0")
start = datetime.now()
while not p1.done or not p2.done:
    if keyboard.is_pressed("enter") and not p1.done:
        p1.calcLen(start, datetime.now())
    if keyboard.is_pressed("space") and not p2.done:
        p2.calcLen(start, datetime.now())
        
