#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. `sorted`, `lambda`, `operator`
# 2. Objects
#     - Classes
#     - Instances
#     - Attributes
#     

# In[11]:


import random

random.seed(0)
numbers = [random.randint(0, 10000)
          for i in range(10)]

numbers


# In[12]:


sorted(numbers)


# In[13]:


numbers = [5, 7, 30, 2, 100, 20, 45, 4]
sorted(numbers)


# In[14]:


sorted(numbers, key=lambda one_number: str(one_number))


# In[15]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

[line_to_dict(one_line)
 for one_line in open('shoe-data.txt')]


# # Exercise: Sorting shoes
# 
# 1. Print the list of shoes, sorted by (ascending) size.
# 2. Print the list of shoes, sorted by the brand.
# 3. Print the list of shoes, sorted first by brand and then by size.
# 4. Ask the user which field should be used for sorting (brand/color/size), and then sort by that size.

# In[16]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

shoes = [line_to_dict(one_line)
 for one_line in open('shoe-data.txt')]


# In[19]:


def by_size(shoe_dict):
    return shoe_dict['size']

sorted(shoes, key=by_size)


# In[20]:


# def by_size(shoe_dict):
#     return shoe_dict['size']

sorted(shoes, key=lambda shoe_dict: shoe_dict['size'])


# In[21]:


sorted(shoes, key=lambda shoe_dict: shoe_dict['brand'])


# In[22]:


sorted(shoes, key=lambda shoe_dict: (shoe_dict['brand'], 
                                     shoe_dict['size']))


# In[23]:


sorted(shoes, key=lambda shoe_dict: (shoe_dict['brand'], 
                                     shoe_dict['size']), reverse=True)


# In[27]:


sorted(shoes, key=lambda shoe_dict: (shoe_dict['brand'], 
                                     -int(shoe_dict['size'])))


# In[30]:


field = input('Enter sort field: ').strip()

def by_user_choice(user_dict):
    return user_dict[field]    

sorted(shoes, key=by_user_choice)


# In[31]:


field = input('Enter sort field: ').strip()

def by_user_choice(sort_field):
    def by_field(shoe_dict):
        return shoe_dict[sort_field]   
    return by_field

sorted(shoes, key=by_user_choice(field))


# In[32]:


fields = input('Enter sort fields: ').split()

def by_user_choice(sort_fields):
    def by_field(shoe_dict):
        return [shoe_dict[one_field]   
                for one_field in sort_fields]
    return by_field

sorted(shoes, key=by_user_choice(fields))


# In[33]:


import operator


# In[34]:


operator.itemgetter('brand')


# In[35]:


sorted(shoes, key=operator.itemgetter('brand'))


# In[ ]:





# In[36]:


sort_field = input('Enter sort field: ').strip()

sorted(shoes, key=operator.itemgetter(sort_field))


# In[38]:


sort_fields = input('Enter sort fields: ').split()

sorted(shoes, key=operator.itemgetter(*sort_fields))


# In[39]:


a = 5


# In[40]:


print(a)   # LEGB  -- local, enclosing, global, builtin


# In[43]:


# attributes -- a kind of private dict for each object

a.b   # we're asking for the value of attribute b that belongs to variable a


# In[44]:


# ICPO -- instance, class, parent, "object" (the ultimate object in our hierarchy)
# the search path for attributes in Python


# In[46]:


class MyClass:
    pass


# In[47]:


m1 = MyClass()
m2 = MyClass()


# In[48]:


type(m1)


# In[49]:


type(m2)


# In[50]:


m1.x = 100
m1.y = [10, 20, 30]

m2.a = {10, 20, 30, 40, 50}
m2.b = 'hello, out there!'


# In[51]:


vars(m1)


# In[52]:


vars(m2)


# In[56]:


class MyClass:
    def __init__(self):
        self.x = 100
        self.y = [10, 20, 30]


# In[57]:


m1 = MyClass()
m2 = MyClass()


# In[58]:


vars(m1)


# In[59]:


vars(m2)


# In[60]:


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
m1 = MyClass(100, [10, 20, 30])
m2 = MyClass(2345, [1000, 2000, 3000])        


# In[61]:


vars(m1)


# In[62]:


vars(m2)


# In[ ]:


m1 = MyClass(10, 20)

# MyClass.__new__(*args, **kwargs)
#    o = [new object]
#    MyClass.__init__(o, *args, **kwargs)
#    return o


# In[66]:


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, new_x):
        self.x = new_x
        
    def set_y(self, new_y):
        self.y = new_y
        
m1 = MyClass(100, [10, 20, 30])
print(m1.get_x())
m1.set_x(2345)   # MyClass.set_x(m1, 2345)
print(m1.get_x())


# In[64]:


s = 'abcd'

s.upper()  


# In[65]:


str.upper(s)


# In[68]:


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._z = 100
                
m1 = MyClass(100, [10, 20, 30])
print(m1.x)
m1.x = 2345
print(m1.x)


# # Exercise: Book
# 
# 1. Define a `Book` class, with three attributes passed when we create each instance: `title`, `author`, and `price`.
# 2. Define three instances of `Book`.
# 3. Define a `Shelf` class, with one attribute, `books` (will be a list).
# 4. Define an `add_books` method that takes any number of `Book` objects, and puts them on the shelf.
# 5. Define a `titles` method that returns a list of strings, the titles of the books on the shelf.

