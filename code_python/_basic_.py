
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


# In[120]:


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

