#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# # day 11
# 

# In[1]:


a={'ram','hari','sita'}
print(type(a))
print(a)


# In[4]:


#the set()constructor
a=set(("ram",'hari','sita'))
print(type(a))
print(a)


# In[5]:


a=set()
print(a)


# In[6]:


#access items
a= {'a','b','c','d','e'}
for x in a:
    print(x)


# In[7]:


a= {'a','b','c','d','e'}
print("a"in a)


# In[11]:


#add and delete items
a= {'a','b','c','d','e'}
a.add(100)
print(a)
a.remove(100)
print(a)


# In[14]:


#updating one set to another
a={'a','b','c','d'}
b={'e','f','g','h'}
a.update(b)
print(a)
a.pop()
print(a)
a.clear()
print(a)


# In[19]:


#max value and min value
a={1,23,4,33,90,67}
print("the orginal set of element is",a)
print("maximum value in set is",max(a))
print("minimum value of set is ", min (a))


# In[23]:


# return a new set of identical items from two sets
a={'a','b','c','d'}
b={'e','f','g','h'}
c= a.union(b)
d= a.intersection(b)
print(c)
print(d)


# In[62]:


colors = ["red", "black", "blue"]
for index, color in enumerate(colors):
    print("Index: {}, Color: {}".format(index,color))


# In[64]:


word="prime IT collage"
for index, char in enumerate(word):
    print(f"index:{index},character:{char}")


# In[7]:


y=0
while y<10:
    print(y,"is less than 10 so, we are adding 1 to the",y)
    y=y+1
    if(y==7):
        print(y,"is equal to 7 and we are stopping thsi program here")
else:
    print("continue")


# In[14]:


tasks = []

while True:
    print("1: Enter your new task")
    print("2: Remove the task")
    print("3: View tasks")
    print("4: Exit")

    choice = input('Enter your choice: ')

    if choice == "1":
        new_task = input("Enter your new task: ")
        tasks.append(new_task)

    elif choice == "2":
        if tasks:
            task_to_remove = input("Enter the task you want to remove: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
            else:
                print("Task not found.")
        else:
            print("No tasks to remove.")

    elif choice == "3":
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f'{index}. {task}')
        else:
            print("No tasks to view.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")


# In[2]:


x=list(range(0,21,4))
print(x)


# In[3]:


p=["apple","mango","happy"]
print(p)


# In[7]:


x=list(range(0,98,3))
print(x)


# In[11]:


a=[2,4,6,8,10] #zip allows us to print the pairing element having same cardanility
b=['a','e','i','o','u']
c=list(zip(a,b))
print(c)


# In[21]:


#list coprehension
# it allows us to build out the list using diffeent notation
# one line of loop
test=[x for x in "jay-nepal"]
print(test)


# In[25]:


y=list(range(0,11))
print(y)
z=[k*k for k in y]
print(z)


# In[28]:


a=[ m**2 for m in range(0,11,2)]
print(a)


# In[33]:


a=[m for m in range(0,11) if m%2==0]
print(a)


# In[35]:


c=[0,-40,40,100]
f=[((9/5)*temp+32) for temp in c]
print(f)


# In[36]:


a=[x**2 for x in[x**2 for x in range(0,12)]]
print(a)


# # funtion

# In[3]:


def squarefunction(a):
    return a**2
mylist=[2,3,5,7,9]
result=list(map(squarefunction,mylist))
print(result)


# In[5]:


def function(b):
    if len(b)%2==0:
        return"even"
    else:
        return("odd")
    
   


# In[9]:


player=['messi','ronaldo','saurez']
result=list(map(function,player))
print(result)


# In[15]:


def filterfunc(a):
    return a%2==0
b=[2,4,6,8,10,12,14]
c=list(filter(filterfunc,b))
print(c)


# In[16]:


#lambda
a= lambda b:b*3
result=a(7)
print(result)


# In[22]:


a=[2,3,4,5,6]
b=list(map(lambda c:c*2,a))
print(b)


# In[18]:


#arg
def function(*a):
    return a*2


# In[19]:


test=function(1,2,3,4)
print(test)


# In[20]:


def func(*a):
    return len(a)


# In[21]:


test=func('my','function')
print(test)


# # day 12

# In[9]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# In[5]:


a=np.array((1))
print(arr)


# # dimenssioon in array

# In[10]:


arr=np.array([1])
print(arr)
print(arr.ndim)


# In[11]:


arr=np.array([1,2,3,4,5,6])
print(arr)
print(arr.ndim)


# In[16]:


#2d array
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)


# In[24]:


# 3d array
a=np.array([[[1,2,3],[4,5,6]]])
print(a)
print(a.ndim)


# In[25]:


