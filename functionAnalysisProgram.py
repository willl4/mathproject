"""
function = input('Enter a function: ')
func = function.split('x^')
for temp in func:
    print(temp)
    
"""
import math

if __name__ == '__main__':
    data = {}
    data['coefficients'] = ''
    data['derivative'] = ''
print('If there is a sinx function input it as sin(x)')
print('If there is a cosx function input it as cos(x)')
print('If there is a tanx function input it as tan(x)')
print('If there is a cotx function input it as cot(x)')
print('If there is a secx function input it as sec(x)')
print('If there is a cscx function input it as csc(x)')
print('If there is a log(x)/log(base) function input it as log(x[,base]')
print('If there is an lnx function input it as log(x)')
print('If there is a e^x function input it as exp(x)')
print('If there is a a^x function input it as pow(a,x)')
print('If there is an inverse sin(x) function input it as asin(x)')
print('If there is an inverse cos(x) function input it as acos(x)')
print('If there is an inverse tan(x) function input it as atan(x)')
print('If there is an inverse cot(x) function input it as acot(x)')
print('If there is an inverse sec(x) function input it as asec(x)')
print('If there is an inverse csc(x) function input it as acsc(x)')
print('Input x^ as x**')
print('Use the * to show multiplication. Ex: 3x^2 is 3*x**2')

function = input('Enter the function: ')
lbound = int(input('Enter left bound: '))
rbound = int(input('Enter right bound: '))

range1 = int((rbound-lbound)/0.001)
x = float(lbound)
fval = []
deltx = 0.001
tot=0
for i in range(0,range1):
    tot=float(eval(function))
    fval.append(tot)
    x+=0.001

onederiv = []
valonederiv = 0.0
for i in range(0,len(fval)-1):
    valonederiv = (fval[i+1]-fval[i])/deltx
    onederiv.append(valonederiv)

twoderiv = []
valtwoderiv = 0.0
for i in range(0,len(onederiv)-1):
    valtwoderiv = (onederiv[i+1]-onederiv[i])/deltx
    twoderiv.append(valtwoderiv)

increase = []
decrease = []
ispos = onederiv[0]>0
rangestart=0
max = []
min = []
if ispos:
    min.append([lbound,fval[0]])
else:
    max.append([lbound,fval[0]])
for i in range(0,len(onederiv)-1):
    if onederiv[i] * onederiv[i+1] < 0:
        if ispos:
            increase.append([(rangestart*deltx)+lbound,(i*deltx)+lbound])
            max.append([(i*deltx)+lbound,fval[i]])
        else:
            decrease.append([(rangestart*deltx)+lbound,(i*deltx)+lbound])
            min.append([(i*deltx)+lbound,fval[i]])
        ispos = not ispos
        rangestart=i+1
if ispos:
    increase.append([(rangestart*deltx)+lbound,rbound])
    max.append([rbound,fval[len(fval)-1]])
else:
    decrease.append([(rangestart*deltx)+lbound,rbound])
    min.append([rbound,fval[len(fval)-1]])
abmax=max[0]
abmin=min[0]
for i in range(1,len(max)):
    if max[i][1] > abmax[1]:
        abmax=max[i]
for i in range(1,len(min)):
    if min[i][1] < abmin[1]:
        abmin=min[i]
        
concaveup = []
concavedown= []
ispos = twoderiv[0]>0
rangestart=0
inflectionpt = []
for i in range(0,len(twoderiv)-1):
    if twoderiv[i] * twoderiv[i+1] < 0:
        if ispos:
            concaveup.append([(rangestart*deltx)+lbound,(i*deltx)+lbound])
            inflectionpt.append([(i*deltx)+lbound,fval[i]])
        else:
            concavedown.append([(rangestart*deltx)+lbound,(i*deltx)+lbound])
            inflectionpt.append([(i*deltx)+lbound,fval[i]])
        ispos = not ispos
        rangestart=i+1
if ispos:
    concaveup.append([(rangestart*deltx)+lbound,rbound])
else:
    concavedown.append([(rangestart*deltx)+lbound,rbound])


print("increase: " + str(increase))
print("decrease: " + str(decrease))
print("local max: " + str(max))
print("local min: " + str(min))
print("absolute max: " + str(abmax))
print("absolute min: " + str(abmin))
print("concave up: " + str(concaveup))
print("concave down: " + str(concavedown))
print("inflection points: " + str(inflectionpt))
