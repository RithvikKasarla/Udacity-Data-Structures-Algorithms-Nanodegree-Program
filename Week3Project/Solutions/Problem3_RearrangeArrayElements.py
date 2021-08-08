def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heapsort(input_list)
    big = [None,None]
    for x in range(len(input_list)-1,-1,-1):
        if x%2 == 0:
            if big[0] == None:
                big[0] = input_list[x]
            else:
                big[0] = big[0] * 10 + input_list[x]
        elif x %2 == 1:
            if big[1] == None:
                big[1] = input_list[x]
            else: 
                big[1] = big[1] * 10 + input_list[x]
    #print("beeg", big)
    return big
    
def heapify(arr,array_length,middle_node):
    large = middle_node
    left = 2 * middle_node + 1
    right = 2 * middle_node + 2

    if left < array_length and arr[left] > arr[middle_node]:
        large = left
    
    if right < array_length and arr[right] > arr[middle_node] and arr[right] > arr[left]:
        large = right 
    
    if large != middle_node:
        arr[middle_node], arr[large] = arr[large],arr[middle_node]
        heapify(arr,array_length,large)
    

def heapsort(arr):
    arr_len = len(arr)
    for x in range(arr_len,-1,-1):
        heapify(arr,len(arr),x)
    #print("HEAP: ", arr)

    for x in range(arr_len-1,0,-1):
        arr[x], arr[0] = arr[0], arr[x]
        heapify(arr,x,0)
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[8,6], [8,6]]
test_function(test_case)