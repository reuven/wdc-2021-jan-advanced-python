#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# - How do dicts work?
# - Variations on dicts
#     - `set`
#     - `defaultdict`
#     - `OrderedDict`
#     - `Counter`
# - Functions
#     - Parameters (positional + keyword)
#     - Function object 
#     - Bytecodes

# https://github.com/reuven/wdc-2021-jan-advanced-python

# In[3]:


d = {}


# In[4]:


d['a'] = 1


# In[5]:


hash('a') % 8 


# In[6]:


hash('b') % 8

   index          key          value
     0           
     1
     2
     3             'b'          3
     4
     5
     6             'a'           1
     7
     
     
     
# In[ ]:





# In[ ]:


'a' in d


# In[7]:


d = {}
d['a'] = 100


# In[8]:


hash('a') % 8

index       key          value
   0         'a'              100
   1         'b'              200 
   2         'c'              300
   3         'd'              400

[None, 2, None, 1, 3, None, 0, None]
# In[9]:


d['a']   # (1) hash('a') % 8  -->   (2) table[0]


# In[10]:


d['b'] = 200


# In[11]:


hash('b') % 8


# In[12]:


hash('c') % 8


# In[13]:


d['c'] = 300


# In[14]:


'a' in d


# In[15]:


hash('d') % 8


# In[16]:


d['d'] = 400


# In[17]:


'd' in d


# In[18]:


d.keys()


# In[19]:


for key in d:
    print(key)


# In[20]:


mylist = [10, 20, 30]

d[mylist] = 500


# In[21]:


id('abcd')


# In[22]:


id('efgh')


# In[23]:


id('ijkl')


# In[24]:


# set


# In[25]:


s = {1,2,3,4,5}   #  this is a set! 
type(s)


# In[26]:


s = {}   # empty dict, *NOT* empty set
type(s)


# In[27]:


s = set()  # use the name
s.add(1)
s.add(2)
s.add(3)

s


# In[28]:


2 in s


# In[29]:


100 in s


# In[30]:


s.add(4)
s.add(4)


# In[31]:


s


# In[32]:


s.remove(3)
s


# In[34]:


s = set('abcdef')
s


# In[35]:


for one_item in s:
    print(one_item)


# In[37]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}

s1 | s2     # union


# In[39]:


s1 & s2      # intersection


# In[40]:


s1 ^ s2   # xor


# In[42]:


for one_item in s:
    print(f'{one_item}: {hash(one_item) % 16}')


# In[43]:


s = set()
for one_letter in 'abcdef':
    s.add(one_letter)
    
for one_item in s:
    print(f'{one_item}: {hash(one_item) % 8}, {hash(one_item) % 16} ')


# # Exercise: dictdiff
# 
# ```python
# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4}
# d3 = {'a':1, 'b':5, 'x':100}
# 
# 
# dictdiff(d1, d2) #  {'c':[3, 4]}
# dictdiff(d2, d1) #  {'c':[4, 3]}
# 
# dictdiff(d1, d3) # {'b':[2, 5], 'c':[3, None], 'x':[None, 100]}
# ```
# 
# 1. Write a function, `dictdiff`, that takes two arguments, both dicts.
# 2. The output will be a dict describing the differences between the two.
# 3. If a key-value pair is the same in both dicts, ignore it in the output.
# 4. Where there is a difference, the value will be a two-element list, with the first and second values.  
# 5. If the key doesn't exist in one of the dicts, then it should be `None` in the list.

# In[51]:


def dictdiff(first, second):
    output = {}
    
    for one_key in first.keys() | second.keys():
        v1 = first.get(one_key)
        v2 = second.get(one_key)
        
        if v1 != v2:
            output[one_key] = [v1, v2]
    
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':5, 'x':100}


print(dictdiff(d1, d1))
print(dictdiff(d1, d2)) #  {'c':[3, 4]}
print(dictdiff(d2, d1)) #  {'c':[4, 3]}

print(dictdiff(d1, d3)) # {'b':[2, 5], 'c':[3, None], 'x':[None, 100]}


# In[47]:


d.keys()


# In[50]:


d.keys() | d.keys()


# In[52]:


# defaultdict

from collections import defaultdict


# In[53]:


d = {'a':1, 'b':2, 'b':3}

d['d']


# In[54]:


d = defaultdict(0)


# In[56]:


class Foo:
    def __init__(self, x):
        self.x = x
        
Foo(10)          


# In[57]:


callable(Foo)


# In[58]:


callable(int)


# In[59]:


callable(callable)


# In[60]:


int() 


# In[61]:


d = defaultdict(int)


# In[62]:


d['a'] = 100


# In[63]:


d['b'] = 200


# In[64]:


d


# In[65]:


d['c']


# In[66]:


d


# In[67]:


d['x'] += 100   # d['x'] = d['x'] + 100


# In[68]:


d


# In[69]:


d = defaultdict(dict)


# In[70]:


d['a']['b'] = 100
d['x']['y'] = 200
d['a']['z'] = 300

d


# In[71]:


d = defaultdict(list)

while True:
    s = input('Enter city, country: ').strip()
    
    if not s:
        break
        
    city, country = s.split(',')
    
    d[country.strip()].append(city.strip())


# In[72]:


d


# In[ ]:


d = {}

while True:
    s = input('Enter city, country: ').strip()
    
    if not s:
        break
        
    city, country = s.split(',')
    
    if country.strip() not in d:
        d[country.strip()] = []
    
    d[country.strip()].append(city.strip())


# In[73]:


import time
time.time()


# In[74]:


d = defaultdict(time.time)


# In[75]:


d['a']


# In[76]:


d['b']


# In[77]:


d['c']


# In[78]:


'd' in d


# In[79]:


'd' in d


# # Exercise: Character count
# 
# ```
# Enter a string: abcd
# Enter a string: cdef
# Enter a string: cd!!
# Enter a string: [ENTER]
# 
# 'a': 1
# 'b': 1
# 'c': 3
# 'd': 3
# 'e': 1
# 'f': 1
# '!': 2
# ```
# 
# 1. Write a program that asks the user to enter strings, one at a time.
# 2. When the user presses ENTER, stop asking.
# 3. For each string, count the number of times each character appears, and store that count in a `defaultdict`.
# 4. When the user is done entering input, print how many times each letter appeared.

# In[83]:


from collections import defaultdict
counts = defaultdict(int)

while s := input('Enter a string: ').strip():
    for one_character in s:
        counts[one_character] += 1 
        
for key, value in counts.items():
    print(f'{key}: {value}')


# In[82]:


counts


# In[84]:


# whitespace == space, \n, \t, \r, \v (vertical tab)

s = '    a     b      c     '
s.strip()


# In[85]:


s = 'abcabcabc'

s.strip('a')


# In[86]:


s.strip('ab')


# In[87]:


s.strip('abc')


# In[88]:


filename = 'excel.exe'
filename.strip('exe')


# In[89]:


# starting in 3.9, we have

filename.removesuffix('.exe')


# In[ ]:


filename = 'excel.exe'
filename.strip('ex')  #  'cel.'


# In[90]:


from collections import OrderedDict


# In[91]:


od = OrderedDict()

od['a'] = 100
od['b'] = 200
od['c'] = 300

od.keys()


# In[92]:


od.pop('b')  


# In[93]:


od.keys()


# In[94]:


od['b'] = 400
od.keys()


# In[95]:


d = {'a':100, 'b':200, 'c':300}

new_stuff = {'c':444, 'd':555, 'e':666}

d.update(new_stuff)
d


# In[96]:


d = {'a':100, 'b':200, 'c':300}

new_stuff = {'c':444, 'd':555, 'e':666}

d | new_stuff


# In[97]:


d


# In[98]:


d |= new_stuff   # d.update(new_stuff)


# In[99]:


from collections import Counter

c = Counter()


# In[100]:


c['a'] += 5
c['b'] += 10
c['c'] += 2
c['b'] += 3

c


# In[101]:


c = Counter('abcabcccccbbccc')


# In[102]:


c


# In[103]:


c + c


# In[104]:


counts = Counter()

while s := input('Enter a string: ').strip():
    counts += Counter(s)
        
for key, value in counts.items():
    print(f'{key}: {value}')


# In[105]:


counts.most_common()


# In[106]:


counts.most_common(3)


# In[107]:


def hello(name):
    return f'Hello, {name}!'


# In[108]:


type(hello)


# In[109]:


hello = 7


# In[110]:


hello('world')


# In[111]:


def hello(name):
    return f'Hello, {name}!'


# In[112]:


hello('world')


# In[113]:


hello()


# # Argument types
# 
# - Positional arguments
# - Keyword arguments

# In[114]:


def hello(name):
    return f'Hello, {name}!'


# In[115]:


hello('world')  # positional argument


# In[116]:


hello(name='world')  # keyword argument


# In[117]:


def add(x, y):
    return x + y


# In[118]:


add(10, 5)  # two positionals


# In[119]:


add(x=10, y=5)  # two keywords


# In[120]:


add(10, y=5)  # one positional, one keyword


# In[121]:


add(x=10, 5)


# In[122]:


def hello(name):
    return f'Hello, {name}!'


# In[123]:


hello.__code__.co_argcount


# In[124]:


hello.__code__.co_varnames


# In[125]:


def add(x, y):
    return x + y


# In[126]:


add()


# In[127]:


add.__code__.co_argcount


# In[128]:


add.__code__.co_varnames


# In[129]:


def add(x, y):
    z = x + y
    return z


# In[130]:


add.__code__.co_argcount


# In[131]:


add.__code__.co_varnames


# In[132]:


def add(x, y=2):
    z = x + y
    return z


# In[133]:


add.__code__.co_argcount


# In[135]:


add.__code__.co_varnames


# In[136]:


add(3, 2)


# In[137]:


add(3)


# In[138]:


add.__defaults__


# In[139]:


add(5, 3)


# In[140]:


add(5)


# In[141]:


def add(x=3, y=2):
    z = x + y
    return z


# In[142]:


add.__defaults__


# In[143]:


add()


# In[144]:


add(10)


# In[145]:


add(y=10)  # keyword


# In[146]:


def hello(name):
    return f'Hello, {name}!'


# In[147]:


hello('world')


# In[148]:


hello([10, 20, 30])


# In[149]:


hello(hello)


# In[150]:


def hello(name):
    if type(name) is str:
        return f'Hello, {name}!'
    else:
        raise TypeError('I wanted a string')


# In[151]:


hello('world')


# In[152]:


hello([10, 20, 30])


# In[ ]:


# duck typing 


# In[153]:


def hello(name):
    return f'Hello, {name}!'


# In[154]:


# type annotations

def hello(name:str):
    return f'Hello, {name}!'


# In[155]:


hello.__annotations__


# In[156]:


hello('world')


# In[157]:


hello(123)


# In[158]:


def foo(x=1, y):
    return x + y


# In[159]:


def foo(a, b, c, d=1, e=2, f=3):
    return a+b+c+d+e+f


# In[160]:


foo(10, 20, 30)


# In[161]:


foo.__code__.co_argcount


# In[162]:


foo.__defaults__


# In[163]:


def add_one(x=[]):
    x.append(1)
    print(f'{x=}')
    
mylist = [10, 20, 30]
add_one(mylist)


# In[164]:


mylist


# In[165]:


add_one(mylist)


# In[166]:


mylist


# In[167]:


add_one() 


# In[168]:


add_one.__defaults__


# In[169]:


add_one()


# In[170]:


add_one()


# # Exercise: `firstlast`
# 
# 1. Write a function, `firstlast`, that accepts one sequence (string, list, tuple)
# 2. The function should return the same type as it got, but with only two elements, the first and last.
# 
# ```python
# firstlast('abcde')               # 'ae'
# firstlast([10, 20, 30])          # [10, 30]
# firstlast((100, 200, 300, 400))  # (100, 400)
# ```

# In[171]:


def firstlast(s):
    return s[0] + s[-1]


# In[172]:


print(firstlast('abcde'))               # 'ae'
print(firstlast([10, 20, 30]))          # [10, 30]
print(firstlast((100, 200, 300, 400)))  # (100, 400)


# In[174]:


def firstlast(s):
    return s[:1] + s[-1:]

print(firstlast('abcde'))               # 'ae'
print(firstlast([10, 20, 30]))          # [10, 30]
print(firstlast((100, 200, 300, 400)))  # (100, 400)


# In[176]:


def firstlast(s):
    return s[::len(s)-1]

print(firstlast('abcde'))               # 'ae'
print(firstlast([10, 20, 30]))          # [10, 30]
print(firstlast((100, 200, 300, 400)))  # (100, 400)


# # Python has 4 scopes:
# 
# - `L` Local — if I'm in a function body
# - `E` Enclosing — if I'm in a function body
# - `G` Global
# - `B` Builtin

# In[178]:


# scoping 

x = 100

print(f'{x=}')  # is x global?


# In[179]:


'x' in globals()


# In[180]:


# scoping 

x = 100

def myfunc():
    print(f'In myfunc, {x=}')

print(f'Before, {x=}') # is x global? True
myfunc()
print(f'After, {x=}')


# In[181]:


'x' in myfunc.__code__.co_varnames


# In[184]:


x = 100

def myfunc():
    x = 200
    print(f'In myfunc, {x=}')  # is x local? True

print(f'Before, {x=}') # is x global? True
myfunc()
print(f'After, {x=}')


# In[183]:


'x' in myfunc.__code__.co_varnames


# In[185]:


x = 100

def hello():
    print('Hello from the "hello" function!')

def myfunc():
    x = 200
    hello()
    print(f'In myfunc, {x=}')  # is x local? True

print(f'Before, {x=}') # is x global? True
myfunc()
print(f'After, {x=}')


# In[186]:


x = 100

def myfunc():
    print(f'In myfunc, {x=}')  
    x = 200

print(f'Before, {x=}') 
myfunc()
print(f'After, {x=}')


# In[187]:



def myfunc():
    print(f'In myfunc, {x=}')  
    x = 200


# In[188]:


myfunc.__code__.co_varnames


# In[189]:


x = 100

def myfunc(x):
    x += 1  
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}') 
myfunc()
print(f'After, {x=}')


# In[ ]:


x = 100

def myfunc():
    global x
    x = 200
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}') 
myfunc()
print(f'After, {x=}')


# In[192]:


def myfunc():
    global x
    x = 200
    print(f'In myfunc, {x=}')  

myfunc.__code__.co_varnames    


# In[193]:


x = 100

def myfunc():
    global x
    x = 200
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}') 
myfunc()
print(f'After, {x=}')


# In[194]:


import __main__

x = 100

def myfunc():
    __main__.x = 200   
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}') 
myfunc()
print(f'After, {x=}')


# In[195]:


sum = 0
sum += 10
sum += 15
sum


# In[196]:


sum([10, 20,30])


# In[197]:


dir(__builtin__)


# In[198]:


del(sum) 


# In[199]:


sum([10,20, 30])


# # Next time
# 
# - `*args`
# - `**kwargs`
# - positional-only, keyword-only parameters
# - Enclosing scope
# - Comprehensions

# In[ ]:




