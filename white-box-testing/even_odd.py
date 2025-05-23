def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Test cases
def test_is_even():
    assert is_even(4) == True, "4 should be even"
    
    assert is_even(7) == False, "7 should be odd"
    
    assert is_even(0) == True, "0 should be even"
    
    assert is_even(-2) == True, "-2 should be even"
    
    assert is_even(-3) == False, "-3 should be odd"

if __name__ == "__main__":
    test_is_even()
    print("All test cases passed!") 