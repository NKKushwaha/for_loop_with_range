# W.A.P.T. Print the sum of first n number
'''
N=int(input('Enter the Numeber:'))
Sum=0
for i in range(1,N+1):
    Sum+=i
print(Sum)
'''
'''
1. Taking number from the user(3)
2. Initilze Sum by assuming Number is not present
Extracting each and every element from range
itration:1:
    i=1
    Now Sum the i value (S=1)
itration:2:
    i=2
    Now Sum the i value (S=3)
itration:3:
    i=3
    Now Sum the i value (S=6)
At last print the Sum Value whic is 6
'''

#W.A.P.T. print the given number
'''
N=int(input('Enter the Numeber:'))
fac=1
for i in range(1,N+1):
        fac*= i
print(fac)
'''
'''
1. Taking number from the user(3)
2. Initilze fac by assuming the Number is 0 so it factorail is 1
Extracting each and every element from range
itration:1:
    i=1
    Now fac is multiply by the i (fac=1)
itration:2:
    i=2
    Now fac is multiply by the i (fac=2)
itration:3:
    i=3
    Now fac is multiply by the i (fac=6)
At last print the fac value which is 6
'''
# W.A.P.T given number is prefect number or not
# Note:- if the given number is equal to sum of the divisers of given number then we call it as perfect number
#(ex: 6 is perfect number because the sum of divisior (1+2+3=6))
'''
N=int(input('Enter the Numeber:'))
S=0
for i in range(1,N//2+1):
    if N%i==0:
        S+=i
if N==S:
    print(f'{N} is perfect number')
else:
    print(f'{N} is not perfect number')
'''

'''
1. Taking number from the user(6)
2. Initilze S by assuming the Number is 0 so it factorail is 1
Extracting each and every element from half of the given number(because after of half of the number is not divisible for that)
itration:1:
    i=1
    Now N is divided by i and check it equal to zero
    it is true then add the i value with S (S=1)
itration:2:
    i=2
    Now N is divided by i and check it equal to zero
    it is true then add the i value with S (S=1+2=3)
itration:3:
    i=3
    Now N is divided by i and check it equal to zero
    it is true then add the i value with S (S=1+2+3=6)
itration:4:
    i=4
    Now N is divided by i and check it equal to zero
    it is not true then don't add the i value with S (S=6)
itration:5:
    i=5
    Now N is divided by i and check it equal to zero
    it is not true then don't add the i value with S (S=6)
After iteration check N is equal to S
It is true
Then print the N value which is perfect number
If it is not true
Then print the N value which is not perfect number
'''

# W.A.P.T. Find number between 100 and 400 (both included) where each digit of a number is even number. The number obtained should be printed n a comma seperated
'''
for i in range (100,401):
    p=str(i)
    if int(p[0])%2==0 and int(p[1])%2==0 and int(p[2])%2==0:
        print(i, end=',')
'''

'''
m=[]
for i in range (100,401):
    l=''
    p=str(i)
    for k in p:
        if int(k)%2==0:
            l+=k
        else:
            l=''
            break
    if l!='':
        p=int(p)
        if p%2==0:
            m.append(p)
print(m)
            
'''


for i in range(0, 401):
    p=str(i)
    C=0
    for k in p:
        if int(k)%2==0:
            C+=1
    if C==len(p):
        print(p,end=',')


#W.A.P.T.Print even number in the given range
# In this method time complexcity is high

'''
S=int(input('Enter the staring Number:'))
n=int(input('Enter the Ending Number:'))
for i in range (S,n+1):
    if i%2==0:
        print(i)
'''

'''
1. Taking staring number from the user (10)
2. Taking Ending number from the user (14)
Extracting each and every element from the range
itration:1:
    i=10
    now check the i is divided by 2
    it is true then print i (10)
itration:2:
    i=11
    now check the i is divided by 2
    it is not true then not print i
itration:3:
    i=12
    now check the i is divided by 2
    it is true then print i (12)
itration:4:
    i=13
    now check the i is divided by 2
    it is not true then not print i
itration:5:
    i=14
    now check the i is divided by 2
    it is true then print i (14)

'''
# In this method time complexcity is less
'''
S=int(input('Enter the staring Number:'))
n=int(input('Enter the Ending Number:'))
if S%2!=0:
    S=S+1
for i in range (S,n+1,2):
    print(i)
'''
'''
1. Taking staring number from the user (11)
2. Taking Ending number from the user (20)
3. Now Checking Starting number is not true
    if it true then add the staring number with i (S=12)
Extracting each and every element from the range
itration:1:
    i=12
    print the i value which is 12
itration:2:
    i=14
    print the i value which is 14
itration:3:
    i=16
    print the i value which is 16
itration:4:
    i=18
    print the i value which is 18
itration:5:
    i=20
    print the i value which is 20
'''
            
