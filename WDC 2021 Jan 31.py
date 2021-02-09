#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello, world!')


# # Agenda
# 
# 0. About assignment, `==` and `is`
# 1. Basic data structures — how they work
# 2. `Decimal`
# 3. `namedtuple`
# 4. Variations on `dict`

# In[2]:


import sys
sys.version


# In[3]:


x = 100
y = 100

x == y


# In[4]:


x is y


# In[5]:


x = 1000
y = 1000

x == y


# In[6]:


x is y


# In[7]:


x == y   # x.__eq__(y)


# In[8]:


x is y


# In[9]:


id(x)


# In[10]:


id(y)


# In[11]:


x is y   # id(x) == id(y)


# In[12]:


x = 100
y = 100

x is y


# In[13]:


x = 1000
y = 1000

x is y


# In[14]:


x = None

if x == None:  # non-Pythonic
    print('Yes, it is None!')


# In[15]:


if x is None:   # VERY Pythonic
    print('Yes, it is None!')


# In[16]:


x = 100
y = x

x = 200
y


# In[17]:


x = 100
x += 5

x


# In[18]:


x = 'abcde'
x[0] = '!'  # str is immutable


# In[19]:


x = 'fghij'


# In[20]:


import sys
x = 0
sys.getsizeof(x)


# In[21]:


x = 1234567890
sys.getsizeof(x)


# In[22]:


x = x ** 10
sys.getsizeof(x)


# In[23]:


x = x ** 100
sys.getsizeof(x)


# In[1]:


a = 1
type(a)


# In[2]:


a = 1.0
type(a)


# In[3]:


0.1 + 0.2


# In[4]:


0.1 + 0.2 == 0.3


# In[5]:


round(0.1 + 0.2, 2)


# In[6]:


round(0.1 + 0.2, 2) == 0.3


# In[7]:


# BCD -- binary coded decimals


# In[8]:


123   # 0b1 0b2 0b3


# In[9]:


from decimal import Decimal 

a = Decimal('0.1')
b = Decimal('0.2')

a + b


# In[10]:


float(a+b)


# In[12]:


import sys
sys.getsizeof(a)


# In[13]:


sys.getsizeof(b)


# In[14]:


sys.getsizeof(0.1)


# In[15]:



a = Decimal(0.1)
b = Decimal(0.2)

a + b


# In[16]:


a


# In[17]:


b


# In[18]:


1/3


# In[19]:


from math import isclose


# In[20]:


isclose(0.1+0.2, 0.3)


# In[21]:


isclose(0.1+0.2, 0.3, rel_tol=0.000000000000000001)


# In[22]:


isclose(0.1+0.2, 0.3, rel_tol=0.1)


# In[24]:


x = 0.1
y = 0.2

f'{x} + {y} = {x+y:0.2}'


# In[25]:


x = 'abcd'
y = 'abcd' 

x == y


# In[26]:


x is y


# In[27]:


x = 'abcd' * 5000
y = 'abcd' * 5000

x == y


# In[28]:


x is y


# In[29]:


x = 'ab.cd'
y = 'ab.cd'

x == y


# In[30]:


x is y


# In[31]:


a = 100
b = [10, 20, 30]


# In[32]:


globals() 


# In[33]:


globals()['a']


# In[34]:


globals()['b']


# In[35]:


globals()['a'] = 987

a


# In[36]:


print(a)


# In[37]:


# interning -- cache of string


# In[38]:


x = 'abcde'   
y = 'abcde'

x is y


# In[39]:


x = 'abcde' * 2000
y = 'abcde' * 2000

x is y


# In[40]:


x = 'ab.cd'
y = 'ab.cd'


# In[41]:


x is y


# In[43]:


x = sys.intern('ab.cde')
y = sys.intern('ab.cde')


# In[44]:


x is y


# In[45]:


for i in range(5):
    print(x)   # print(globals()['x'])


# In[46]:


# f-string
# str.format
# str % ('a', 'b')  -- printf-ish


# In[47]:


x = 100
y = [10, 20, 30]
z = {'a':1, 'b':2}

s = f'x = {x}, y = {y}, z = {z}'


# In[48]:


print(s)


# In[49]:


d = {'a':1, 'b':200, 'cdefg': 3, 'hijklmn': 45678}

for key, value in d.items():
    print(f'{key}: {value}')


# In[50]:



for key, value in d.items():
    print(f'{key:8}: {value:8}')


# In[51]:



for key, value in d.items():
    print(f'{key:8}{value:8}')


# In[52]:



for key, value in d.items():
    print(f'{key:.<8}{value:*>8}')


# In[54]:



for key, value in d.items():
    print(f'{key:.>8} {value:*<8}')


# In[55]:


f = 123456.7890123

print(f'The number is {f}.')


# In[58]:


print(f'The number is {f:6.5}.')


# In[59]:


x


# In[60]:


y


# In[61]:


z


# In[62]:


print(f'x = {x}, y = {y}, z = {z}')


# In[63]:


# From Python 3.8, we can do this:

print(f'{x=}, {y=}, {z=}')


# In[64]:


mylist = [10, 20, 30, 40, 50]


# In[65]:


type(mylist)


# In[66]:


mylist.append(60)
mylist


# In[68]:


mylist = []
for i in range(60):
    print(f'{i}: len(mylist) = {len(mylist)}, sys.getsizeof(mylist) = {sys.getsizeof(mylist)}')
    mylist.append(i)


# In[69]:


[1] * 100


# In[70]:


# sequence -- string, list, tuple

t = (10, 20, 30, 40, 50)
type(t)


# In[71]:


# no parens needed!
t = 10, 20, 30, 40, 50

t


# In[72]:


type(t)


# In[73]:


t = ([10, 20, 30],
     [100, 200,300, 400, 500])

t


# In[74]:


t[0] = '!'


# In[75]:


t[0].append(40)
t


# In[76]:


p = ('Reuven', 'Lerner', 46)
p


# In[77]:


p[0]


# In[79]:


p[1]


# In[80]:


p[2]


# In[81]:


# named tuples


# In[82]:


from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'shoesize'])


# In[83]:


class Foo:
    pass


# In[84]:


Foo.__name__


# In[87]:


# namedtuple returns a new class
# the list of strings shows the fields that we can create

Person = namedtuple('Person',
                    ['first', 'last', 'shoesize'])


# In[88]:


Person.__name__


# In[89]:


p = Person('Reuven', 'Lerner', 46)


# In[90]:


p


# In[91]:


p[0]


# In[92]:


p[1]


# In[93]:


p[2]


# In[94]:


p.first


# In[95]:


p.last


# In[96]:


p.shoesize


# In[97]:


type(Person)


# In[98]:


type(Person)


# In[99]:


p1 = Person('first1', 'last1', 1)
p2 = Person('first2', 'last2', 2)


# In[100]:


p1


# In[101]:


p2


# In[102]:


type(p1)


# In[103]:


type(p2)


# In[104]:


p1.first


# In[105]:


p1.first = 'asdfafafa'


# In[106]:


p1._replace(first='zzzzz')


# In[107]:


p1 = p1._replace(first='zzzzz')
p1


# In[108]:


t


# In[109]:


t[0].append(50)
t


# In[110]:


t[0] += [60, 70, 80]    # __iadd__ # (1) adds (2) assigns


# In[111]:


t


# In[112]:


t[0].extend([90, 91, 92])
t


# In[113]:


# tuple with 1 element
t = (10,)  
type(t)


# In[114]:


t = (10)
type(t)


# # Exercise: Bookstore
# 
# 1. Create, using `namedtuple`, a new `Book` class, which has three attributes: `title`, `author`, and `price`.
# 2. Create a list of `Book` objects (3-4 is fine), and put them inain a list.
# 3. Ask the user repeatedly to enter the name of a book they want to buy.
#     - If the book is in inventory, then print all of its details, and add the price to the total
#     - If the book is *not* in inventory, then tell the user
#     - If we get an empty string, then we stop asking
# 4. At the end, tell the user the final price.

# In[115]:


from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'price'])

b1 = Book('title1', 'author1', 50)
b2 = Book('title2', 'author1', 100)
b3 = Book('title3', 'author2', 200)

all_books = [b1, b2, b3]

all_books


# In[118]:


total = 0

while True:
    s = input('Enter book title: ').strip()
    
    if not s:    # if s is empty, then exit from the loop
        break
        
    found_book = False
    for one_book in all_books:
        if one_book.title == s:
            print(f'Found {s} by {one_book.author}, price {one_book.price}')
            total += one_book.price
            found_book = True
            break
            
    if not found_book:
        print(f'Did not find {s}')
            
print(f'Total is {total}')


# In[119]:


total = 0

