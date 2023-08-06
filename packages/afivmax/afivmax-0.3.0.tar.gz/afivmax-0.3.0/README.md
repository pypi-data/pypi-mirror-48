# afivmax

[![Build Status](https://travis-ci.com/eggachecat/afivmax.svg?branch=master)](https://travis-ci.com/eggachecat/afivmax)
[![PyPI version](https://badge.fury.io/py/afivmax.svg)](https://badge.fury.io/py/afivmax)
[![Coverage Status](https://coveralls.io/repos/github/eggachecat/afivmax/badge.svg?branch=master&kill_cache=1)](https://coveralls.io/github/eggachecat/afivmax?branch=master)
[![Documentation Status](https://readthedocs.org/projects/afivmax/badge/?version=latest)](https://afivmax.readthedocs.io/en/latest/?badge=latest)

# 安装
```pip install afivmax```

# 使用
```python
from afivmax.afivmax import afiv_max
# args
assert 3 == afiv_max(1, 2, 3)
assert 3 == afiv_max(3, 3, 3)


# args with key
assert 3 ==afiv_max(1, 2, 3, key=lambda x: x ** 2)
class TmpClass:
    def __init__(self, x):
        self.val = x
assert 9 == afiv_max(*[TmpClass(x) for x in range(10)], key=lambda x: x.val).val


# iterables
assert 3 == afiv_max([1, 2, 3])
assert 3 == afiv_max([3, 2, 1])
assert 3 == afiv_max([3])

# iterables with keys
assert 3 == afiv_max([1, 2, 3], key=lambda x: x ** 2)
assert 9 == afiv_max([TmpClass(x) for x in range(10)], key=lambda x: x.val).val

# iterables with default
assert 10 == afiv_max([], default=10), "iterable with default only"
```