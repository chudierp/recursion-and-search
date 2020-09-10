#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item, index=0)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index == len(array):
        return None
    if array[index] == item:
        return array[index]
    else:
        result = linear_search_recursive(array, item, index+1)
        return result

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle_index = (left + right) // 2
        
        if array[middle_index] == item:
            return middle_index
        elif item < array[middle_index]:
            right = middle_index - 1
        elif item > array[middle_index]:
            left = middle_index + 1

    return None

def binary_search_recursive(array, item, left=None, right=None):
    # checks to set default values
	if left is None and right is None:
		left = 0
		right = len(array) - 1

    # defines our new middle
	middle = (left + right) // 2

    # if we get to the center and can't find our item
	if left == middle and array[middle] is not item:
		return None # not found

	if array[middle] == item:
		return middle # found
    # else if, we recursively call our function changing the left/right pointer
	elif item < array[middle]:
		return binary_search_recursive(array,item,left, middle - 1)
	elif item > array[middle]:
		return binary_search_recursive(array,item,middle + 1, right)