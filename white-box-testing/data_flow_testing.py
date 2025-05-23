def calculate_weighted_grade(assignments, midterm, final, attendance):
    assignment_weight = 0.4
    midterm_weight = 0.2
    final_weight = 0.3
    attendance_weight = 0.1

    weighted_assignments = assignments * assignment_weight
    weighted_midterm = midterm * midterm_weight
    weighted_final = final * final_weight
    weighted_attendance = attendance * attendance_weight

    final_grade = (weighted_assignments + weighted_midterm + 
                   weighted_final + weighted_attendance)

    if final_grade >= 90:
        grade_letter = 'A'
    elif final_grade >= 80:
        grade_letter = 'B'
    elif final_grade >= 70:
        grade_letter = 'C'
    elif final_grade >= 60:
        grade_letter = 'D'
    else:
        grade_letter = 'F'

    is_passing = final_grade >= 60

    return final_grade, grade_letter, is_passing

def test_data_flow():
    print("\nTesting All-defs Coverage:")
    result = calculate_weighted_grade(85, 90, 88, 95)
    assert result[0] == 87.5
    assert result[1] == 'B'
    assert result[2] == True

    print("\nTesting All DU Pairs Coverage:")
    result = calculate_weighted_grade(100, 0, 0, 0)
    assert result[0] == 40.0

    result = calculate_weighted_grade(0, 100, 0, 0)
    assert result[0] == 20.0

    result = calculate_weighted_grade(0, 0, 100, 0)
    assert result[0] == 30.0

    result = calculate_weighted_grade(0, 0, 0, 100)
    assert result[0] == 10.0

    print("\nTesting All DU Paths Coverage:")
    result = calculate_weighted_grade(95, 95, 95, 95)
    assert result[1] == 'A'

    result = calculate_weighted_grade(85, 85, 85, 85)
    assert result[1] == 'B'

    result = calculate_weighted_grade(75, 75, 75, 75)
    assert result[1] == 'C'

    result = calculate_weighted_grade(65, 65, 65, 65)
    assert result[1] == 'D'

    result = calculate_weighted_grade(55, 55, 55, 55)
    assert result[1] == 'F'

def print_data_flow_report():
    print("\nData Flow Testing Report:")
    print("========================")
    print("\n1. Definition Points (d):")
    print("   d1: assignment_weight = 0.4")
    print("   d2: midterm_weight = 0.2")
    print("   d3: final_weight = 0.3")
    print("   d4: attendance_weight = 0.1")
    print("   d5: weighted_assignments = assignments * assignment_weight")
    print("   d6: weighted_midterm = midterm * midterm_weight")
    print("   d7: weighted_final = final * final_weight")
    print("   d8: weighted_attendance = attendance * attendance_weight")
    print("   d9: final_grade = sum of all weighted scores")
    print("   d10: is_passing = final_grade >= 60")
    print("\n2. Computation-use Points (c-use):")
    print("   c-use1: assignments and assignment_weight in weighted_assignments calculation")
    print("   c-use2: midterm and midterm_weight in weighted_midterm calculation")
    print("   c-use3: final and final_weight in weighted_final calculation")
    print("   c-use4: attendance and attendance_weight in weighted_attendance calculation")
    print("   c-use5: all weighted scores in final_grade calculation")
    print("\n3. Predicate-use Points (p-use):")
    print("   p-use1: final_grade >= 90 (A grade)")
    print("   p-use2: final_grade >= 80 (B grade)")
    print("   p-use3: final_grade >= 70 (C grade)")
    print("   p-use4: final_grade >= 60 (D grade)")
    print("   p-use5: final_grade < 60 (F grade)")
    print("   p-use6: final_grade >= 60 (passing condition)")
    print("\n4. DU Pairs Coverage:")
    print("   - All definitions are covered")
    print("   - All computation uses are covered")
    print("   - All predicate uses are covered")
    print("\n5. DU Paths Coverage:")
    print("   - All possible grade paths (A through F) are tested")
    print("   - All weight calculation paths are tested")
    print("   - All passing/failing paths are tested")

if __name__ == "__main__":
    test_data_flow()
    print_data_flow_report()
    print("\nAll test cases passed successfully!") 
