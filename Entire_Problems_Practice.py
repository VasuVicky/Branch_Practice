'''
#1. Reverse of the given number without string conversion.
n = int(input('Enter the number : '))
l = len(str(n))
original = n
reverse , rem = 0,0
for i in range(l):
    rem = n%10
    reverse = reverse*10 + rem
    n = n//10

print("Original : ",original,' and reverse number : ',reverse)

#while loop :
n = int(input('Enter the number : '))
l = len(str(n))
original = n
rev =0
while n!=0:
    rem = n%10
    rev = rev*10+rem
    n = n//10
print(rev)

#2. print 1 , 100 , 100 to 1 , 1 - 100 divisible by 7 and 10.
print('\n1 to 100 : \n\n')
for i in range(1,101):
    print(i,end=' ')

print('\n1 to 100 : \n\n')
nm = 101
for i in range(100):
    nm -= 1
    print(nm,end=' ')

print("\n1-100 , divisible by 10 and 7 : \n")
for i in range(1,101):
    if i%10==0:
        print(i,end=' ')
    if i%7 ==0:
        print(i,end=' ')

print('\nSum of number 1-100 : \n')
sm =0
for i in range(1,101):
    sm+=i
print(sm)

#3. palindrome and reverse of the given string :
pal , rem , = 0,0
num = int(input('Enter the number : '))
original = num
while num!=0:
    rem = num%10
    pal = pal * 10 + rem
    num //=10
if original == pal:
    print('Given is the palindrome number.')
else:
    print('Not a palindrome number.')

#reverse of the given string :
s = input('Enter the string : ')
rev = s[::-1]
print(rev)

rev =''
for i in range(1,len(s)+1,-1):
    rev += s[i]
print(rev)

#4. amstrong number. [sum of nth power of every digits equals to itself]
n = int(input('Enter the number : '))
l = len(str(n))
arm , rem = 0,0
for i in range(l):
    rem = n%10
    arm = arm + rem  ** l #or pow(rem,l)
    n = n//10
print(arm)

#5. Mykids : add ? after every character except the last character.
a = 'Mykids'
out =''
for i in range(len(a)):
    out = out + a[i]
    if i == len(a)-1:
        break
    out+="?"
print(out)

#6. largest number in the given list : [3,4,5,6,223,4]
a = [3,4,5,6,223,4]
mx =a[0]
for i in a:
    if i>mx:
        mx = i
print(mx)

#7. get the values in the list whose first and last char are same.
out =[]
data = ['abc','xyz','aba','1221','a']
for i in data:
    if i[0] == i[-1] and len(i)>=2:
        out.append(i)
print(out)

#8. finding the unique values & remove duplicates in the list :
a = [1,2,3,4,5,54,2,2,2,3,5,3,6]
print('Unique : \n')

out = []
for i in a:
    if i not in out:
        out.append(i)
print(out)

print('Removing duplicates : \n')
nond=[]
for i in a:
    if not a.count(i) > 1:
        nond.append(i)
print(nond)

#9. swapping of two number : using 3rd var, without.
a ,b = 10 ,20
#1. 
print('Before swapping : ',a,b)
a,b = b,a
print("After swapping : ",a,b)

#2.
a ,b = 10 ,20
print('Before swapping : ',a,b)
c = a
a = b
b =c
print("After swapping : ",a,b)

#3.
a ,b = 15 ,20
print('Before swapping : ',a,b)
a = a+b
b = a-b
a= a-b
print("After swapping : ",a,b)

#10. ['a','b','c','d'] find +ve index and negative index in forward and backword.
a = ['a','b','c','d']
l = len(a)
for i in range(len(a)):
    print(f"Char : {a[i]} and forward +ve index  : {i} and +ve index : {i-l}")

#11. Create a dict from two dict : whose keys are same in both , make value of first dict as key and val in d2 as value.
#output : {2:15,5:8,9:10}
d1 = {1:2,4:5,3:9}
d2 = {4:8,3:10,1:15}
d3={}
if len(d1) == len(d2):
    for k,v in d1.items():
        if k in d2:
            d3[d1[k]] = d2[k]
        else:
            print('key in d1 must exist in d2')
else:
    print('diff lengths not supported')

#find a dict key as values values as keys.
a = {2:15,5:8,9:10}
out ={}
for k,v in a.items():
    out[v] = k
print(out)

#12. a = {2:15,5:8,9:10} largest value in the given dictionary.
a = {2:15,5:8,9:10}
mx =0
for k,v in a.items():
    if v>mx:
        mx = v
print('Largest value is : ',mx)
print(max(a.values()))

#Convert : {'p2':10,'p4':50,'p1':80} into : "p2=10?p4=50?p1=80?"
a = {'p2':10,'p4':50,'p1':80}
out = ""
for k,v in a.items():
    out+=str(k)+"="+str(v)+"?"
print(out)

#back to the original from the output :{'p2':10,'p4':50,'p1':80}
b = "p2=10?p4=50?p1=80?".split('=')
d = {}
c = []
for i in b:
    if '?' in i:
        c.append(i.split('?'))
    else:
        c.append(i)

e = []
for i in c:
    if type(i) ==str:
        e.append(i)
    else:
        e.extend(i)

for i in range(0,len(e)-1,2):
    d[e[i]] = e[i+1]

#13. Find the given value is key in the dictionary or not.
d = {15: 2, 8: 5, 10: 9}
val = int(input("Enter the number : "))
if val in d:
    print(f'{val} is the key in dict and it\'s value is : {d[val]}')

#convert abcdef to aBcDeF.
s = 'abcdef'
out = ''.join([s[i] if i%2==0  else s[i].upper() for i in range(len(s))])

#14. d = [{'VI':S001},{'V':S002},{'VI':S001},{'VI':S005},{'VII':S005},{'V':S009},{'VII':S007}]
#find the unique keys in the given list .
d = [{'VI':'S001'},{'V':'S002'},{'VI':'S001'},{'VI':'S005'},{'VII':'S005'},{'V':'S009'},{'VII':'S007'}]
out =[]
for i in d:
    for k,v in i.items():
        if v not in out:
            out.append(v)
print(out)

#15. Remove space in the dict keys.
a = {'key1      ':1,'key2    ':2,'key3    ':3}
d = {k.strip():v for k,v in a.items()}
print(d)

#daabbccda : dabcda
s = 'daabbccda '
out =''
for i in range(len(s)):
    if i ==0 or s[i] !=s[i-1]:
        out += s[i]

print(out)

#16. Factorial of the given number : using exceptions.
fact =1
num = int(input('Enter the number : '))
for i in range(1,num+1):
    fact *=i
print("using loop : ",fact)

import math
try:
    n = int(input('Enter number : '))
    fact = math.factorial(n)
    print(fact)
except:
    print('Factorial not worked with -ve numbers.')

#17. "this is python" : "python is this"
a = "this is python"
b = ' '.join(a.split()[::-1])
print(b)

# [['ramesh',30],['suresh',45],['mahesh',35]] : if any marks less than 35 say fail else pass along with name.
s = [['ramesh',30],['suresh',45],['mahesh',35]]
for i in s:
    name,marks = i
    if marks <35:
        print(name,' : Fail')
    else:
        print(name,' : Pass')
**** : 
#1. Flattened list :  Recursion : 
a = [1,2,[3,4,5],[6,7,8],[9,10,[11,12]]]
out =[]
def Flattened(sublist):
    for val in sublist:
        if isinstance(val,list):
            Flattened(val)
        else:
            out.append(val)

Flattened(a)
print(out)

#using while loop from pro :
#==============================
[[1, 2, [3, 4, 5], [6, 7, 8], [9, 10, [11, 12]]]] : after adding to the stack.
[1, 2, [3, 4, 5], [6, 7, 8], [9, 10, [11, 12]]] : popinig the element from stack.
[[9, 10, [11, 12]], [6, 7, 8], [3, 4, 5], 2, 1] : reversin the item after pop.
then extracting from it , stack follows lifo , here 1 , 2, if it list then reverse and add to the stack
for accessing element by the next iteration.
for the first iteration it extract entire list and then reverse and again add to the stack.
2nd get 1 add to out , 3rd get 2 add to out , 3rd get [3,4,5] and reverse and add to the stack becomes 5,4,3
4th get 3 and add to out , 5th get 4 add to out , 6th get 5 add to out ,7th get [6,7,8] and then reverse and extend to stack again
then becomes 8,7,6 then 8th get 6 add to out , 7 , 8 ...like that....

it adds to out only when it is an integer.
#==============================

#2. Better approach than the recursion : 
a= [1,2,[3,4,5],[6,7,8],[9,10,[11,12]]]
out = []
stack = [a]
while stack:
    #iterating until stak is empty.
    item = stack.pop()
    #poping the last element
    if isinstance(item,list):
        #if it is list then reversed and extend to the empty stack 
        stack.extend(reversed(item))
    else:
        #if it is not a list then added to the out.
        out.append(item)

print("Flattened List : ",out)

#18. find the output of the given code :
class A:
    def calc(self):
        pass

class B(A):
    def __init__(self):
        self.value = 42
    def calc(self):
        print(self.value)

class C(B):
    def __init__(self):
        self.value=48

class D(A): #error because there no value in A class.
    def calc(self):
        print(self.value)

class E(C):
    def __init__(self):
        pass

a = A() #empty
b = B()
c = C()
d = D()
e=E()
a.calc()
b.calc() #42
c.calc() #48
d.calc()#error
e.calc()

#19. 11,12,2024 => 11/12/2024.
s = "11,12,2024"

out = s.replace(",","/")
print(out)

#or
out = ''
for i in s:
    if i==',':
        out+='/'
    else:
        out+=i
print(out)

#20. Decorator :
def decor(funname):
    def wrapper(name):
        if name == 'vasu':
            print('Converted to upper : ',name.upper())
        else:
            return funname(name)
    return wrapper

@decor
def Main(name):
    print('As Lower : ',name)

Main('vasu')

#21 : righ half of the diamon shape.

n1 = int(input('Enter the number of rows : '))
n = int(input('Enter the number of rows : '))
c = int(input('Enter he number of columns : '))
for i in range(n1):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(n):
    for j in range(c):
        print('*',end=' ')
    c=c-1
    print()

# reversed right angled reversed and right angled down.
n1 = int(input('Enter the number of rows : '))
n = int(input('Enter the number of rows : '))
c = int(input('Enter he number of columns : '))
for i in range(n):
    for j in range(c):
        print('*',end=' ')
    c = c-1
    print()

for i in range(n1):
    for j in range(i+1):
        print('*',end=' ')
    print()

#20. Creating a window, with some label.
import tkinter
from tkinter import *
a = tkinter.Tk()
a.geometry('500x500')
a.title('Winteck')
label = tkinter.Label(a,text="winteck",bg='black',fg='red',font=("calibri",35,'bold')).place(x=60,y=30)
a.configure(bg='limegreen')
a.mainloop()

#21.
num = int(input('Enter number of users : '))
sample ={}
l = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10', 'user11', 'user12', 'user13', 'user14', 'user15', 'user16', 'user17']
v = ['hello', 'ganga', 'chandu', 'vasu', 'vicky', 'gnanu', 'raju', 'mahesh', 'rama', 'krishna', 'winteck', 'learning', 'class', 'satya', 'priya', 'geetha', 'shankar']
for i in range(num):
    sample[l[i]] = v[i]

print(sample)
#based on the get method we can get place instead of the removed user.

#22 : find the factorial of the given number without using inbuilt function :
#by looP;
fact = 1
n = int(input('Enter number to find factorial : '))
for i in range(1,n+1):
    fact*=i
print('factorial : ',fact)

def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))

#program without using break statement :
a=[]
while not len(a)==5:
    n = input('Enter the number : ')
    a.append(n)
print(a)

#23 *** : Reverse only alpha not numbers :#o/p : h1g2iba3

first get the alphas and reverse it , loop over the original list it it alpha then get the char of the reversed one
if not then add the digitt to the out. take a separate pointer variable for increment the alpha sequence.

a = 'a1b2igh3' 
alpha = [ch for ch in a if ch.isalpha()]
alpha.reverse()
out = ''
j =0
for i in a:
    if i.isalpha():
        out+=alpha[j]
        j+=1
    else:
        out+=i

#24 :missing objects b/w a given sequence :
#get the min and max value then get the missing number.
a = [1,3,4,2,4,6,7,10]
missing = []
for i in range(min(a),max(a)):
    if i not in a:
        missing.append(i)
print('Missing numbers are : ',missing)
'''
#25 : validate the password. [must be 8, atleast one alpha small , cap , digits , @/-/+/./_].
p = input('Enter password to validate : ')
if len(p) ==8 :
    




 

















