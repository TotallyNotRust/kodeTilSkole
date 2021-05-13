from sys import getsizeof, maxsize

class Char:
    """
    Custom Char klasse,
    Tager en string med 1 karakter
    """
    def __init__(self, val: str):
        if len(val) > 1:
            raise SyntaxError("Passed value must be a str with 1 character")
        else:
            self.int = ord(val)
            self.str = val
    def __repr__(self):
        return self.str

def pointerExample(var):
    print(f"Type: {type(var)}")
    print(f"Value: {var}")
    print(f"Binary value: {bin(x := getsizeof(var))}")
    print(f"Size in bytes: {x}")
    print(f"Max size: {maxsize}")
    print(f"Hex location: {hex(id(var))}")
    printByteArray(x)
                   
    
def printByteArray(var, a=4, s=0): # a = amount; amount per line. s = start; hvor array starter
    for i in range(0, round(var/a)*a, a):
        for x in range(a):
            print(f"+---{i+x+s:^4}---+", end="" if not x+1 == a else "\n")
        print(f"|  1 byte  |"*a)
        print(f"+----------+"*a)
    if not var%a == 0:
        printByteArray(var%a, a=var%a, s=var-1)    

if __name__ == "__main__":
    # Input 
    print("Giv mig et variable\nF.eks. 53, '53', [53]")
    pointerExample(eval(input(": ")))
    input()