while True:
    s = input('Enter book title: ').strip()
    
    if not s:    # if s is empty, then exit from the loop
        break
        
    for one_book in all_books:
        if one_book.title == s:
            print(f'Found {s} by {one_book.author}, price {one_book.price}')
            total += one_book.price
            break
            
    else:    # got_to_end_of_loop_without_encountering_a_break
        print(f'Did not find {s}')
            
print(f'Total is {total}')


# In[121]:


total = 0

# := "assignment expression"
# "walrus"
# starting with Python 3.8

while s := input('Enter book title: ').strip():
    
    for one_book in all_books:
        if one_book.title == s:
            print(f'Found {s} by {one_book.author}, price {one_book.price}')
            total += one_book.price
            break
            
    else:    # got_to_end_of_loop_without_encountering_a_break
        print(f'Did not find {s}')
            
print(f'Total is {total}')


# In[123]:


if x := 5:
   print(x)


# In[124]:


print(f'{b1=}, {b2=}, {b3=}')


# In[125]:


# unpacking
mylist = [10, 20, 30]

x,y,z = mylist


# In[126]:


print(f'{x=}, {y=}, {z=}')


# In[127]:


title, author, price = b1


# In[128]:


title


# In[129]:


author


# In[130]:


price


# In[131]:


total = 0

# := "assignment expression"
# "walrus"
# starting with Python 3.8

while s := input('Enter book title: ').strip():
    
    for title, author, price in all_books:
        if title == s:
            print(f'Found {s} by {author}, price {price}')
            total += price
            break
            
    else:    # got_to_end_of_loop_without_encountering_a_break
        print(f'Did not find {s}')
            
print(f'Total is {total}')


# In[132]:


mylist = [10, 20, 30, 40, 50, 60]

x,y,z = mylist


# In[133]:


x, *y, z = mylist


# In[134]:


x


# In[135]:


z


# In[136]:


y


# In[137]:


x,y,*z = mylist


# In[138]:


z


# In[139]:


x


# In[140]:


y


# In[141]:


d = {'a':1, 'b':2, 'c':3}


# In[142]:


# keys must be immutable -- typically, int, float, or string
# values can be anything at all


# In[143]:


globals()


# In[144]:


d['a']


# In[145]:


d['b']


# In[146]:


d['c']


# In[147]:


k = 'b'
d[k]


# In[148]:


'b' in d


# In[149]:


3 in d


# In[151]:


k = 'b'
if k in d:
    print(d[k])
else:
    print(f'{k} is not a key in d')


# In[152]:


k = 'v'
if k in d:
    print(d[k])
else:
    print(f'{k} is not a key in d')


# In[ ]:


d.get('b')   # if 'b' in d, we get d['b']


# In[154]:


d.get('v')   # if 'b' in d, we get d['b']... otherwise None


# In[155]:


print(d.get('v'))


# In[156]:


d.get('v', 'No such key in d')


# # Exercise: Travel 
# 
# 1. Start with an empty dictionary, `all_places`.
# 2. Ask the user, repeatedly, to give us a city + country in the form `city, country`
# 3. If we got an empty string, we stop asking.
# 4. If we got a string without `,`, scold the user and try again.
# 5. Otherwise, take the city and country, and add to the dict:
#     - The countries will be keys (as string)
#     - The cities will be in a list.
# 6. At the end, print all countries, and then all cities within those countries.
# 
# Example:
# 
#     Where have you gone: New York, USA
#     Where have you gone: Chicago, USA
#     Where have you gone: Beijing, China
#     Where have you gone: Shanghai, China
#     Where have you gone: [ENTER]
#     
# Our data structure:
# 
#     {'USA': ['New York', 'Chicago'], 'China': ['Beijing', 'Shanghai'}    
#     
# USA
#     New York
#     Chicago
# China
#     Beijing
#     Shanghai
#     

# In[159]:


all_places = {}

while s := input('Enter place: ').strip():

    if ',' not in s:
        print(f'Enter "city, country"')
        continue
        
    city, country = s.split(',')
    city = city.strip()
    country = country.strip()
    
#     if country not in all_places:
#         all_places[country.strip()] = []
        
    all_places.setdefault(country, [])
    
    if city in all_places[country]:
        print(f'We already got {city}!')
        continue
        
    all_places[country].append(city)
    
for country, all_cities in all_places.items():
    print(country)
    
    for one_city in all_cities:
        print(f'\t{one_city}')


# In[158]:


all_places


# In[ ]:




