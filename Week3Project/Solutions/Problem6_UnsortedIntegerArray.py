def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return (None,None)
    min = ints[0]
    max = ints[0]
    for x in range(1,len(ints)):
        if ints[x] > max:
            max=ints[x]
        elif ints[x] < min:
            min = ints[x]
    return (min,max)



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print ("Pass" if ((-1, 0) == get_min_max([0,0,0,0,0,0,0,0,-1])) else "Fail")

print ("Pass" if ((0, 0) == get_min_max([0,0,0,0,0,0,0,0,0])) else "Fail")
print ("Pass" if ((None,None) == get_min_max([])) else "Fail")