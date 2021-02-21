#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. List comprehensions
# 2. Dict comprehensions
# 3. Set comprehensions
# 4. Nested comprehensions
# 4. `lambda`

# In[1]:


numbers = list(range(10))

numbers


# In[2]:


output = []

for one_number in numbers:
    output.append(one_number ** 2)
    
output


# In[3]:


# list comprehensions

[one_number ** 2              # expression  -- SELECT
 for one_number in numbers]   # iteration   -- FROM 


# In[4]:


mylist = ['abcd', 'efgh', 'ijkl']

'*'.join(mylist)


# In[5]:


'___'.join(mylist)


# In[6]:


mylist = [10, 20, 30]

'*'.join(mylist)


# In[8]:


[str(one_item)
 for one_item in mylist]


# In[9]:


'*'.join([str(one_item)
          for one_item in mylist])


# In[12]:


s = 'abcd'

[f'{index}: {one_item}'
 for index, one_item in enumerate(s)]


# In[13]:


d = {'a':1, 'b':2, 'c':3}

[f'{key}: {value}'
for key, value in d.items()]


# In[14]:


[key * value
for key, value in d.items()]


# # Exercises: Comprehensions
# 
# 1. Ask the user to enter a string with integers separated by spaces. (Example: `'10 20 30'`) Use a list comprehension to take this string and sum the numbers. You may use `sum` to calculate this.
# 2. Ask the user to enter a string. Use a list comprehension and `str.capitalize` to get the same result as you would from `str.title`.

# In[16]:


s = 'this is a test'

s.capitalize()  # returns a string -- all lowercase, except the first 


# In[17]:


s.title()  # returns a string -- all lowercase, except the first letter in each word


# In[20]:


s = input('Enter numbers: ')

sum([int(one_item)
 for one_item in s.split()])


# In[25]:


s = input('Enter a sentence: ')

' '.join([one_word.capitalize()
          for one_word in s.split()])


# In[29]:


[one_line.split(':')[0]                 # expression -- SELECT
 for one_line in open('/etc/passwd')    # iteration -- FROM
 if not one_lpeine.startswith("#")]     # condition -- WHERE


# In[30]:


get_ipython().system('ls *.txt')


# In[31]:


get_ipython().system('cat nums.txt')


# # Exercise: `nums.txt`
# 
# Read from `nums.txt`, and sum the numbers that are there using a comprehension.

# In[42]:


sum([int(one_line)
for one_line in open('nums.txt')
if one_line.strip().isdigit() ])


# In[35]:


int('1')


# In[36]:


int('   1    ')


# In[38]:


int('   ')


# In[44]:


s = '123'
s.isdigit()


# In[45]:


s = '一二三'
s.isdigit()


# In[46]:


s.isnumeric()


# In[47]:


get_ipython().system('head shoe-data.txt')


# # Exercise: Shoe dicts
# 
# 1. Read from `shoe-data.txt` with a list comprehension
# 2. Turn each row (separated by `'\t'` characters) into a dict.
# 3. Each dict should look like this: `{'brand':'Adidas', 'color':'orange', 'size':'43'}`
# 4. I suggest that you write a function (`line_to_dict`) that will be called by the comprehension once for each line in the file, and which returns a dict of the form we want.

# In[50]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

[line_to_dict(one_line)
 for one_line in open('shoe-data.txt')]


# In[54]:


def line_to_dict(one_line):
    return dict(zip(['brand', 'color', 'size'],
                    one_line.strip().split('\t')))

[line_to_dict(one_line)
 for one_line in open('shoe-data.txt')]


# In[53]:


dict(zip('abc', [10, 20, 30]))


# In[58]:


# list of lists with a comprehension
[[one_line.split(':')[0], one_line.split(':')[2]]
for one_line in open('/etc/passwd')
if not one_line.startswith('#')]


# In[59]:


# get a dict from our list of lists with a comprehension
dict([[one_line.split(':')[0], one_line.split(':')[2]]
for one_line in open('/etc/passwd')
if not one_line.startswith('#')])


# In[62]:


# dict comprehension 

#     key                         value
{ one_line.split(':')[0] :  one_line.split(':')[2]
for one_line in open('/etc/passwd')
if not one_line.startswith('#') }


# In[63]:


get_ipython().system('ls *.txt')


# # Exercise: Words and lengths
# 
# 1. Ask the user to enter a sentence.
# 2. Use a dict comprehension to turn the input into a dict, where the words are keys and the values are the lengths of the words.

# In[65]:


s = input('Enter a sentence: ')


# In[66]:


s


# In[67]:


s.split()


# In[69]:


{one_word : len(one_word)
 for one_word in s.split()}


# In[72]:


s = input('Enter numbers: ')

sum([int(one_number)
 for one_number in s.split()])


# In[73]:


s = input('Enter numbers: ')

sum([int(one_number)
 for one_number in s.split()])


# In[74]:


s = input('Enter numbers: ')

sum(set([int(one_number)
 for one_number in s.split()]))


# In[75]:


s = input('Enter numbers: ')

sum({int(one_number)
 for one_number in s.split()})


# In[76]:


# set comprehension
{ x**2
 for x in range(-5, 5)
    
}


# In[77]:


# list comprehension
[ x**2
 for x in range(-5, 5)
    
]


# In[78]:


# dict comprehension
{ x: x**2
 for x in range(-5, 5)
    
}


# In[79]:


get_ipython().system('cat linux-etc-passwd.txt')


# # Exercise: Different shells
# 
# 1. Use a set comprehension to read from `linux-etc-passwd.txt`.
# 2. Ignore lines that start with `#` or are empty.
# 3. The returned set should contain all of the different shells on the system. The shell is the *final* field in each record.

# In[82]:


[one_line
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith('#') and one_line.strip()]


# In[86]:


{one_line.split(':')[-1].strip()
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith(('#', '\n'))}


# In[87]:


get_ipython().system('head mini-access-log.txt')


# In[88]:


# what IP addresses are in mini-access-log.txt?

[one_line.split()[0]
for one_line in open('mini-access-log.txt')]


# In[89]:


# what DIFFERENT IP addresses are in mini-access-log.txt?

{one_line.split()[0]
for one_line in open('mini-access-log.txt')}


# In[91]:


# how many times does each IP address appear in the logfile?

from collections import Counter

c = Counter([one_line.split()[0]
        for one_line in open('mini-access-log.txt')])
c


# In[93]:


c.most_common(5)


# In[94]:


{ one_line.split(':')[0] :  one_line.split(':')[2]
for one_line in open('/etc/passwd')
if not one_line.startswith('#') }


# In[96]:


# walrus operator :=
# assignment expression

while s := input('Enter your name: ').strip():
    print(f'Hello, {s}!')


# In[98]:


# using the walrus for assignment in the condition

{ fields[0] : fields[2]
for one_line in open('/etc/passwd')
if not one_line.startswith('#') and (fields := one_line.split(':'))}


# In[99]:


mylist = [[10, 20, 25, 30], [40, 45, 50, 55, 60, 65],
         [70, 80], [90, 95, 100, 105]]

mylist


# In[100]:


# how can I flatten this list?

[one_item
 for one_item in mylist]


# In[101]:


# nested list comprehension
[one_item
 for one_sublist in mylist
 for one_item in one_sublist]


# In[102]:


[one_item for one_sublist in mylist for one_item in one_sublist]


# In[103]:


# nested list comprehension

[one_item
 for one_sublist in mylist
 if len(one_sublist) > 2
 for one_item in one_sublist]


# In[105]:


# nested list comprehension

[one_item
 for one_sublist in mylist
 for one_item in one_sublist
 if one_item % 2  ]  # odd number


# In[108]:


# nested list comprehension

[one_item
 for one_sublist in mylist
 if len(one_sublist) > 4
 for one_item in one_sublist
 if one_item % 2  ]  # odd number


# In[109]:


[(x,y)
 for x in range(5)
 for y in range(5)]


# In[110]:


get_ipython().system('ls movi*')


# In[111]:


get_ipython().system('head movies.dat')


# # Exercise: Movie categories
# 
# 1. Use a nested list comprehension to find the 5 most common categories for movies in `movies.dat`.
# 2. Take the output from the list comprehension, which will be a list of categories, and use `Counter` to find the most common ones.

# In[120]:


from collections import Counter

c = Counter([one_category
for one_line in open('movies.dat', encoding='Latin-1')
for one_category in one_line.split('::')[2].strip().split('|')])
c


# In[121]:


c.most_common(5)


# In[123]:


for key, value in c.most_common(5):
    print(f'{key:10}: {value}')


# In[126]:


for key, value in c.most_common(5):
    print(f'{key:10}: {int(value / 50)* "x"}')


# In[127]:


import random

numbers = [random.randint(0, 100) 
          for i in range(10)]

numbers


# In[128]:


sorted(numbers)


# In[129]:


import random

numbers = [random.randint(-100, 100) 
          for i in range(10)]

numbers


# In[130]:


sorted(numbers)


# In[131]:


sorted(numbers, key=abs)


# In[132]:


words = 'This is a sentence for my Python course at WDC'.split()

sorted(words)


# In[133]:


# case-insensitive sort
sorted(words, key=str.lower)


# In[134]:


# what if I want to sort by backwards words?
def by_backwards_word(one_word):
    return one_word[::-1]

sorted(words, key=by_backwards_word)


# In[135]:


def square(x):
    return x ** 2

square(5)


# In[136]:


lambda x: x ** 2


# In[137]:


sorted(words, key=lambda one_word: one_word[::-1])


# # Next time:
# 
# 1. `lambda` and `operator`
# 2. Objects!

# In[ ]:




