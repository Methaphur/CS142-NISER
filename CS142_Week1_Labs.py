#Factorial function
def factorial(n):
  if n == 1:
    return n
  return n*factorial(n-1)

print(factorial(5))


#nth fibonnaci number

def fibon(n):
  if n < 3: 
    return 1
  return fibon(n-1)+fibon(n-2)

print(fibon(6))


#Testing for 50th fibonnaci number using for loop
fibon = [1,1]
for i in range(2,50):
  fibon.append(fibon[i-1]+fibon[i-2])
print(fibon[-1])


#Finding the 50th fibonnaci number usin recursion but previously calculated values are stored 
# Initialising a list with thousand elements all zeroes 
x = [0]*1000
#Initialising the starting condition with first 2 elements 1 
x[0] = x[1] = 1

def fibon(n):  
  # If the nth element is not zero , it is already calculated and this value is returned
  if x[n-1] !=  0:
    return x[n-1] 
  
  else:
    #if not nth value is calculated using recursion
    a = fibon(n-1)+fibon(n-2)
    #Returning calculated value to the nth element in the list
    x[n-1] = a
    return a

print(fibon(50))
     
#Calculating c^m using logm number of multiplication operations

def expo(m,n):
  if n == 0:
    return 1
  if  n < 0:
    return 1/expo(m,-n)
  if n%2 == 0:
    a = expo(m,n/2)
    return a**2
  else:
    b = expo(m,(n-1)/2)
    return m*(b**2)

print(expo(2,32))
     