# In[74]:


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
b1 = Book('title1', 'author1', 100)        
b2 = Book('title2', 'author2', 125)
b3 = Book('title3', 'author2', 150)

class Shelf:
    def __init__(self):
        self.books = []
        
    def add_books(self, *args):
        self.books += args
        
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
    def total_price(self):
        return sum([one_book.price
                   for one_book in self.books])
    
s = Shelf()
s.add_books(b1, b2)
s.add_books(b3)

print(s.titles())


# In[87]:


print('A')
class Person:
    x = 100  # what is this???  -- it's a class attribute
    
    print('B')
    def __init__(self, name):
        z = 100         # local variable -- dissappears when __init__ exists
        print('C')
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
        
    print('D')
print('E')
        
p1 = Person('name1')
p2 = Person('name2')


# In[88]:


Person.x


# In[89]:


p1.x   # (I) does p1 have x? NO ... (C) does type(p1) have x?  YES


# In[90]:


p2.x# (I) does p2 have x? NO ... (C) does type(p2) have x?  YES


# In[ ]:


p1.greet() # ICPO -- does p1 have greet? NO  ... (C) does Person have greet? YES


# # Search path
# 
# ## Variables
# - `L` local
# - `E` enclosing
# - `G` global
# - `B` builtin
# 
# ## Attributes
# - `I` instance
# - `C` instance's class
# - `P` instance's class's parent(s)
# - `O` object, at top of hierarchy

# In[92]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
        
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())

class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        
    def greet(self):
        return f'Hello, {self.name}!'
    
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())
print(e2.greet())


# In[94]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
        
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())  # p1 has greet? NO... .Person has greet? YES
print(p2.greet())

class Employee(Person):  # ICPO -- instance, class, parent, object
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
            
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())  # e1 has greet? NO.... Employee has greet? NO.... Person has greet? YES!
print(e2.greet())


# In[96]:


class MyClass:
    pass

m = MyClass(10)  # m has __init__?  NO.. MyClass has __init__?  NO object has __init__? 


# In[98]:


class BigParent:
    def __init__(self, x):
        self.x = x
        
    def greet(self):
        return f'BigParent says hello, x = {self.x}'
    
class OneChild(BigParent):
    def greet(self):
        return f'OneChild says hello, x = {self.x}'
    
class SecondChild(BigParent):
    def greet(self):
        return f'SecondChild says hello, x = {self.x}'
    
sc = SecondChild(100)  # sc.__init__ ?? NO.  SecondChild.__init__? NO. BigParent.__init__? YES
sc.greet() # sc.greet? NO.  SEcondChild.greet? YES.


# In[102]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
        
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())  # p1 has greet? NO... .Person has greet? YES
print(p2.greet())

class Employee(Person):  # ICPO -- instance, class, parent, object
    def __init__(self, name, id_number):
        # Person.__init__(self, name)
        super().__init__(name)
        self.id_number = id_number
                   
#     def greet(self):
#         return f'{super().greet()}!!!!!!'

e1 = Employee('emp1', 1)  # e1.__init__? NO... Employee.__init__? YES
e2 = Employee('emp2', 2)

print(e1.greet())  # e1 has greet? NO.... Employee has greet? NO.... Person has greet? YES!
print(e2.greet())


# In[103]:


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
b1 = Book('title1', 'author1', 100)        
b2 = Book('title2', 'author2', 125)
b3 = Book('title3', 'author2', 150)

class Shelf:
    def __init__(self):
        self.books = []
        
    def add_books(self, *args):
        self.books += args
        
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
    def total_price(self):
        return sum([one_book.price
                   for one_book in self.books])
    
s = Shelf()
s.add_books(b1, b2)
s.add_books(b3)

print(s.titles())


# # Exercise: BigShelf
# 
# 1. Add a class attribute, `max_books` to `Shelf`.  If someone tries to add more than 5 books, they get an exception.
# 2. Define a new class, `BigShelf`, which is the same as `Shelf`, but takes up to 10 books.  

# In[105]:


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
b1 = Book('title1', 'author1', 100)        
b2 = Book('title2', 'author2', 125)
b3 = Book('title3', 'author2', 150)
b4 = Book('title4', 'author2', 150)
b5 = Book('title5', 'author2', 150)
b6 = Book('title6', 'author2', 150)
b7 = Book('title7', 'author2', 150)


class Shelf:
    max_books = 5     # Shelf.max_books = 5    
    
    def __init__(self):
        self.books = []
        
    def add_books(self, *args):
        for one_book in args:
            if len(self.books) >= self.max_books:
                raise ValueError('Too many books!')
            self.books.append(one_book)
        
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
    def total_price(self):
        return sum([one_book.price
                   for one_book in self.books])
    

class BigShelf(Shelf):
    max_books = 10
    
    
s = BigShelf()
s.add_books(b1, b2)
s.add_books(b3, b4, b5)
s.add_books(b6, b7)

print(s.titles())
    


# # Next time
# 
# 1. Multiple inheritance
# 2. Magic methods / operator overloading
# 3. Properties
# 4. Descriptors

# In[ ]:




