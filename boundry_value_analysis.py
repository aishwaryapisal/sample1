"""
Test case statments -> Generate valid and Invalid values to be tested -> Create a test case with the 
combination of having all the variable to nominal values and 1 variable to all the boundry values generated.
"""
#  FIXME: Correct the Variable names 

import itertools


def boundry_value_analysis(min_value:int, max_value:int)->list: 
    """Boundry Value Analysis is a software testing technique, works
    on the basis of single fault Assumption. Test cases are designed
    based on the boundry values.
    For a variable to be tested, values between the min and max values 
    are the nominal values[Valid Test case] and the values less than and 
    greater than are considered as extreme Values[Invalid Test case]

    Args:
        min_value (int): minimum value of the Variable to be tested
        max_value (int): maximum value of the variable to be tested

    Returns:
        list: test cases
    """
    # TODO: Decide "Separation of Valid and Invaid test cases are required at this level"

    # test_cases = {}
    # test_cases['valid'] = [min_value+1, min_value, max_value, max_value-1]
    # test_cases['invalid'] = [min_value-1, max_value+1]
    
    # TODO: Below line can be optimized,
    test_cases = [min_value+1, min_value, max_value, max_value-1, min_value-1, max_value+1]
    return test_cases

def single_fault_assumption(values_tested:dict)->dict:
    """Get the boundry values for each variable, combine them to create 
    combinations and finally check the boundry value is within the range 
    of particular variable then mark them approp. 

    Args:
        values_tested (dict): varibale names with max and min value

    Returns:
        dict: test cases with expected outcomes
    """
    
    # FIXME: Optimize it, and it is possible :)

    # required_test_case = 4*len(values_tested.keys())+1 # Base formula 
    # no_of_variables = len(values_tested)

    test_cases = {} # {variable: [boundry_values]}
    # Get the boundry values to be tested for each variable
    for variable_name, extremes in values_tested.items(): 
        test_cases[variable_name] = boundry_value_analysis(extremes[0], extremes[1])

    final_test_cases = [] # Combination of three variable boundry values 

    tst_css_values = list(test_cases.values())

    # Create a list for generating combinations
    for i in range(0, len(tst_css_values)):
        list_ = []
        for enum, tst_css_value in enumerate(tst_css_values): 
            if enum == i: 
                list_.append(tst_css_value) # [1, 2, 3]
            else: 
                # (Maximum Extreme + Minimum Extreme)/2 - Median
                list_.append([int((max(tst_css_value)+min(tst_css_value))/2)]) # [2]
        
        # Generate combination
        final_test_cases.extend([p for p in itertools.product(*list_)]) # [(1, 2), (2, 2), (3, 2)]
    
    # For each value in the final_test_case check the value is in the extrems range 
    # Mark it as Expected and Not Expected for outcome
    final_cases = {}
    for each_test_case in final_test_cases:
        for e, (variable_name, values) in enumerate(values_tested.items()):
            if not each_test_case[e] in range(values[0], values[1]+1):
                final_cases[each_test_case] =  "Not Expected"
                break
        if each_test_case not in final_cases.keys():
            final_cases[each_test_case] = 'Expected'
    return final_cases
    
    # from pprint import pprint
    # pprint(final_cases)
    # # print(final_test_cases)


if __name__ == "__main__":
    from pprint import pprint 
    pprint(single_fault_assumption({"variable1":[0, 5], "variable2":[6, 10]}))