#print upto 4 dimenssional array
a=np.array(1)
b=np.array([1,2])
c=np.array([[2,3]])
d=np.array([[[3,4]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[31]:


#numpy array indexing
a=np.array([1,2,3,4,5])
print(a[0])
print('the 4rth elemnt of the array lis is',a[3])




# In[37]:


#array indexing for 2d 
a=np.array([[1,4,6,22],[6,8,10,14]])
print("2nd elemnet on the first row is",a[0,1])
print("the third element in 2nd row is",a[1,2])


# In[38]:


import numpy as np

a = np.array([[[1, 4, 76, 44], [12, 34, 56, 78]], [[98, 34, 55, 19], [84, 4, 10, 60]]])
print(a[0, 1, 3])


# In[1]:


import numpy as n
a=n.array([[[7,12,34,54],[90,34,77,19]],[[12,43,56,77],[88,41,90,91]]])
print(a[1,1,1])


# # day 13

# In[2]:


#slicing of numpy arrays
import numpy as n
a=n.array([[[11,23,44,55,66],[90,80,70,60,50],[11,22,33,44,55]]])
print(a[0,1,1:3])


# In[5]:


#checking the data type of an array
a=n.array([[[11,23,44,55,66],[90,80,70,60,50],[11,22,33,44,55]]])
print(a.dtype)




# In[6]:


a=n.array(["cat","dog"])
print(a.dtype)


# In[9]:


#creating array by user defined data type
a=n.array([1,2,3,4],dtype="S")
print(a)
print(a.dtype)


# In[11]:


#create an array with data type 4 byte integer
a=n.array([1,2,3],dtype="i4")
print(a)
print(a.dtype)


# In[13]:


#numpy array shape
#shape of an array is number of elements in each direction
 #print the shape of 2d array
a=n.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)
     


# In[14]:


a=n.array([[[11,23,44,55,66],[90,80,70,60,50],[11,22,33,44,55]]])
print(a.shape)


# In[15]:


#joining the numpy array


# In[17]:


a=n.array([1,2,3])
b=n.array([4,5,6])
c=n.concatenate((a,b))
print(c)


# In[18]:


a=n.array([[1,2],[3,4]])
b=n.array([[5,6],[7,8 ]])
c= n.concatenate((a,b),axis=1)
print(c)


# In[4]:


#splitting the array
import numpy as n
a=n.array([1,3,4,5,6])
b=n.array_split(a,4)
print(b)


# In[2]:


import numpy as n
a=n.array([[1,2],[3,4]])
b=n.array([[5,6],[7,8 ]])
c= n.concatenate((a,b),axis=0)
print(c)


# In[3]:


a=n.array([1,2,3,4,5,6,7 ])
b=n.array_split(a,5)
print(b)


# In[11]:


#ravel and flatten function
#they convert multi_dimenssional array into 1d array

a=n.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a)
print("the dimenssion is",a.ndim)
b= a.flatten()
print(b)
print("the dimenssion is",b.ndim)


# In[14]:


a=n.array([[[[1,2,3],[4,5,6],[7,8,9]]]])
print(a)
print("the dimenssion of array is",a.ndim)
b=n.ravel(a)
print(b)
print("the dimenssion of array is",b.ndim)


# In[13]:


#unique function
k=n.array([1,2,3,4,5,1,4,7,9,0,7])
print(k)
b=n.unique(k)
print(b)


# In[16]:


k=n.array([1,2,3,4,5,1,4,7,9,0,7])
print(k)
b=n.unique(k,return_index=True,return_counts=True)
print(b)


# In[17]:


k=n.array([1,2,3,4,5,1,4,7,9,0,7])
b=n.delete(k,[1])
print(b)


# In[22]:


a=n.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
print(a)
b=n.delete(a,1,axis=1)
print(b)


# # day 14

# In[9]:


#pandas library
import pandas as p
a=p.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
a.tail()#the tail reads and display the last 5 data of the list
#head displays first 5


# In[13]:


a.dtypes


# In[12]:


a.describe()


# In[14]:


a


# In[18]:


a[['Name','Sex','Cabin','Ticket','Embarked']]


# In[19]:


a.dtypes=='object'


# In[20]:


a.dtypes=='float'


# In[3]:


import pandas as p
a=p.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
a.tail()


# In[6]:


a[a.dtypes[a.dtypes=='float64'].index]


# In[7]:


a.describe()


# In[8]:


a.dtypes


# In[10]:


a[a.dtypes[a.dtypes=="int64"].index]


# In[11]:


a.head(10)


# In[2]:


import pandas as p
a=p.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
a.tail()


# df.columns

# In[5]:


a.columns


# In[7]:


a[['Ticket']]


# In[11]:


a[['Ticket']][7:16:2]


# In[14]:


a[['Ticket','Cabin',"Name"]][4:17:3]


# In[18]:


a[['player']]=2


# In[23]:


a.insert(loc=3,column="food",value=0)


# In[24]:


a


# In[25]:


a.insert(loc=6,column="equipment",value="oxygen cylinder")


# In[26]:


a


# In[1]:


import pandas as p
a=p.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
a.tail()


# In[2]:


a.dtypes


# In[4]:


a[a.dtypes[a.dtypes=="int64"].index]


# In[7]:


a.columns


# In[8]:


a[['Parch','Fare','Cabin']]


# In[9]:


a[['Fare']][0:20:4]


# In[10]:


a.insert(loc=6,column="dancers",value="belly dancers")


# In[11]:


a


# In[13]:


a.head(13)


# In[14]:


a.tail(7)


# In[15]:


a.insert(loc=1,column="country",value="nepal")


# In[16]:


a


# In[1]:


import pandas as p


# In[5]:


a=p.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[6]:


a


# In[7]:


a.columns


# In[8]:


a[["Name"]]


# In[11]:


b=a["Name"][0:10]


# In[12]:


type(b)


# In[13]:


c=["biplaw",'a1','a2','a3','a4','a5','a6','a7','a8','a9']


# In[17]:


p.Series(b,index=c)


# In[18]:


p.Series(list(b),index=c)


# In[20]:


m1=p.Series([100,200,300,400,500],index=[1,2,3,4,5])


# In[21]:


m1


# In[22]:


m2=p.Series([600,700,800,900,1000],index=[1,2,3,4,5])


# In[23]:


m2


# In[24]:


m3=p.concat([m1,m2])


# In[ ]:





# In[25]:


m3


# In[26]:


m3[1]


# In[27]:


m1*m2


# In[28]:


m1+m2


# In[33]:


a.head()


# In[40]:


import pandas as p
a.drop("PassengerId",axis=1)


# In[47]:


a.drop('Survived',axis=1, inplace=True)


# In[48]:


a


# In[ ]:




