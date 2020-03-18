
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


# In[158]:


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


# In[159]:


#__regular_expression__
import re
regex = re.compile("^.+(sub-.+)_(ses-.+)_(mod-.+)")
strings = ["abcsub-33_ses-01_mod-mri", "defsub-04_ses-01_mod-mri","ghisub-055_ses-02_mod-ctscan"]
print([regex.findall(s)[0] for s in strings])


# In[173]:


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


# In[174]:


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
thread1 = threading3



