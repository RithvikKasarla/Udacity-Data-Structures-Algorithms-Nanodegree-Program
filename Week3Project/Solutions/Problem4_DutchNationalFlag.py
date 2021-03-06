def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) == 0:
        return []
    zero = 0
    two = len(input_list) -1
    while input_list[zero] == 0 and zero < len(input_list)-1:
        zero += 1
    movingPointer = zero + 1
    while input_list[two] == 2:
        two -= 1
    while movingPointer <= two:
        if input_list[movingPointer] == 0 and zero < len(input_list) :
            input_list[movingPointer], input_list[zero] =  input_list[zero], input_list[movingPointer]
            zero += 1
        elif input_list[movingPointer] == 2 and two > -1:
            input_list[movingPointer], input_list[two] =  input_list[two], input_list[movingPointer]
            two -= 1
        else:
            movingPointer += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
test_function([])