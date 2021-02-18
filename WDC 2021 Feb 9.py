#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. `*args`
# 2. `**kwargs`
# 3. keyword only parameters
# 4. positional parameters
# 5. Enclosing scope -- nested functions
# 6. Comprehensions

# In[1]:


sum([10, 20, 30])


# In[2]:


def mysum(numbers):
    print(f'{numbers=}')
    total = 0
    for one_number in numbers:
        total += one_number
    return total

mysum([10, 20, 30])


# In[3]:


mysum((10, 20, 30))


# In[4]:


mysum({1:'a', 2:'b', 3:'c'})


# In[5]:


mysum(10, 20, 30)


# In[7]:


# *args

def mysum(*numbers):
    print(f'{numbers=}')
    total = 0
    for one_number in numbers:
        total += one_number
    return total

mysum(10, 20, 30)


# In[8]:


mysum.__code__.co_argcount


# In[9]:


mysum.__code__.co_varnames


# In[10]:


mysum.__code__.co_flags


# In[11]:


bin(mysum.__code__.co_flags)


# In[12]:


# *args

def mysum(numbers):
    print(f'{numbers=}')
    total = 0
    for one_number in numbers:
        total += one_number
    return total


# In[13]:


bin(mysum.__code__.co_flags)


# In[14]:


import dis


# In[15]:


dis.show_code(mysum)


# In[16]:


def mysum(*numbers):
    print(f'{numbers=}')
    total = 0
    for one_number in numbers:
        total += one_number
    return total


# In[17]:


dis.show_code(mysum)


# In[18]:


mylist = [10, 20, 30]

mysum(mylist)


# In[19]:


mysum(*mylist)


# In[20]:


def add(a, b):
    return a + b

t = (10, 3)
add(t)


# In[21]:


add(*t)


# In[22]:


x, *y, z = [10, 20, 30, 40, 50]
y


# In[24]:


def foo(a, b, *args):
    return f'{a=}, {b=}, {args=}'


# In[25]:


foo(10, 20, 30, 40, 50)


# In[26]:


foo.__code__.co_argcount


# In[27]:


def foo(a, b=999, *args):
    return f'{a=}, {b=}, {args=}'


# In[28]:


foo(10, 20, 30, 40, 50)


# In[29]:


foo(10, args=(30, 40, 50))


# In[30]:


# keyword-only arguments
# b is now keyword only, with a default!
# if I want to give it a value, I have to say b=VALUE

def foo(a, *args, b=999):
    return f'{a=}, {b=}, {args=}'

foo(10, 20, 30, 40, 50)


# In[31]:


foo(10, 20, 30, 40, 50, b=60)


# In[33]:


get_ipython().system('ls *.txt')


# In[39]:


def find_in_file(filename, *args):
    for one_line in open(filename):
        for one_string in args:
            if one_string in one_line:
                print(f'{one_string}: {one_line}', end='')
            
find_in_file('linux-etc-passwd.txt', 'x', 'y')


# # Types of parameters
# 
# 1. Mandatory (positional, no default)
# 2. Optional (positional, with default)
# 3. `*args` (positional, gets all remaining ones)
# 4. Keyword-only (optionally has a default)

# In[41]:


def find_in_file(filename, *args, only_first=False):
    for one_line in open(filename):
        for one_string in args:
            if one_string in one_line:
                print(f'{one_string}: {one_line}', end='')
                if only_first:
                    break
            
find_in_file('linux-etc-passwd.txt', 'x', 'y', only_first=True)


# # Exercise: all_lines
# 
# 1. Write a function, `all_lines`, that takes:
#     - Mandatory argument `outfilename`, into which data will be written
#     - Any number of arguments `infilenames`, names of files from which we'll read
#     - Optional argument `sep`, defaults to `\n`
# 2. After running the function, all content from each file in `infilenames` will be written to `outfilename`, separated from one another with `sep`.

# In[42]:


# all_lines('outfile.txt', 'infile1.txt', 'infile2.txt', 'infile3.txt', sep='------\n')


# In[43]:


def all_lines(outfilename, *infilenames, sep='\n'):
    with open(outfilename, 'w') as outfile:
        for one_filename in infilenames:
            for one_line in open(one_filename):
                outfile.write(one_line)
            outfile.write(sep)


# In[44]:


for i in range(5):
    with open(f'infile{i}.txt', 'w') as outfile:
        for one_word in 'abcd efgh ijkl mnop'.split():
            outfile.write(f'{i} {one_word}\n')
        


# In[45]:


get_ipython().system('ls infile*')


# In[46]:


import glob


# In[47]:


glob.glob('infile*')


# In[49]:


all_lines('outfile.txt', *glob.glob('infile*'))


# In[50]:


get_ipython().system('cat outfile.txt')


# In[51]:


all_lines('outfile.txt', *glob.glob('infile*'), sep='****\n')


# In[52]:


get_ipython().system('cat outfile.txt')


# In[53]:


def all_lines(outfilename, *infilenames, sep='\n'):
    with open(outfilename, 'w') as outfile:
        for one_filename in infilenames:
            for one_line in open(one_filename):
                outfile.write(one_line)
            outfile.write(sep)


# In[54]:


dis.show_code(all_lines)


# In[55]:


def add(a, b):
    return a + b


# In[56]:


add(5, b=3)


# In[57]:


add(a=5, 3)


# # `**kwargs`
# 
# `kwargs` will be a dict!
# 
# - Gets all of the leftover keyword arguments
# - Keys will be strings (left side of the key=value)
# - Values will be whatever we pass

# In[58]:


def myfunc(a, b, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[64]:


myfunc(10, 20, x=100, y=200, z=300)


# In[65]:


def write_config(filename, **kwargs):
    with open(filename, 'w') as outfile:
        for key, value in kwargs.items():
            outfile.write(f'{key}={value}\n')


# In[67]:


write_config('config.txt', a=1, b=2, c=3)


# In[68]:


get_ipython().system('cat config.txt')


# In[69]:


def write_config(filename, sep='=', **kwargs):
    with open(filename, 'w') as outfile:
        for key, value in kwargs.items():
            outfile.write(f'{key}{sep}{value}\n')


# In[70]:


write_config('config.txt', a=1, b=2, c=3)


# In[71]:


write_config('config.txt', a=1, b=2, c=3, sep='****')


# In[72]:


get_ipython().system('cat config.txt')


# In[73]:


def myfunc(a, b, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[74]:


myfunc(10, 20, a=100, b=200)


# In[75]:


def write_config(filename, sep='=', **kwargs):
    with open(filename, 'w') as outfile:
        for key, value in kwargs.items():
            outfile.write(f'{key}{sep}{value}\n')


# In[76]:


my_config = {'a':100, 'b':[10,20, 30], 'c':'hello'}


# In[77]:


write_config('config.txt', my_config)


# In[78]:


get_ipython().system('cat config.txt')


# In[79]:


# turn a dict into keyword arguments with ** during invocation

write_config('config.txt', **my_config)


# In[80]:


get_ipython().system('cat config.txt')


# # Exercise: XML generator
# 
# ```python
# print(xml('foo'))               # first argument = tagname
# # <foo></foo>
# 
# print(xml('foo', 'bar'))        # second (optional) argument = content
# # # # # <foo>bar</foo>
# 
# print(xml('a',
#           xml('b',
#               xml('c', 'hello'))))
# # # # # # # <a><b><c>hello</c></b></a>
# 
# # # # kwargs become attributes in opening tag
# 
# print(xml('tag', 'text', a=1, b=2, c=3))
# 
# # # # # <tag a="1" b="2" c="3">text</tag>
# 
# print(xml('tag', 'text', a=1, b=2))
# # # # # <tag a="1" b="2">text</tag>
# 
# print(xml('tag', a=1, b=2))
# # # # # # <tag a="1" b="2"></tag>
# ```
<address>
    <country>Israel</country>
    <city region="center">Modi'in</city>
</address>
# In[91]:


def xml(tagname, text='', **kwargs):
    attributes = ''
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'
    return f'<{tagname}{attributes}>{text}</{tagname}>'

print(xml('foo'))
print(xml('foo', 'bar'))

print(xml('a',
          xml('b',
              xml('c', 'hello'))))


print(xml('tag', 'text', a=1, b=2, c=3))
print(xml('tag', 'text', a=1, b=2))
print(xml('tag', a=1, b=2))


# In[92]:


def foo(a, b=10, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[93]:


foo(2,4)


# In[94]:


foo(2,4, x=100, y=200)


# In[95]:


foo(2, b=4, x=100, y=200)


# In[97]:


def foo(a, *, b=10, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[98]:


foo(2)


# In[99]:


foo(2,4)


# In[100]:


def add(*, a, b):
    return a + b

add(10, 5)


# In[101]:


add(a=10, b=5)


# In[102]:


len('abcd')


# In[103]:


help(len)


# In[104]:


len(obj='abcd')


# In[105]:


def add(a, b, /):
    return a + b

add(10, 3)


# In[106]:


add(a=10, b=3)


# # Parameter types:
# 
# 1. Positional-only (before `/`, just 3)
# 2. Positional (mandatory)
# 3. Positional (optional)
# 4. `*args`  (or `*`, if we want keyword args after here, just 3)
# 5. Keyword-only (with or without default, just 3)
# 6. `**kwargs`

# # Scopes:
# 
# - `L` Local
# - `E` Enclosing
# - `G` Global
# - `B` Builtin

# In[107]:


for i in range(5):
    print(i, end=' ')


# In[108]:


i


# In[109]:


def outer():
    def inner():
        print('I am in inner!')
    return inner

f = outer()


# In[110]:


type(f)


# In[111]:


f()


# In[118]:


def outer(x):
    def inner(y):
        print(f'I am in inner, {x=}, {y=}')
    return inner


# In[114]:


f = outer(10)


# In[117]:


f(20)


# In[119]:


f1 = outer(10)
f2 = outer(20)
f3 = outer(30)


# In[120]:


f1(6)


# In[121]:


f2(6)


# In[122]:


f3(6)


# In[123]:


outer.__code__.co_cellvars


# In[124]:


f1.__code__.co_freevars


# In[125]:


def mulby(x):
    def calculate(y):
        return x * y
    return calculate

m10 = mulby(10)
m20 = mulby(20)


# In[126]:


m10(5)


# In[127]:


m10(2)


# In[128]:


m10('abc')


# In[129]:


m20(2)


# In[130]:


# closure


# In[134]:


hello_counter = 0

def hello(name):
    global hello_counter
    hello_counter += 1
    return f'{hello_counter} Hello, {name}!'


# In[135]:


hello('world')


# In[136]:


hello('world again')


# In[137]:


del(hello_counter)


# In[144]:


def counter():
    hello_counter = 0
    def hello(name):
        nonlocal hello_counter   
        hello_counter += 1
        return f'{hello_counter} Hello, {name}!'
    return hello


# In[145]:


f = counter()


# In[148]:


for i in range(5):
    print(f('world'))


# In[149]:


for i in range(5):
    print(f('world'))


# # Exercise: Password generator generator
# 
# 1. Define `make_password_generator`, which takes a single argument, a string, `s`.
# 2. This function should return a function, which takes a single argument, an integer, `n`.
# 3. When called, this function will return a string of length `n`, with characters taken randomly from `s`.
# 
# ```python
# make_letter_pw = make_password_generator('abcde')
# print(make_letter_pw(5))   # bccea
# print(make_letter_pw(5))   # cabae
# 
# make_symbol_pw = make_password_generator('!@#$%')
# print(make_symbol_pw(5))   # @#$@!
# print(make_symbol_pw(5))   # $#^#$
# ```
# Hint: `random.choice` returns a random element of a sequence.
# 
# 

# In[1]:


import random

def make_password_generator(s):
    def make_password(n):
        output = ''
        for i in range(n):
            output += random.choice(s)
        return output
    return make_password
            


# In[2]:


make_letter_pw = make_password_generator('abcde')
print(make_letter_pw(5))   # bccea
print(make_letter_pw(5))   # cabae

make_symbol_pw = make_password_generator('!@#$%')
print(make_symbol_pw(5))   # @#$@!
print(make_symbol_pw(5))   # $#^#$


# In[3]:


import random

def make_password_generator(s):
    remaining_uses = 5
    def make_password(n):
        nonlocal remaining_uses
        if remaining_uses <= 0:
            raise ValueError('Too many uses of this password string')
            
        remaining_uses -= 1
        output = ''
        for i in range(n):
            output += random.choice(s)
        return output
    return make_password
            


# In[4]:


make_letter_pw = make_password_generator('abcde')

for i in range(10):
    print(make_letter_pw(7))


# In[5]:


def a():
    return "I'm in A!"

def b():
    return "I'm in B!"

while True:
    s = input('Enter a function name: ').strip()
    
    if not s:
        break
        
    if s == 'a':
        print(a())
        
    elif s == 'b':
        print(b())
        
    else:
        print(f'No function {s}')
    


# In[6]:


def a():
    return "I'm in A!"

def b():
    return "I'm in B!"

# dispatch table
funcs = {'a':a,
         'b':b}

while True:
    s = input('Enter a function name: ').strip()
    
    if not s:
        break
        
    if s in funcs:
        print(funcs[s]())

    else:
        print(f'No function {s}')  


# # Exercise: Prefix notation calculator
# 
# 1. We'll write a function that asks the user to enter a math expression with prefix notation (e.g., `+ 2 2`), and prints the answer.
# 2. When the user gives us an empty string, we stop asking.
# 3. You should support `+` and `-` (you can do others, too, if you want).
# 4. Use a dispatch table to choose the functions, based on the operator.
# 
# Example:
# 
#     Expression: + 2 2
#     4
#     Expression: - 10 5
#     5
#     Expression: @ 10 5
#     @ not known
#     

# In[7]:


def add(a, b):
    return int(a) + int(b)

def sub(a, b):
    return int(a) - int(b)

ops = {'+':add,
       '-':sub}

while True:
    s = input('Expression: ').strip()
    
    if not s:
        break
        
    op, *numbers = s.split()
    
    if op in ops:
        print(ops[op](*numbers))
    
    else:
        print(f'Operator {op} is not known')


# In[8]:


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

ops = {'+':add,
       '-':sub}

while True:
    s = input('Expression: ').strip()
    
    if not s:
        break
        
    op, *numbers = s.split()
    
    numbers = [int(one_number)
              for one_number in numbers]
    
    if op in ops:
        print(ops[op](*numbers))
    
    else:
        print(f'Operator {op} is not known')


# In[10]:


import operator

ops = {'+':operator.add,
       '-':operator.sub,
      '*':operator.mul,
      '/':operator.truediv}

while True:
    s = input('Expression: ').strip()
    
    if not s:
        break
        
    op, *numbers = s.split()
    
    numbers = [int(one_number)
              for one_number in numbers]
    
    if op in ops:
        print(ops[op](*numbers))
    
    else:
        print(f'Operator {op} is not known')


# In[11]:


s1 = 'abcde'
s2 = 'fghij'

def i3(data):
    return data[3]

def i2(data):
    return data[2]

i3(s1)


# In[12]:


i2(s2)


# In[13]:


def get_index(i):
    def inner(data):
        return data[i]
    return inner


# In[14]:


i3 = get_index(3)
i2 = get_index(2)


# In[15]:



i3(s1)


# In[17]:


i2(s2)


# In[18]:


i3 = operator.itemgetter(3)
i2 = operator.itemgetter(2)


# In[19]:


i3(s1)


# In[20]:


i2(s2)


# In[21]:


i234 = operator.itemgetter(2,3,4)

i234(s1)


# # Next time:
# 
# 
# - Comprehensions!
#     - List comprehensions
#     - Set comprehensions
#     - Dict comprehensions
#     - Nested comprehensions
# - Sorting 
# - `lambda`
# 

# In[ ]:




