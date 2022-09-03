"""
f_000.py | Claus Pagano | Last update: 2022-8-20

Algorithms and Data Structures practice with Python

"""


# --------------------------------------------------------------------------------------------------
# FUNCTION DECLARATION 
# --------------------------------------------------------------------------------------------------

def function_test(test_config):
    """Description:
            test function, performs the job of testing the functions 
            passed by means of a list of parameters

        Parameters:
            test_config (dict): dictionary with parameters
    """
    tests = []
    
    for test in test_config['tests']:
        output_calculated = test_config['function'](*test['input_values'])
        if test['output_expected'] != int and test['output_expected'] != float: #Preguntar si no es un numero
            test_result = 'Passed' if test['output_expected'] == output_calculated else 'Failed'
        else:
            test_result = 'Passed' if abs(test['output_expected'] - output_calculated) <= test['num_precision'] else 'Failed'
        tests.append(test)
        tests[-1]['output_calculated'] = output_calculated
        tests[-1]['result'] = test_result
        if test_config['print_details']:
            print('\n')
            print(f'{"Test case":<25} {test["id"]:>15}')
            print(f'{"Result":<25} {test["result"]:>15}')
            for i, input_name in enumerate(test_config['input_names']):
                print(f'{"Input - " + input_name:<25} {str(test["input_values"][i]):>15}')       
            print(f'{"Output - Expected":<25} {str(test["output_expected"]):>15}')
            print(f'{"Output - Calculated":<25} {str(output_calculated):>15}')
    
    return tests


   