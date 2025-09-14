"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x

    return foo(x - 1) + foo(x - 2)

def longest_run(mylist, key):
    ### TODO
    longest_arr = 0

    cnt = 0
    for i in range(len(mylist)):
        if mylist[i] != key:
            longest_arr = max(longest_arr, cnt)
            cnt = 0
        else:
            cnt += 1

    longest_arr = max(longest_arr, cnt)
    return longest_arr


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    # Base case: empty list
    if len(mylist) == 0:
        return Result(0, 0, 0, False)
    # Base case: single element
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    # Recursive case: split list in half
    mid = len(mylist) // 2
    left = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)

    # Combine results
    # If left's right end and right's left end are both runs of key, they may connect
    left_size = left.left_size
    if left.is_entire_range:
        left_size = left.left_size + right.left_size if right.left_size > 0 else left.left_size

    right_size = right.right_size
    if right.is_entire_range:
        right_size = right.right_size + left.right_size if left.right_size > 0 else right.right_size

    # If left's right end and right's left end are both runs of key, combine them
    cross = 0
    if left.right_size > 0 and right.left_size > 0:
        cross = left.right_size + right.left_size

    longest_size = max(left.longest_size, right.longest_size, cross)
    is_entire_range = left.is_entire_range and right.is_entire_range

    # If the whole range is key, update left_size and right_size
    if is_entire_range:
        left_size = right_size = len(mylist)

    return Result(left_size, right_size, longest_size, is_entire_range)
