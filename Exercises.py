#Fibonacci series - nth term is the sum of (n-1)th and (n-2)th terms
'''
length = int(input('Enter the length of the list: '))
num1, num2 = 0, 1
count = 0
sequence = []

#validate the entered input
if length < 1:
    print('Please enter a positive number')
#If the length is one, then print the first term
elif length == 1:
    print('Fibonacci sequence of length 1: {}'.format(num1))
#generating the sequence
else:
    print('Fibonacci sequence of length {}: '.format(length))
    while count<length:
        sequence.append(num1)
        sum = num1 + num2
        #update the value of num1 and num2 for the next iteration
        num1 = num2
        num2 = sum
        count+= 1
    print(sequence)
'''

#Testing for Prime number
''' 
flag = False
num = int(input('Enter a number:'))
if num<1:
   print('Invalid input. Use a positive integer')
if num>1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
#based on the flag value
if flag:
    print(f'{num} is not a prime number')
else:
    print(f'{num} is a prime number')
'''