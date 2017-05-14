## Addition function with lambda and reduce
def add(values):
	return reduce(lambda x,y : x+y , values)
print add([47, 11, 42, 13])

## Subtraction function with lambda and map
def substract(num1, num2):
	return map(lambda x,y :x-y , num1,num2)
print substract([47, 11, 42, 13], [37, 21, 22, 33])

## Multiplication function with lambda and reduce
def multiply(values):
	return reduce(lambda x,y : x * y , values)
print multiply([47, 11, 42, 13])

## Division function with lambda and map
def divide(num1,num2):
	return map(lambda x,y: x/float(y) if y!=0 else 'NaN' ,num1,num2)
print divide([2,4,5],[3,7,0])

## Modulus function with lambda and map
def modulus(num1, num2):
	return map(lambda x,y :x % y , num1,num2)
print modulus([47, 11, 42, 13], [37, 21, 22, 33])

## Exponential function with lambda and map
def exponential(num1, num2):
	return map(lambda x,y :x ** y , num1,num2)
print exponential([3, 2, 0,], [9, 5, 1])

## Minimum function with lambda and reduce
def min(values):
    return reduce(lambda x,y: x if (x<y) else y, values) 
print min([3, 11, 42, 32])

## Maximum function with lambda and reduce
def max(values):
    return reduce(lambda x,y: x if (x>y) else y, values)
print max([3,11,542,32,9]) 

## Factorial function with lambda and reduce
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print factorial(5)

## Even Numbers function with lambda and filter
def is_even(values):
    return filter(lambda x: x%2 == 0, values)
print is_even([50, 10, 17, 33])

## Odd Numbers function with lambda and filter
def is_odd(values):
    return filter(lambda x: x%2 == 1, values)
print is_odd([50, 10, 17, 33])

## Greater than Mean function with lambda and filter
def greater_than_mean(values):
    mean = sum(values)/len(values)
    return filter(lambda x: x>mean, values)
print greater_than_mean([47, 11, 42, 13])

## Square Root function with lambda and map
def square_root(values):
    return map(lambda x: x**(1/2.0) if x > 0 else -(-(-x)**(1/2.0)), values)
print square_root([50, 49, -17])

## Cube Root function with lambda and map
def cube_root(values):
    return map(lambda x: x**(1.0/3.0) if x > 0 else -(-(-x)**(1.0/3.0)) , values)
print cube_root([50, 125, -17])

## list Comprehension :Finding odd numbers and doubled them

numbers = [1, 2, 3, 4, 5]

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
print doubled_odds
## Applying list comprehension
numbers = [1, 2, 3, 4, 5]

doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

print doubled_odds

## Another Example for List Comprehension
squares = []

for x in range(10):
    squares.append(x**2)
print squares
## Applying list comprehension
squares = [x**2 for x in range(10)]
print squares


## Generator Fibonacci with user input

def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter >= n): return
        yield a
        c = a
        a = b
        b = c + b
        counter += 1
f = fibonacci(int(raw_input('Give a Number: ')))
for x in f:
    print x,
print '\n'

## Next() method on Generator
def foo():
	print "begin"
	for i in range(3):
		print "before yield", i
		yield i
		print "after yield", i
	print "end"
f = foo()
f.next()
f.next()
f.next()

