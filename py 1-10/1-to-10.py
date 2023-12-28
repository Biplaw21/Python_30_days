#!/usr/bin/env python
# coding: utf-8

# # day 1-

# In[5]:


print("hello world. hello man")


# In[7]:


print(2+3) 


# # python comments
# 
# 
# 
# 
# 
# 

# In[8]:


#this is comment
print("hello world")


# # multi line comment

# In[9]:


#this is comment 1
#this is comment 2
#this is comment 3
print(2+2)


# # day-2

# In[11]:


x,y,z="ball","apple","masala"
print(x)
print(y)
print(z)


# In[12]:


a=1
print(a)


# In[13]:


b=1
c=2.4
print(b+c)


# In[14]:


x="raman"
print(x)


# In[17]:


student=23
print(student)


# In[18]:


student12=123
print(student12)


# In[19]:


biplaw_tiwari=1211
print(biplaw_tiwari)


# In[20]:


x="python"
y="is"
z="amazing"
print(x,y)
print(z)


# In[25]:


x=123
print(x)
print(type(x))


# In[26]:


z= 2+4j
print(z)
print(type(z))


# In[2]:


a= "i am learning the python class."
print(a)
print(type(a))


# In[3]:


b=[1,2,3,4,5,6,7,8,9,10]
print(b)
print(type(b))


# In[4]:


b=(1,2,3,4,5,6,7,8,9,10)
print(b)
print(type(b))


# In[5]:


get_ipython().run_line_magic('whos', '')


# In[8]:


a= 10.11
b= "ram"
c= 3+5j
d= "i am learning python but"
e=[1,2,3,4,5]
f=(6,7,8,9,10)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# In[7]:


get_ipython().run_line_magic('whos', '')


# In[9]:


get_ipython().run_line_magic('whos', '')


# # operators in python

# In[10]:


a=5
b=6
print(a+b)


# In[11]:


a=5
b=11.1
print(a+b)


# In[12]:


a=2+3j
b=4
print(a+b)


# In[17]:


a= "hello"
b="mommy"
print(a+ " " +b)


# In[18]:


a= 12
b=9
print(a%b)


# In[20]:


a=3
b=2
print(a**b)


# In[21]:


a=((144+111)+(12**11)+(11/3)-(10-1))
print(a)


# In[24]:


a= True
b=False
print(a or b)


# In[23]:


a=True
b=True
print(a and b)


# In[25]:


a= True
print(not a)


# In[1]:


a= True
print(not a)


# In[26]:


a=  int(input("enter a value" ))
b=  int(input("enter next value"))
if a<b: 
    print(a+b)
else: 
    print(a-b)


# In[27]:


a=5
print(a)
print(type(a))


# In[24]:


student= "sanchai hununxa?"
print(student[0])
print(len(student))
print(student.upper())
print(student[0:5])
print(student[7:])
print(student[1:7])
print(student.split())
print(student[-1])


# In[25]:


age=12
txt="my name is biplaw, and  i am {}"
print(txt.format(age))


# In[27]:


a=3
b=4
c="teh value of a is{} and the value of b is {}"
print(c.format(a,b))


# In[34]:


quantity=4
price =1123
days=12
c="i want {} piece of balls at the price of rs {} for {} days"
print(c.format(quantity,price,days))


# In[38]:


name= input("enter your name")
print("your name is"+" " +name)


# In[39]:


name= input("enter your name")
b= "my name is {}"
print(b.format(name))


# In[ ]:


b=  "my name is biplw tiwari"
print(b.count("i"))


# In[ ]:


a= input("enter your name")
b= int(input("enter your class"))
print("name of the student is" + ""+a)
h= "age of the student is{}"
print(h.format(b))


# In[20]:


a= input("enter your name")
b= int(input("enter your age"))
c= "your age is {}"
print("your name is " + a)
print(c.format(b))
marks= (input("enter marks in 5 subjects:"))
d,e,f,g,h= map(int,marks.split())    
print("marks in math",d)
print("marks in gk",e)
print("marks in nepali",f)
print("marks in english",g)
print("marks in social",h)
sum = d+e+f+g+h
print("total marks is:", sum)
percentage= (sum/500)*100
print("the percentage of student is", percentage)
if 80>percentage>= 70:
    print("the result is distinction")
elif 70>percentage>=80:
        print("the result is first divison")
elif 70>percentage>=60:
            print("the result is second divison")
elif 60>percentage>=60:
                print(" the result is thrid divison")
else:
                    print("the student is fail")
        


# In[1]:


a= -5.12
print(abs(a))


# # binary funtion

# In[3]:


x= 1234
print(bin(x))


# # python bytes function

# In[2]:


x= bytes(4)
print(x)


# In[3]:


# char function
x= chr(97)
print(x)


# In[4]:


#complex function
x= complex(3,5)
print(x)


# In[6]:


#float function
x= float(12)
print(x)


# In[7]:


#integer function
x= int(12.1)
print(x)


# In[12]:


#string function
a= str("12")
print(a)
print(type(a))


# # day 4

# In[12]:


a= input("enter your name")
print("your name is:", a)
b= int(input("enter your roll number"))
print("Your roll number is:", b)
c= input("enter marks in 5 subjects sperated by space")
d,e,f,g,h= map(int,c.split())
print("your marks in math is", d)
print("your marks in science", e)
print("your marks in social is", f)
print("your marks in english is", g)
print("your marks in nepali is", h)
percentage= ((d+e+f+g+h)/500)*100
print("your total percentage is:", percentage)
if percentage>=90:
    print("A+")
elif 80<=percentage<90:
        print("A")
elif 70<=percentage<80:
    print("B+")
elif 60<=percentage<70:
    print("B")
elif 60<=percentage<50:
    print("C+")
elif 50<=percentage<40:
    print("C")
else:
        print("fail")



# # day-5 CONCEPT  OF LOOPS

# In[3]:


#while loop program to display numbers from 1 to 5
i=1
n=5
while i<=n:
 print(i)
 i=i+1


# In[ ]:


# enter value from user and make a multiplication table upto 10
a= int(input("enter the number"))
i=1
while i<=10:
    print(a*i)
    i=i+1
    


# In[1]:


a= int(input("enter your age"))
while(a>=18):
    print("you can vote")
else:
        print("you cannot vote")


# In[1]:


#for loop
fruits= ["apple","banana","mango"]
for x in fruits:
    print(x)


# In[2]:


#looping through string
a= "banana"
for x in a:
    print(x)


# In[4]:


for x in range(8):
    print(x)


# 
# # day-6 

# In[4]:


def function():
 a= input("enter your name")
 print("your name is:", a)
 b= int(input("enter your roll number"))
 print("Your roll number is:", b)
 c= input("enter marks in 5 subjects sperated by space")
 d,e,f,g,h= map(int,c.split())
 print("your marks in math is", d)
 print("your marks in science", e)
 print("your marks in social is", f)
 print("your marks in english is", g)
 print("your marks in nepali is", h)
 percentage= ((d+e+f+g+h)/500)*100
 print("your total percentage is:", percentage)
 if percentage>=90:
    print("A+")
 elif 80<=percentage<90:
        print("A")
 elif 70<=percentage<80:
    print("B+")
 elif 60<=percentage<70:
    print("B")
 elif 60<=percentage<50:
    print("C+")
 elif 50<=percentage<40:
    print("C")
 else:
        print("fail")



# In[5]:


function()


# 

# In[7]:


a= True
b= False
print(not a and b)


# In[14]:


a= "10"
b= "30"
print(a+""+b)


# In[ ]:


a= input("enter a word")
x= len(a)
if x%2==0:
    print("even")
else:
    print("odd")
    
        


# In[ ]:


word= input("enter a letter").lower()
if word== "a" or word=="e" or word=="i" or word=="o" or word == "u":

    print("vowel")
else:

    print("consonant")


# In[2]:


# use of list and tuple in python

lake= ["rara","phewa","tilicho","begnas"]
print(lake)
print(type(lake))
print(len(lake))
print(lake[1:])
print(lake[2:])
print(lake[-3:-1])
print(lake[1:2])
lake.append("phuksundo")


# In[7]:


# append: add new elements in last position parmanently
# pop(): delete element from last position parmanently
# sort(): sort the element in ascending or aplhabetical order
# reverse(): use to reverse all the element in the list
lake= ["rara","phewa","tilicho","begnas"]
print(lake)
lake.pop(1)
print(lake)
lake.append("phewa")
print(lake)
lake.sort()
print(lake)
lake.reverse()
print(lake)


# In[9]:


#nested loop
barclona=['kaka','mabappe','beligo']
print(barclona)
psg=['messi', 'nymar','ronaldo']
print(psg)
matrix=[barclona,psg]
print(matrix)
print(matrix[1])
print(matrix[1][2])
print(matrix[0][1])


# In[13]:


city=['ktm','pkr','npj','dhr']
dist=['ktm','kaski','banke','unknown']
test=[city,dist]
print(test[1][3])


# In[16]:


list1= ['one','two','three','four']
print(list1)
print(list1[:-2])
print(list1[-2:])


# In[22]:


a=[1,3,2,7,4]
a.sort()
print(a)
a.reverse()
print(a)
for item in a:
    print(item)


# In[25]:


barcelona=['messi','saurez','mbappe']
print("messi" in barcelona)
print("kaka" in barcelona)
print("saurez" not in barcelona)
print("Messi"in barcelona) # case sensetive so it wil print false


# In[30]:


a= "ram"
b= "hari"
c="sita"
d="gita"
e=["ram","hari",'sita','gita']
check = a in e
print(check)
print(c in e)
print("laxman" in e)


# In[38]:


hi= "ram"
hari= "k xa"
shyam="thekai xa"
check=['ram',hari,shyam]
print(hi in check)
print(hari not in check)
print("thekai xa" in check)


# In[46]:


ram=('ram','hari','shyam')
print(type(ram))
print(ram.index("shyam"))
for x in ram:
    print(x,end=' ')


# In[1]:


#dictionary means mapping i.e it will always come in thr key value pair
player={'first name':'biplaw','last name':'tiwari','age':'35','height':'5.7'}
print(player.keys())#only return the keys form dictionary
print(player['first name'])
print(player['last name'])


# In[6]:


player={'first name':'biplaw','last name':'tiwari','age':'35','height':'5.7','country':['nepal','india','china','usa']}
print(player['country'])
print(player['country'][0])
print(player['country'][1])
print(player['country'][-1])
print(player.keys())
print(player.values())
print(player.items())


# In[4]:


d={}
print(type(d))
d['name']='biswash'
d['age']='25'
print(d)


# In[9]:


test={'key1':{'nestkey':{'subnestkey':'hello'}}}
print(test['key1']['nestkey']['subnestkey'])
print(test['key1']['nestkey'])
print(test['key1'])
print(test.values())


# In[14]:


ram={'hari':'shrestha','jindar':'mahal','sunsan':'akela'}
print(type(ram))
print('hari')
print(ram['hari'])


# In[1]:


#set is defined as the collection of well defined elements
#featres of set 
#unordered
#unchangable
#no duplicates
set1={'hello','k','xa','khabar'}
print(set1)
print(type(set1))


# In[2]:


set2=set(["kathmandu","bsantapur","nepal","bhaktapur"])
print(type(set2))


# In[4]:


set1={"kathmandu","ghumna","majja","auxa"}
print(set1)
set1.add("jhut_bolxas")#adding the elements in set
print(set1)


# In[5]:


set1={"pro",'is','always','pro'}
print(set1)
#set3[1]="sorry man" error as the elements cannot be asigned


# In[6]:


set1={'ram','shyam','hari'}
set2={'sita','geeta','binita'}
set3=set1.union(set2)


# In[13]:


set1={'ram','shyam','hari'}
set2={'sita','geeta','binita','ram'}
set3=set1.difference(set2)
print(set3)


# In[12]:


set1={'ram','shyam','hari'}
set2={'sita','geeta','binita','ram'}
set3=set1.intersection(set2)
print(set3)


# In[11]:


set1={'ram','shyam','hari'}
set2={'sita','geeta','binita','ram'}
set1.intersection_update(set2)
print(set1)


# In[2]:


set1={'ram','shyam','hari'}
set2={'sita','geeta','binita','ram'}
set1.symmetric_difference_update(set2)


# In[7]:


for x in range(2,9,2):#comma 2 in the last is used for making the gap between the printed elements like form 2 t 9 there is gap of 2 while printing the value
    print(x)


# In[8]:


set1={1,2,3,4}
set2={4,5,6,7}
set3= set1&set2
print(set3)


# In[9]:


set1={1,2,3,4}
set2={4,5,6,7}
set3= set1-set2
print(set3)


# In[10]:


set1={1,2,3,4}
set1.clear()
print(set1)


# In[1]:


def contact():
    print("contact details of collage")
    print('prime collage')
    print("sorakhutte, Kathmandu")
    print("977-9815154540")
    print("prime@gmail.com")


# In[2]:


for i in range(4):
    a= input("enter your name")
    b=input("enter marks in math science english and nepali seperated by space")
    c,d,e,f= map(int,b.split())
    print()
    contact()


# In[7]:


#agruments
def my_function(fname,lname):
    print(fname + " " + lname)


# In[9]:


my_function("ram","shrestha")
my_function("hari","ojha")


# In[ ]:


def cal():
    if b <= 500:
        print("Your amount is", b * 5)
    elif 500 < b <= 700:
        print("Your amount is", b * 10)
    elif 700 < b <= 1000:
        print("Your amount is", b * 15)
    elif b > 1000:
        print("Your amount is", b * 20)

def info():
    print("Last date of paying the bill is 20th April.")
    print("After 20th April, you will be fined 1000.")
    print("Electricity office is in Thamel.")

for i in range(3):
    a = input("Enter your name: ")
    b = int(input("Enter the unit of electricity used: "))
    cal()
    info()


# In[ ]:





# In[1]:


def cal(b):
    if b <= 500:
        print("Your amount is", b * 5)
    elif 500 < b <= 700:
        print("Your amount is", b * 10)
    elif 700 < b <= 1000:
        print("Your amount is", b * 15)
    elif b > 1000:
        print("Your amount is", b * 20)
    
        


# # day 7

# In[1]:


#indexing in string
a="hello my friend"
print(a[10])


# In[8]:


#slicing of strings
a="hello students how are you"
print(a[0:15:2])


# In[10]:


a="hello students how are you?" #reverse
print(a[::-1])


# In[11]:


a="hello students how are you?"
print(len(a))


# In[12]:


#replace function
a="hello how are you"
print(a.replace("hello","bye"))


# In[26]:


#find method
a="python is great"
b= a.find("i")
print(b)


# # DAY 8

# In[1]:


mylist=["apple",'banana',"mango"]
print(type(mylist))


# In[4]:


list1=["apple",1,1.5,True]
list2=[1,3,4]
list3=[1.2,3.4,1,8]
list4=[True,False,True]
print(list1)
print(list2)
print(list3)
print(list4)


# In[5]:


thislist=[12,12,17,18,10,36]
print(thislist[4])


# In[12]:


list=[1,2,3,4,5,6,7,8,9,10]
print(list[1:7])


# In[9]:


list=[1,2,3,4,5,6,7,8,9,10]
print(list[::-1])


# In[10]:


#change items
list=['apple','banana','mango']
list[1]="litchi"
print(list)


# In[11]:


#change a range of items value
a=[1,2,3,4,-9,-11]
a[1:3]=["pen",'books','copy']
print(a)


# In[17]:


a=[1,2,3,4]
a.append(9)
print(a)
a.pop(1)
print(a)
a.reverse()
print(a)


# In[26]:


l=[1,4,5,6,11,9]
print(len(l))
a=0
for i in range(6):
    a=a+l[i]
    print(a)


# In[27]:


#multiply all the number of the list
l=[1,2,3,4,5]
print(len(l))
a=1
for i in range(5):
    a=a*l[i]
    
    
print(a)


# In[28]:


l = [1, 2, 3, 4, 5]
print(len(l))

a = 1
for i in range(5):
    a = a * l[i]

# Removed the unnecessary i = i + 1 line

print(a)


# # DAY-9 TUPLES

# In[1]:


A=(1,2,3,4,5)
print(type(A))


# In[3]:


a=()
print(a)
print(type(a))


# In[4]:


#creating the tuple with only one item
a=(14,)
print(a)
print(type(a))


# In[5]:


#tuple constructer
a=tuple(("a","b",'c'))
print(a)
print(type(a))


# In[8]:


a=(12,11,16,19,15)#indexing
print(a[3])
print(a[1:3])


# In[11]:


a=(1,2,3,4,5,6,7,8,9,10)
print(a[::2])
print(a[::-1])
print(a[::])
print(a[3:])
print(a[:4])
print(a[-2:-5])


# In[2]:


a=[10,11,15,17]
b=list(a)
b.append(19)
a=tuple(b)
print(a)


# In[6]:


a=[11,15,18,20,21]
y= list(a)
y.append(50)
b= tuple(y)
print(b)


# In[9]:


a=[11,15,18,20,21]
y= list(a)
y.remove(18)
b= tuple(y)
print(b)


# In[14]:


#loops in tuple
d=("a","b","c")
for i in d:
    print(i)


# In[15]:


#joining the 2 tuple
a=("a",'b','c')
b=(1,2,3)
c= tuple(a)+tuple(b)
print(c)


# 
# i=0
# while i<=5:
#     a=int(input("enter values"))
#     t=t+(a,)
#     i=i+1
#     print(t)

# # day 10 dictionary

# In[10]:


a={
    " id":"123ab",
    "color":"blue",
    "year":1999,
    "year":1213
}


# In[11]:


print(a)
print(type(a))


# In[8]:


print(a["color"])


# In[14]:


a={
    " id":"123ab",
    "color":"blue",
    "year":1999
}


# In[15]:


print(len(a))


# In[18]:


dict={
    " id":"123ab",
    "color":"blue",
    "year":1999,
    'a':[1,2,3,4,5],
    'b':(2.3,2.4,2.3,5.2),
    "c":False
}


# In[19]:


print(dict)


# In[28]:


a={'name':"ram",'age':"24",'place':"nepal"}
print(a["name"])


# In[29]:


a={'name':"ram",'age':"24",'place':"nepal"}


# In[30]:


x=a.keys()


# In[31]:


a


# In[32]:


a={'name':"ram",'age':"24",'place':"nepal"}
b=a.values()
print(b)


# In[42]:


a={'name':"ram",'age':"24",'place':"nepal","gender":"male"}
a['age']=19
a.update({'mail':"tiwaribiplaw@gmail.com"})
a.pop("name")
del a["mail"]

print(a)


# In[43]:


a={'name':"ram",'age':"24",'place':"nepal","gender":"male"}
a['age']=19
a.update({'mail':"tiwaribiplaw@gmail.com"})
a.clear()
print(a)


# In[5]:


a={1:10,2:20}
b={3:30,4:40}
c={5:50,6:60}
d={}
for i in(a,b,c):d.update(i)
print(d)


# In[8]:


d=dict()
for x in range(1,6):
    d[x]=x**2
    print(d)


# In[10]:


# check whether a given key alredy exist in a dictionary


# In[10]:


def mul(a,b):
    return(a*b)
result=mul(4,5)
print(result)


# In[15]:


from random import shuffle
mylist=[1,2,3,4,5]
shuffle(myslist)
print(mylist)


# In[19]:


from random import shuffle
def suffle1(a):
    shuffle(a)
    return a
    mylist=['a','p','p','l','e']
    c=shuffle1(mylist)
    print(c)


# In[22]:


transfer=[("raunak",100),("trisha",10000),("biplaw",1000000)]
for player in transfer:
    print(player)
for player,value in transfer:
        print(player)
for player,value in transfer:
            print(value)


# In[27]:


def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
value1=int(input("enter value"))
value2=int(input("enter another value"))
c=add(value1,value2)
d=mul(value1,value2)
e=sub(value1,value2)
f=div(value1,value2)
print(c)
print(d)
print(e)
print(f)


# In[ ]:




