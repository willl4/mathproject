"""
function = input('Enter a function: ')
func = function.split('x^')
for temp in func:
    print(temp)
    
"""

































function = int(input('Choose highest power in function: '))
while function > 0:
    coefficient1 = int(input('Enter the coeffecient for the x^'+str(function)+' term: '))
    function = function-1
if function > 0: 
    coefficient1 = int(input('Enter the coeffecient for the x^'+str(function)+' term: '))

if __name__ == '__main__':
    data = {}
    data['coefficient'] = ''

    
