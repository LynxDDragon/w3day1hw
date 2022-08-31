#EXERCISE 1

#Filter out all of the empty strings from the list below

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

place =[" ","Argentina", " ", "San Diego",""," "," ","Boston","New York"]

result = list(filter(lambda location: location.strip() != "", place))

print(result)


#EXERCISE 2

#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

def sort_last(author):
    author.sort(key=lambda x: x.split()[-1])

    return author

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]


print(sort_last(author))


#EXERCISE 3

#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

conversion = list(map(lambda f : (f[1] * 1.8 + 32), places))

print (conversion)



#EXERCISE 4

#Write a recursion function to perform the fibonacci sequence up to the number passed in.

#Output for fib(5) => 
#Iteration 0: 1
#Iteration 1: 1
#Iteration 2: 2
#Iteration 3: 3
#Iteration 4: 5
#Iteration 5: 8


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))