# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similarities:  
   
   1. Both lists and tuples allow for duplicates     
   2. Both lists and tuples can be indexed, sliced and selected using integer values within brackets.    
   3. Two tuples or two lists are both compared by their first element, and if there is a tie, then by the second element, and       so on. No further attention is paid to subsequent elements after earlier elements show a difference.         
   
   Differences: 
   
   1. Tuple are immutable whereas lists are mutable  
   2. Lists are enclosed in square brackets, whereas tuples are enclosed in parenthesis  
   3. Tuple have heterogeneous data, whereas lists are homogenous  
   
   Tuples work as keys in dictionaries, primarily because they are immutable.  


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similarities:  
  
   1. Both are collections of objects.  
   2. Both lists and sets support append and pop operations  
   
   Differences:  
   
   1. Sets can’t have duplicate elements whereas lists can  
   2. Sets are unordered and immutable whereas lists are not  
   3. Sets can only contain hashable elements  
   
   List e.g.  
   >> Names_list = [“Jack”, “John”, “Mary”, “Tim”, “John”]  
   >> print Names_list  
   Output: ['Jack', 'John', 'Mary', 'Tim', 'John']  
   
   >> Names_set = (["Jack", "John", "Mary", "Tim", "John"])  
   >> print Names_set  
   Output: Set(['Tim', 'John', 'Jack', 'Mary'])  
   
   Sets are much faster than lists for finding an element. In a set, the search operation has a speed of O(1), whereas in a      list the search operation takes O(logN). This kind of speed is accomplished through the use of an open address hash table      as the underlying data structure.  


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>lambda is a construct in Python used for creating anonymous functions at runtime. We use lambda functions when we require a nameless function for a short period of time. In Python, we generally use lambda as an argument to a higher-order function (a function that takes in other functions as arguments). Lambda functions are used along with built-in functions like filter(), map() and reduce().  

An example of using lambda in the key argument is given below:

>> word_list = ['lowercase', 'words', 'sort', 'Uppercase']
>> sorted (word_list)
['Uppercase', 'lowercase', 'sort', 'words']

The sorted function sorts uppercased words before words that are lowercased as shown above. However, we can lowercase all the words before sorting using lambda as shown below:

>> sorted ([word_list, key=lambda word: word.lower())
['lowercase', 'sort', 'Uppercase', 'words']


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





