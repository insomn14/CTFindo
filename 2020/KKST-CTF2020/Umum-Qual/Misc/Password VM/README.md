# Solution

```
>>> import hashlib, itertools
>>> for i,j in itertools.product(printable, printable):
...     tmp = hashlib.sha1(f'6879d9f430{i}554b113292dfc94d7335{j}'.encode()).hexdigest()
...     if tmp == know:
...             print(f'6879d9f430{i}554b113292dfc94d7335{j}')
... 
6879d9f4300554b113292dfc94d7335a
```

Flag : `KKST2020{6879d9f4300554b113292dfc94d7335a}`
