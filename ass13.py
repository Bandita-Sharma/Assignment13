#Que1-->Write a python program to print the cube of each value of a list using list comprehension
n=int(input("enter the number of elements you want in list"))
l1=[]
for i in range(n):
    l1.append(int(input(i)))
print(l1)
lst_cub=[i*i*i for i in l1]
print("Liat after cube of each value of list is:",lst_cub)
print()

#Que2-->Write a python program to get all the prime numbers in a specific range using list comprehension
lst_prime=[i for i in range(2,31) if all(i % j != 0 for j in range(2,i))]
print(lst_prime)
print()

#Que3-->Write the main difference between list comprehension and generator expression
The generator yeilds one item at a time and generates item only when in demand.
whereas,in a list comprehension,python reserves memory for the whole list.
Generator expression are faster than list comprehension and
hence time efficient.

#Que4-->Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
celsius = [39.2, 36.5, 37.3, 37.8]
fah=list(map(lambda i: i*1.8+32 , celsius))
print(fah)
print()

#Que5-->Apply an anonymous function to square all the elements of a list using map and lambda.
n=int(input("enter the number of elements you want in list"))
l1=[]
for i in range(n):
    l1.append(int(input(i)))
print(l1)
lst_sqr=list(map(lambda i : i*i , l1))
print(lst_sqr)
print()

#Que6-->Filter out all the primes from a list
def prime (mylist):
        for i in range(2, 8):
            return list(filter(lambda x: x == i or x % i, mylist))
lst=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(prime(lst))
print()

#Que7-->Write a python program to multiply all the elements of a list using reduce.
from functools import *
n=int(input("enter the number of elements you want in list"))
l1=[]
for i in range(n):
    l1.append(int(input(i)))
print(l1)
lst_prod=reduce(lambda a,b:a*b , l1)
print(lst_prod)
