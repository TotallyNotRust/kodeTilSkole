from numba import jit, types # pip install numba
 
from numba.typed import List
import random, datetime
 
def partitionJittedMethod(array, start=0, end=-1):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
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
 
def quickSortJittedMethod(array, start, end):
    if start >= end:
        return
 
    p = partitionJitted(array, start, end)
    quickSortJitted(array, start, p-1)
    quickSortJitted(array, p+1, end)
 
partitionJitted = jit(partitionJittedMethod, nopython=True)
quickSortJitted = jit(quickSortJittedMethod, nopython=True)
 
for i in range(1_000):
    arg = list(range(100_000))
    random.shuffle(arg)
    arg = List(arg)
    start = datetime.datetime.now()
    quickSortJitted(arg, 0,  len(arg)-1)
    timeInMs = (datetime.datetime.now() - start).microseconds / 1000
    print(f"{i:< 4}: Passed: {list(arg)==sorted(arg)} | Time in milliseconds: {timeInMs}")
        
