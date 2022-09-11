
def prueba(output_expected, output_calculated):
    num_precision = 0.5
    test = abs(output_expected - output_calculated)
    if test <= num_precision:
        return print('passed') 
    else:
        return print('failed') 

def digit(a):
    test = a
    if str(test).isdigit() == True:
        print('Es digito')
    else:
        print('No es digito')

def prueba2(output_expected, output_calculated):
    num_precision = 0.5
    if str(output_expected).isdigit() == True:
        output_expected = float(output_expected)
        print('Passed') if abs(output_expected - output_calculated) <= num_precision else print('Failed')
    else:
        print('entro_aqui')
        print(type(output_expected))

print(prueba2(0.15, 0.14999999999997726))
