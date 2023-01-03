#Factorial of n 
def factorial(n):
    if n == 1:
        return n
    return n*factorial(n-1)

#Reference 
fibon = [1,1]
for i in range(2,10):
  fibon.append(fibon[i-1]+fibon[i-2])
print(*fibon,sep=",")

# nth fibonacci number
def fibon(n):
  if n < 3: 
    return 1
  return fibon(n-1)+fibon(n-2)

print(fibon(6))


#Save in memory algo Method 1
def fibon(n,x=[1,1]):
  if n <= len(x):
    return x[n-1]
  a = (fibon(n-1)+fibon(n-2))
  x.append(a)
  return a
print(fibon(50))

#Save in memory algo Method 2
x = [0]*1000
x[0] = x[1] = 1
def fibon(n):
  if x[n-1] !=  0:
    return x[n-1] 
  
  else:
    a = fibon(n-1)+fibon(n-2)
    x[n-1] = a
    return a

print(fibon(50))
#Check 
fibon = [1,1]
for i in range(2,50):
  fibon.append(fibon[i-1]+fibon[i-2])
print(fibon[-1])


#calculating C^m using logm number of multiplication operations 
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
