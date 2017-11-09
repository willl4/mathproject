"""
function = input('Enter a function: ')
func = function.split('x^')
for temp in func:
    print(temp)
    
"""

if __name__ == '__main__':
    data = {}
    data['coefficients'] = ''
    data['derivative'] = ''


function = int(input('Choose highest power in function: '))
power = function
while function >= 0:
    coefficient = int(input('Enter the coefficient for the x^'+str(function)+' term: '))
    data['coefficients'] = data['coefficients']+str(coefficient)
    function = function-1

list1 = data['coefficients'].split()
for i in range(0,len(data['coefficients'])):
    derivativecoeff = int(data['coefficients'][i])*power
    while power > 1:
        data['derivative'] = data['derivative']+str(derivative)
    if power = 1:
        data['derivative'] = data['derivative'] + 
    
    derivative = str(derivativecoeff)+'x^'+str(power-1)+'+'
    power+=-1
    data['derivative'] = data['derivative']+str(derivative)
    
print(data['derivative'])




























"""
function = int(input('Choose highest power in function: '))
if function == 1:
    coefficient1 = int(input('Enter the coeffecient for the x^1 term: '))
    coefficient = int(input('Enter the constant: '))
elif function == 2:
    coefficient2 = int(input('Enter the coeffecient for the x^2 term: '))
    coefficient1 = int(input('Enter the coeffecient for the x^1 term: '))
    coefficient = int(input('Enter the constant: '))
elif function == 3:
    coefficient3 = int(input('Enter the coeffecient for the x^3 term: '))
    coefficient2 = int(input('Enter the coeffecient for the x^2 term: '))
    coefficient1 = int(input('Enter the coeffecient for the x^1 term: '))
    coefficient = int(input('Enter the constant: '))
elif function == 4:
    coefficient4 = int(input('Enter the coeffecient for the x^4 term: '))
    coefficient3 = int(input('Enter the coeffecient for the x^3 term: '))
    coefficient2 = int(input('Enter the coeffecient for the x^2 term: '))
    coefficient1 = int(input('Enter the coeffecient for the x^1 term: '))
    coefficient = int(input('Enter the constant: '))
elif function == 5:
    coefficient5 = int(input('Enter the coeffecient for the x^5 term: '))
    coefficient4 = int(input('Enter the coeffecient for the x^4 term: '))
    coefficient3 = int(input('Enter the coeffecient for the x^3 term: '))
    coefficient2 = int(input('Enter the coeffecient for the x^2 term: '))
    coefficient1 = int(input('Enter the coeffecient for the x^1 term: '))
    coefficient = int(input('Enter the constant: '))
"""
    
