#!/usr/bin/env python3

import math

print('**********************************')
print('it is my first python code')
Name = input('input your name: ')
print('Helloworld',Name,'!! Welcome to python')
print('Helloworld = %s,%d' % (Name,393939))

print('**********************************')
print('list test')
ListTest = ['jimmyliu','jimmy393939','jimmyliu']
print(ListTest)
print('list len = ',len(ListTest))
ListTest.append('chenshimin')
print(ListTest)
print('list len = ',len(ListTest))
ListTest.insert(3,'chenshimin3')
print(ListTest)
print('list len = ',len(ListTest))
ListTest.pop(4)
print(ListTest)
print('list len = ',len(ListTest))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])


print('**********************************')
print('tuple test')
TupleTest = ('jimmyliu','jimmy393939','jimmyliuhuajie')
print(TupleTest)

print('**********************************')
print('if else test')
Age = input('Input your age:')
if int(Age) < 30:
	print('<30,a young man')
elif int(Age) < 60:
	print('30<60,a adult')
else:
	print('>60,a old man')

print('**********************************')
print('loop test')
L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print(x)

Sum = 0
Number=range(101)
for x in Number:
	Sum = Sum+x
print('Sum = ',Sum)

print('**********************************')
print('dict test')
DictTest = {'jimmy':711,'changing':625}
print(DictTest)

print('**********************************')
print('function test')

def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError('bad operated type')
	if not isinstance(b,(int,float)):
		raise TypeError('bad operated type')
	if not isinstance(c,(int,float)):
		raise TypeError('bad operated type')
	return math.sqrt(a),math.sqrt(b),math.sqrt(c)

print('function return = ',quadratic(1,2,3))