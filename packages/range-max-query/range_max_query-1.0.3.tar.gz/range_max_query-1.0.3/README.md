rangeMaxQuery
=======================
Python's implementation of range maximum query. 



Install 
-----

-   Install via `$ pip install range_max_query` .

How to use
-----
-   `$ from range_max_query import RangeMaxQuery` .

```

>>> A = [2, 3, 4, 1, 7]         
>>> arr = RangeMaxQuery(A)      # initialize data structure
>>> arr.range_max_query(1, 4)     # maximum query in range(1, 4)
7
>>> arr.update(1, 10)           # set A[1] = 10 and update the data structure
>>> arr.range_max_query(1, 4)    # maximum query in range(1, 4)
10

```
