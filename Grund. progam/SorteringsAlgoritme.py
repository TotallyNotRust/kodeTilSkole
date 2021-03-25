
try:
    get_ipython().run_line_magic('pylab', 'inline')
    from numba import jit # pip install numba
    """
    Numba compiler python metoder til maskin kode. 
    Det tillader at python kode kan køres ca. lige så hurtigt som C eller FORTAN kode.
    Dog tager det en del længere tid at køre metoden første gang.
    Mere info på https://numba.pydata.org/
    """
    from numba.typed import List
    import random
except NameError:
    print("Please run this command")
    print("python -m pip install -r requirements.txt")
    input()
    exit()

@jit(nopython=True) 
def partition(array, start=0, end=-1):
    pivot = array[s]
    low = start + 1
    high = end
    # print(f"{pivot} : {high}")
    while True:
        """
        While loop bruges til at sørge for at pivot ender op det rigtige sted.
        F.eks. hvis du har en liste [3,2,1] vil den ændre 3 og 1 istedet for 3 og 2.
        """
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]

    return high
@jit(nopython=True)
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

"""
Looper gennem en list der består af 0-999.999 og printer tiden
"""
arg = (list(range(1_000_000)))
random.shuffle(arg)
ARG = List()
[ARG.append(i) for i in arg]
print(get_ipython().run_line_magic('time', 'quick_sort(ARG, 0, len(ARG)-1)'))
print(ARG)

