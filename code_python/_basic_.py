
# coding: utf-8

# In[ ]:


#__tuples___
digits = (0, 1, 'two')
digits2 = tuple([0, 1, 'two'])
zero = (0,)
#digits
#zero

digits[2]
len(digits)
digits.count(2)
digits.index(1)

digits2 = digits + (3,4,5)
digits2

(23,43,9) * 2

animals = ('cat', 23, 'dog')
animals


# In[ ]:


#____strings____
s = str(948234)
s2 = 'enigma code binary'
s2[4]
len(s2)
#s2[:5]
#s[1:]
#s[-2]
minus = s2.lower()
minus
mayus = s2.upper()
mayus

s2.startswith('e')
s2.endswith('y')
s2
s2.isdigit()
s.find('code')
s2.replace('code', 'blockcode')

s2.split(' ')
s2.split()
s3 = 'a, an, the'
s3.split(',')
stooges = ['konan', 'nagato','naruto']
print(stooges)
strjoin = ' '.join(stooges)
print(strjoin)
strtext1 ="statistics machine learning python draft"
print(strtext1)
strtext2 = '10101'
strtotal = strtext1 + ' '+ strtext2
print(strtotal)
strtotal2 = strtotal +' '+ 'value pi= ' +str(3.294)
print(strtotal2)

#__remove whitespace_...
text4 = '   book code crypton   '
new_text = text4.strip()
print(new_text)

#_string substitutions
text_format1 = 'technology %s digital money %s' % ('blockchain', 'bitcoin')
text_format2 = 'raining {} and {}'.format('enigma', 'criptography')
text_format3 = 'car {arg1} -  model {arg2}'.format(arg1='lanborguini', arg2='veneno')
text_format4 = 'pi is {:.2f}'.format(3.1415)
#print(text_format1)
#print(text_format2)
#print(text_format3)
#print(text_format4)

print('first line\nsecond line')
print(r'first line\nsecond line')
btext = b'first line\nsecond line'
print(btext)
print(btext.decode('utf-8').split())


# In[ ]:


#__dictionaries__

#...create an empty dictionary...
empty_dict={}
empty_dict2 = dict()
#print(empty_dict)
#print(empty_dict2)

#create a dictionary
soda_ = {'bebida':'coca-cola', 'sabor':'cafe', 'litro':1.5}
print(family)

cookies_ = dict(marca='costa', tipo='wafer',sabor='chocolate', und=6)
print(cookies_)

# convert a list of tuples into a dictionary
list_of_tuples = [('polo','corto'),('color','rojo'),('tamaño','s')]
polo_ = dict(list_of_tuples)
print(polo_)

# examine a dictionary
polo_['color']
print(len(polo_))
print(len(cookies_))
cookies_keys = cookies_.keys()
print(cookies_keys)
cookies_values = cookies_.values()
print(cookies_values)
cookies_items = cookies_.items()
print(cookies_items)

'marca' in cookies_  # True--- solo para claves

#__modify a dictionary_
cookies_['sabor'] = 'fresa'
print(cookies_)
del polo_['color']
print(polo_)

polo_['color'] = ['naranja', 'verde']
print(polo_)
polo_.pop('color')
print(polo_)
polo_.update({'genero':'male','edad':23})
print(polo_)
polo_.get('genero')

#__accesing a lis element within a dictionary
cookies_['sabor'][:]
cookies_['marca'].remove('')


# In[ ]:


#--- sets____
#..create an empty set
empty_set = set()

# create a set
languages = {'python', 'go', 'perl'}
animals =set(['piton', 'hanster', 'camello'])

# examine a set
len(languages)
'go' in languages

# set operations
languages | animals
languages & animals
languages - animals
animals - languages

# modify a set
languages.add('postgresql')
animals.add('elefante')
languages.remove('python')
animals.remove('piton')
languages
animals

try:
    languages.remove('java')
except KeyError as e:
    print("Errror", e)

languages.discard('g')
languages
animals.pop()
animals.clear()
animals.update('hanster', 'elefante', 'bird')

#.. get a sorted list of unique elements from a list
sorted(set([9,0,2,1,0]))


# In[ ]:


#_____conditional_statements____
x = 54
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')

#..single-line
if x > 0: print('positive')
#ternario-operator
'positive' if x > 0 else 'zero or negative'    


# In[ ]:


#___loops____
#range returns a list of integers
#range(0, 3) , range(4), range(0, 4, 2)
languageCoders = ['jscript','scala','kotlin','clojure','haskell']
for i in range(len(languageCoders)):
    print(languageCoders[i].upper())

for x in range(2**4):
    pass

#...iterate through two things at once (using tuple unpacking)
cellphone = {'marca':'huawei', 'modelo':'mate pro', 'color':'azul','version s.o.':9}
print("....cellphone....")
for key, value in cellphone.items():
    print(key, value)

for lang_ in range(len(languageCoders)):
    if languageCoders[lang_] == 'scala':
        print("language programming {}".format(languageCoders[lang_]))
        break
    else:
        print('No language for coders')

# while loop
count = 0
while count < 5:
    print('go print 5 times {}'.format(count))
    count += 1


# In[ ]:


#___exceptions_handling___
dct = dict(a=[12,43], b=[34,99])
key = 'c'
try:
    dct[key]
except:
    print("key %s is missing. Add it with empty value" % key)
    dct['c'] = []

print(dct)


# In[ ]:


#___functions___
def print_text():
    print('enigma-code')

print_text()

def print_this(x):
    print(x, "......")

print_this(2333)

def square_this(x):
    return x ** 2

power_2 = square_this(3)
print(power_2)

def power_this(x, power=2):
    return x ** power

power3 = power_this(5)
print(power3)

def stub():
    pass

def min_max(nums):
    return min(nums), max(nums)

nums = [23, 54, 95, 5, 43, 90,1]
min_max_num = min_max(nums)
print(min_max_num)

min_num, max_num = min_max(nums)
min_num
max_num


# In[ ]:


#___list_comprehensions_iterators
nums = [11, 22,33,44,55]
cubes = []
for num in nums:
    cubes.append(num ** 3)

cubes

cubes2 = [num ** 3 for num in nums]
cubes2

# for loop to create a list of cubes of even numbers
cubes_five_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_five_of_even.append(num **4)
    else:
        cubes_five_of_even.append(num **3)
five_of_even

five_of_even_2 = [num ** 4  if num % 2 == 0 else num ** 3 for num in nums ]
five_of_even_2


#__for loop to flatten a 2d-matrix
matrix = [[1,2], [3,4]]
items = []

for row in matrix:
    for item in row:
        items.append(item)
        
items

#==> equivalent list comprehension
items2 = [item for row in matrix
              for item in row]
items2

#==> set comprehension
fruits = ['graphes', 'cherry','apple','banana']
unique_lengths = {len(fruit) for fruit in fruits}
unique_lengths

#===> dictionary comphension
fruit_lengths = {fruit:len(fruit) for fruit in fruits}
fruit_lengths


# In[ ]:


#__regular_expression__
import re
regex = re.compile("^.+(sub-.+)_(ses-.+)_(mod-.+)")
strings = ["abcsub-33_ses-01_mod-mri", "defsub-04_ses-01_mod-mri","ghisub-055_ses-02_mod-ctscan"]
print([regex.findall(s)[0] for s in strings])


# In[ ]:


#__system_programming__

import os
import tempfile

cwd = os.getcwd()
print(cwd)

os.chdir(cwd)

#temporary directory
tmpdir = tempfile.gettempdir()

#..join paths
mytmpdir = os.path.join(tmpdir, "foobar")
os.listdir(tmpdir)

#..create a directory
if not os.path.exists(mytmpdir):
    os.mkdir(mytmpdir)

os.makedirs(os.path.join(tmpdir, "foobar", "plop","toto"), exist_ok=True)

#..file_i/o
filename = os.path.join(mytmpdir, "myfile.txt")
print(filename)

#write
lines = ["Enigma code 3000", "programming in python enigma"]

##..write line by line
fd = open(filename, "w")
fd.write(lines[0] + "\n")
fd.write(lines[1] + "\n")
fd.close()

## use a context manager to automatically close your file
with open(filename, 'w') as f:
    for line in lines:
        f.write(line + '\n')
        
#read 
## read one line at a time
f = open(filename, "r")
#f.readline()
f.readlines()
f.close()

#-------
f2 = open(filename,'r')
[line for line in f2]
f2.close()

##...
with open(filename, 'r') as f:
    lines=[line for line in f]


# In[ ]:


#... multiprocessing and multithreading
import time
import threading

def list_append(count, sign=1, out_list=None):
    if out_list is None:
        out_list = list()
    for i in range(count):
        out_list.append(sign * i)
        sum(out_list)
    return out_list

size = 10000 # number of numbers to add

out_list = list()
thread1 = threading.Thread(target=list_append, args=(size, 1, out_list, ))
thread2 = threading.Thread(target=list_append, args=(size, -1, out_list, ))

startime = time.time()
# will execute both in parallel
thread1.start()
thread2.start()

# joins threads back to the parent process
thread1.join()
thread2.join()

print("Threading ellapsed time", time.time() - startime)
print(out_list[:10])


# In[ ]:


#_multiprocessing
import multiprocessing

# sharing requires specific mecanism
out_list1 = multiprocessing.Manager().list()
p1 = multiprocessing.Process(target=list_append, args=(size, 1,None))
out_list2 = multiprocessing.Manager().list()
p2 = multiprocessing.Process(target=list_append, args=(size, -1,None))

startime = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print("Multiprocessing ellapsed time ", time.time() - startime)


# In[ ]:


#:.....Object_Oriented_Programming (OPP):
import math

class Shape2D:
    def area(self):
        raise NotImplementedError()
    
# __init__ is a special method called the constructor

#Inheritance + encapsulation
class Square(Shape2D):
    def __init__(self, width):
        self.width = width
        
    def area(self):
        return self.width ** 2

class Disk(Shape2D):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

shapes = [Square(2), Disk(3)]

# polymorphism
print([s.area() for s in shapes])

s = Shape2D()
try:
    s.area()
except NotImplementedError as e:
    print("NotImplementedError")


# In[ ]:


#___ NUMPY_:arrays_and_matrices
from __future__ import print_function
import numpy as np

#__ create arrays ___
data1 = [1, 2, 3, 4, 5]
arr1 = np.array(data1)
print("array = ", data1)
print("array(np) = ", arr1)

data2 = [range(1, 5), range(5, 9)] #list of lists
arr2 = np.array(data2)
print("array2(list of lists): ", arr2)
print ("convert arr->list ", arr2.tolist()) #convert array back to list

int_array = np.arange(5)
float_array = int_array.astype(float)
print("...", float_array)

#.. examining arrays....
arr1.dtype # int32
arr2.dtype # int32
arr2.ndim  # 2
arr2.shape # (2, 4)
arr2.size  # 8
len(arr2)  # 2

#__ reshaping ...
arr = np.arange(10, dtype=float).reshape((2, 5))
print("reshaping_: ", arr.shape)
print(arr.reshape(5, 2))

a = np.array([0, 1])
a_col = a[:, np.newaxis]
print(a_col)
# or
a_col = a[:, None]
print(a_col.T)

arr_flt = arr.flatten()
arr_flt[0] = 43
print(arr_flt)
print(arr)

#... stack arrays...
a = np.array([0, 1])
b = np.array([2, 3])
ab = np.stack((a, b)).T
print("ab: ", ab)
#.. or ..
np.hstack((a[:, None], b[:, None]))


# In[ ]:


#..selection..
arr = np.arange(10, dtype=float).reshape((2, 5))
#print(arr)
arr[0]
arr[0, 3]
arr[0][3]

#_.slicing...
arr[0, :]
arr[:, 0]
arr[:, :2]
arr[:, 2:]
arr2 = arr[:, 1:4]
#print(arr2)

#.......
arr2[0, 0] = 33
#print("arr2: ", arr2 )
#print("arr: ",arr)
#print("arr__: " ,arr[0, ::-1])

#_. fancy_indexing...
arr2 = arr[:, [1,2,3]]
#print("arr2::_ ", arr2)
arr2[0,0] = 44
#print(":: ", arr2)
#print(":::: ", arr)

arr2 = arr[ arr > 5]
#print("arr:>: ", arr2)
arr2[0] = 44
#print("arr_modify:: ", arr2)

#__boolena arrays indexing continues
names = np.array(['Bob', 'Joe','Will','Bob'])
names == 'Bob'
names[names != 'Bob']
(names == 'Bob') |(names== 'Will')
names[names != 'Bob'] = 'Joe'
np.unique(names)

#.. vectorized operations
nums = np.arange(5)
nums * 10
nums = np.sqrt(nums)
np.ceil(nums)
np.isnan(nums)
nums + np.arange(5)
np.maximum(nums, np.array([1, -2, 3, -4, 5]))

# compute euclidean distance between 2 vectors
vec1 = np.random.randn(10)
vec2 = np.random.randn(10)
dist = np.sqrt(np.sum((vec1 - vec2) ** 2))
print(dist)

# math and stats
rnd = np.random.randn(4, 2)
rnd.mean()
rnd.std()
rnd.argmin()
rnd.sum()
rnd.sum(axis=0)
rnd.sum(axis=1)

#.. methods for boolean arrays
(rnd > 0).sum()
(rnd > 0).any()
(rnd > 0).all()

# random numbers
np.random.seed(12234)
np.random.rand(2, 3)
np.random.randn(10)
np.random.randint(0, 2, 10)


# In[ ]:


#..BROADCASTING::__rules..
a = np.array([[0, 0, 0],
             [10, 10, 10],
             [20, 20, 20],
             [30, 30, 30]])
b = np.array([0, 1, 2])
print(a + b)
 


# In[ ]:


#..PANDAS....
from __future__ import print_function

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#... create DataFrame
columns = ['name', 'age', 'gender', 'job']

user1 = pd.DataFrame([['alice', 19, "F", "student"],
                     ['john', 26, "M", "manager"]],
                    columns = columns)
user2 = pd.DataFrame([['eric', 22, 'M', "student"],
                     ['paul', 58, "F", "manager"]],
                    columns = columns)
user3 = pd.DataFrame(dict(name=['peter','julie'],
                         age=[33,44], gender =['M', 'F'],
                         job=['engineer', 'scientist']))
#print(user1)
print()
#print(user3)
#user1

#...combining dataframes
#__concatenate dataFrame
users = pd.concat([user1, user2, user3])
#print(users)
print()
#user1.append(user2)

#.. join dataFrame...
user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric', 'julie'],
                         height = [165, 180, 142, 172]))
#print(user4)

merge_inter = pd.merge(users, user4, on="name")
#print(merge_inter)

#print()

users = pd.merge(users, user4, on="name", how='outer')
#print(users)

#__reshaping by pivoting__
staked = pd.melt(users, id_vars="name", var_name="variable", value_name="value")
#print(staked)

#print()

#print(staked.pivot(index='name', columns='variable', values='value'))

#__summarizing
users
#type(users)
users.head()
users.tail()

users.index
users.columns
users.dtypes
users.shape
users.values
users.info()


#.. columns_selection__
users['gender']
#type(users['gender'])
users.gender

#select multiple colums
#users[['age', 'gender']]
#my_cols =['age','gender']
users[my_cols]
type(users[my_cols])


# In[ ]:


#_ rows_selection_
df = users.copy()
df.iloc[0]
df.iloc[0,0]
df.iloc[0,0] = 55

for i in range(users.shape[0]):
    row = df.iloc[i]
    row.age *= 100

#print(df)

print()

df.ix[0]
df.ix[0,"age"]
df.ix[0,"age"] = 54

for i in range(df.shape[0]):
    df.ix[i, "age"] *= 10

print(df)


# In[ ]:


#...rows_selection(filtering)...
users[users.age < 20]
young_bool = users.age < 20
young = users[young_bool]
users[users.age < 20].job
print(young)

users[users.age < 20][['age', 'job']]
users[(users.age > 20) & (users.gender == 'M')]
users[users.job.isin(['student', 'engineer'])]

#__sorting___
df = users.copy()

df.age.sort_values()
df.sort_values(by='age')
df.sort_values(by='age', ascending=False)
df.sort_values(by=['job','age'])
df.sort_values(by=['job','age'], inplace=True)

#__descriptive statistics
print(df.describe())
print()
print(df.describe(include='all'))
print()
print(df.describe(include=['object']))


# In[ ]:


#.. statistics per group
print(df.groupby("job").mean())
print("......................")
print(df.groupby("job")["age"].mean())
print("----------------------")
print(df.groupby("job").describe(include='all'))
print(".......................")
for grp, data in df.groupby("job"):
    print(grp, data)


# In[ ]:


#__Quality_check___
#..remove_duplicate_date
df = users.append(df.iloc[0], ignore_index=True)

#print(df.duplicated()) #series of booleans
df.duplicated().sum()
df[df.duplicated()]
df.age.duplicated()
df.duplicated(['age','gender']).sum()
df = df.drop_duplicates()

#..missing_data
df = users.copy()
df.describe(include='all')

#..find missing values in a Series
df.height.isnull()
df.height.notnull()
df[df.height.notnull()]
df.height.isnull().sum()

#find missing values in a DataFrame
df.isnull()
df.isnull().sum()

#..drop missing values
df.dropna()
df.dropna(how='all')

#..fill in missing values
df.height.mean()
df = users.copy()
df.ix[df.height.isnull(), "height"] = df["height"].mean()
print(df)


# In[ ]:


#:__rename_values__
df = users.copy()
print(df.columns)
df.columns = ['age','genre','traveli','nom','taille']
#df.travail = df.travail.map({'student':'studiant', 'manger':'manager','engineer':'ingeneiur','scientist':'scientific'})
#assert  df.travail.isnull().sum() == 0

#df['travail'].str.contains("etu|inge")
#errror


# In[ ]:


#...dealing_with_outliers....
size = pd.Series(np.random.normal(loc=175, size=20, scale=10))
size[:3] += 500
size

#--based on parametric statistics:: use the mean
size_outlr_mean = size.copy()
size_outlr_mean[((size - size.mean()).abs() > 3 * size.std())] = size.mean()
print(size_outlr_mean.mean())

#...based on non-parametric statistics: use the median
mad = 1.4826 * np.median(np.abs(size - size.median()))
size_outlr_mad = size.copy()

size_outlr_mad[((size - size.median()).abs() > 3 * mad)] = size.median()
print(size_outlr_mad.mean(), size_outlr_mad.median())


# In[ ]:


#-- File- I/O
#...csv
import tempfile, os.path
tmpdir = tempfile.gettempdir()
csv_filename = os.path.join(tmpdir, "users.csv")
users.to_csv(csv_filename, index=False)
other = pd.read_csv(csv_filename)
other


# In[ ]:


#..excel...
xls_filename = os.path.join(tmpdir, "users.xlsx")
users.to_excel(xls_filename, sheet_name='users', index=False)

pd.read_excel(xls_filename, sheet_name='users')

# multiple sheets
with pd.ExcelWriter(xls_filename) as writer:
    users.to_excel(writer, sheet_name='users', index=False)
    df.to_excel(writer, sheet_name='salary', index=False)
    
pd.read_excel(xls_filename, sheet_name='users')
pd.read_excel(xls_filename, sheet_name='salary')


# In[ ]:


#__ sqlite__
import pandas as pd
import sqlite3

db_filename = os.path.join(tmpdir, "users.db")
conn = sqlite3.connect(db_filename)
#...........


# In[ ]:


#####____MATPLOTLIB____
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(0, 10, 50)
sinus = np.sin(x)

plt.plot(x, sinus)
plt.show()

print()

plt.plot(x, sinus, "o")
plt.show()


# In[ ]:


# rapid multiplot
cosinus = np.cos(x)
plt.plot(x, sinus, "-b", x, sinus, "ob", x, cosinus, "-r", x, cosinus, "or")
plt.xlabel('this is x!')
plt.ylabel('this is y!')
plt.title('my first plot')
plt.show()


# In[ ]:


# step by step
plt.plot(x, sinus, label='sinus', color='blue', linestyle='--', linewidth=2)
plt.plot(x, cosinus, label='cosinus', color='red', linestyle='-', linewidth=2)
plt.legend()
plt.show()


# In[ ]:

 