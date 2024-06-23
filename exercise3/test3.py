import pytest
from exercise3 import custom_sort

@pytest.fixture
def sample_lists():
    return {
        "list1": [4, 1, 3, 2],
        "list2": [5, 8, 6, 7, 3],
        "list3": [1, 2, 3, 4, 5],
        "list4": [],
        "list5": [1, 2, 1, 2],
        "list6": [1, 7, 5, 9, 3],
        "list7": [6, 0, 4, 8, 2]
    }

def test_custom_sort_basic(sample_lists):
    """Tests basic functionality with mixed even and odd numbers."""
    assert custom_sort(sample_lists["list1"]) == [2, 4, 1, 3], "List [4, 1, 3, 2] should be sorted to [2, 4, 1, 3]"
    assert custom_sort(sample_lists["list2"]) == [6, 8, 3, 5, 7], "List [5, 8, 6, 7, 3] should be sorted to [6, 8, 3, 5, 7]"    

def test_custom_sort_consecutive(sample_lists):
    """Tests if a list containing consecutive numbers is sorted correctly."""
    assert custom_sort(sample_lists["list3"]) == [2, 4, 1, 3, 5], "List [1, 2, 3, 4, 5] should be sorted to [2, 4, 1, 3, 5]"

def test_custom_sort_empty_list(sample_lists):
    """Tests if an empty list is handled correctly."""
    assert custom_sort(sample_lists["list4"]) == [], "Empty list should remain empty"

def test_custom_sort_repeated(sample_lists):
    """Tests if a list containing repeated numbers is sorted correctly."""
    assert custom_sort(sample_lists["list5"]) == [2, 2, 1, 1], "List [1, 2, 1, 2] should be sorted to [2, 2, 1, 1]"

def test_custom_sort_all_odd(sample_lists):
    """Tests if a list containing only odd numbers is sorted correctly."""
    assert custom_sort(sample_lists["list6"]) == [1, 3, 5, 7, 9], "List [1, 7, 5, 9, 3] should be sorted to [1, 3, 5, 7, 9]"

def test_custom_sort_all_even(sample_lists):
    """Tests if a list containing only even numbers is sorted correctly."""
    assert custom_sort(sample_lists["list7"]) == [0, 2, 4, 6, 8], "List [6, 0, 4, 8, 2] should be sorted to [0, 2, 4, 6, 8]"

if __name__ == "__main__":
    pytest.main()