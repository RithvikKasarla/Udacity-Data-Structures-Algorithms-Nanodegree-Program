def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == None or input_list == []:
        return -1
    pivot = len(input_list) // 2
    #print("LIST: ", input_list, " Number: ", number," Pivot: ", pivot)
    if input_list[pivot] == number:
        return pivot
    elif  input_list[pivot] > number:
        if input_list[0] > number:
            return pivot + 1 + rotated_array_search(input_list[pivot+1:],number)
        elif  input_list[0] < number:
            return pivot + 1 + rotated_array_search(input_list[:pivot],number)
        elif input_list[0] == number:
            return 0
    elif input_list[pivot] < number:
        if input_list[len(input_list)-1] < number:
            return rotated_array_search(input_list[:pivot],number)
        elif input_list[len(input_list)-1] > number:
            return rotated_array_search(input_list[pivot+1:],number)
        else:
            return len(input_list)-1



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print("YOUR ANSWER: ", rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[],3])
test_function([[],None])