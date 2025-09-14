# Assignment-01 tests.
# each test is 2 pts

from main import *

def test_foo():
    assert foo(10) == 55

def test_foo2():
    assert foo(0) == 0
    assert foo(1) == 1

def test_longest_run_none():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 999) == 0

def test_longest_run():
	assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

def test_longest_run2():
	assert longest_run([12,12,12,8,12,12,0,12,1], 12) == 3
	assert longest_run([12,12,12,8,12,12,0,12,12,12,12], 12) == 4

def test_longest_run_hard():
    """
    This is a hard corner case that requires left_size and
    right_size to be calculated correctly when only one half 
    has is_entire_range==True.

    [6 12] [12 12] [12 6] [6 6]
    """
    assert to_value(longest_run([6, 12, 12, 12, 12, 6, 6, 6], 12)) == 4



def test_longest_run_recursive_none():
    assert to_value(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 999)) == 0

def test_longest_run_recursive():
	assert to_value(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12)) == 3

def test_longest_run_recursive2():
	assert to_value(longest_run_recursive([12,12,12,8,12,12,0,12,1], 12)) == 3
	assert to_value(longest_run_recursive([12,12,12,8,12,12,0,12,12,12,12], 12)) == 4

def test_longest_run_recursive_hard():
    """
    This is a hard corner case that requires left_size and
    right_size to be calculated correctly when only one half 
    has is_entire_range==True.

    [6 12] [12 12] [12 6] [6 6]
    """
    assert to_value(longest_run_recursive([6, 12, 12, 12, 12, 6, 6, 6], 12)) == 4
