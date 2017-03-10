# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are collections of elements. However, a tuple is immutable, in other words it cannot be changed after instantiation, while a list is mutable (can be modified after instantiation).
Only a tuple will work as a key in a dictionary, as keys in dictionaries need to be immutable

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are collections of elements. A list is an ordered collection, while a set is an unordered collection with no duplicate elements.  

```python  
    lst = ['z','z','z','a','b']

    sampleSet = set(lst) # set will contain {'a','b','z'}
```

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is an anonymous function (a function that is not bound to a name) in python. Python allows for functional programming, where a function is passed to another function. `lambda` in these cases allows for inline definition of functions and shortens code.  

```python
    items = [1, 2, 3, 4, 5]
    print map(lambda x: x**2, items) # output: [1, 4, 9, 16, 25]
    print reduce((lambda x, y: x * y), items) # output: 120

    #sorted using lambda function in key
    sorted(['b','bbb','a','aaaa'],key= lambda x:len(x)) # output: ['b', 'a', 'bbb',     'aaaa']
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is syntactical construct in python that allows one to derive a list from another list. In list comprehension a given operation will be applied to each element of the list and a list of results will be returned. `if` statement can be used to filter the resulting list.

```python
# list of squared numbers using list comprehension
squaredNumbers = [x**2 for x in range(10)]
print(squaredNumbers) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# equivalent using map
squaredNumbersUsingMap = map(lambda x: x**2, range(10))
print(squaredNumbersUsingMap) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# list of squared even numbers using list comprehension
evenSquaredNumbers = [x for x in squaredNumbers if x%2==0]
print(evenSquaredNumbers) # output: [0, 4, 16, 36, 64]

# equivalent using filter
evenSquaredNumbersUsingFilter = filter(lambda x: x%2 == 0, squaredNumber)
print(evenSquaredNumbersUsingFilter) # output: [0, 4, 16, 36, 64]
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
