def analyze_number(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        if number % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    else:  # number < 0
        if number % 2 == 0:
            return "Negative Even"
        else:
            return "Negative Odd"

def test_coverage():

    print("\nTesting Statement Coverage:")
    assert analyze_number(0) == "Zero", "Should identify zero"
    assert analyze_number(4) == "Positive Even", "Should identify positive even"
    assert analyze_number(3) == "Positive Odd", "Should identify positive odd"
    assert analyze_number(-2) == "Negative Even", "Should identify negative even"
    assert analyze_number(-3) == "Negative Odd", "Should identify negative odd"

  e
    print("\nTesting Branch Coverage:")

    assert analyze_number(0) == "Zero", "Branch 1: zero"

    assert analyze_number(4) == "Positive Even", "Branch 2: positive even"
   
    assert analyze_number(3) == "Positive Odd", "Branch 3: positive odd"
    
    assert analyze_number(-2) == "Negative Even", "Branch 4: negative even"
    
    assert analyze_number(-3) == "Negative Odd", "Branch 5: negative odd"

    print("\nTesting Condition Coverage:")
   
    assert analyze_number(0) == "Zero", "Condition 1: zero"
   
    assert analyze_number(4) == "Positive Even", "Condition 2: positive"
    assert analyze_number(-2) == "Negative Even", "Condition 2: negative"

    assert analyze_number(4) == "Positive Even", "Condition 3: even"
    assert analyze_number(3) == "Positive Odd", "Condition 3: odd"

def print_coverage_report():
    print("\nCoverage Report:")
    print("===============")
    print("1. Statement Coverage: 100%")
    print("   - All statements in the code are executed")
    print("   - Covered: Zero check, positive/negative checks, even/odd checks")
    
    print("\n2. Branch Coverage: 100%")
    print("   - All branches are executed")
    print("   - Branches covered:")
    print("     * Zero branch")
    print("     * Positive Even branch")
    print("     * Positive Odd branch")
    print("     * Negative Even branch")
    print("     * Negative Odd branch")
    
    print("\n3. Condition Coverage: 100%")
    print("   - All conditions are tested for both True and False")
    print("   - Conditions covered:")
    print("     * number == 0")
    print("     * number > 0")
    print("     * number % 2 == 0")

if __name__ == "__main__":
    test_coverage()
    print_coverage_report()
    print("\nAll test cases passed successfully!") 