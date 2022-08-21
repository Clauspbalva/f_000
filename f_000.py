def multiply(x, y):
    return x * y

test_config = {
    'function': multiply,
    'input_names': ['x', 'y'],
    'tests': [
        {'id': 1, 'input_values': [1, 2], 'output_expected': 4},
        {'id': 2, 'input_values': [-1, 3], 'output_expected': -3}
    ],
    'print_details': True  
}

def function_test(test_config):
    tests = []
    
    for test in test_config['tests']:
        output_calculated = test_config['function'](*test['input_values'])
        test_result = 'Passed' if output_calculated == test['output_expected'] else 'Failed'
        tests.append(test)
        tests[-1]['output_calculated'] = output_calculated
        tests[-1]['result'] = test_result
        if test_config['print_details']:
            print('\n')
            print(f'{"Test case":<25} {test["id"]:>15}')
            print(f'{"Result":<25} {test["result"]:>15}')
            for i, input_name in enumerate(test_config['input_names']):
                print(f'{"Input - " + input_name:<25} {test["input_values"][i]:>15}')
            print(f'{"Output - Expected":<25} {test["output_expected"]:>15}')
            print(f'{"Output - Calculated":25} {output_calculated:>15}')
    
    return tests

function_test(test_config)