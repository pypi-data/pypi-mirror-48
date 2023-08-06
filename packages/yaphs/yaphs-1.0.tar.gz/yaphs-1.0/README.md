# yaphs

[![pipeline status](https://gitlab.com/valtrok/yaphs/badges/master/pipeline.svg)](https://gitlab.com/valtrok/yaphs/pipelines)
[![coverage report](https://gitlab.com/valtrok/yaphs/badges/master/coverage.svg)](https://valtrok.gitlab.io/yaphs/)

Yet another python hook system for python 2.7/3.x

# Usage

## Basic usage

Import yaphs
```python
from yaphs import Hook
```

Register foo as a hook-compatible function
```python
@Hook
def foo(*args):
    print(args)
```

Register bar as a hook to be executed before calling foo
```python
@foo.before(*args):
def bar(*args):
    print('before foo, args: ' + str(args))
```

When you call foo, bar is called before
```python
foo(1, 2)
```

Expected output:
```
before foo, args: (1, 2)
(1, 2)
```

## Class usage (python 3.x only)

You can use yaphs hooks inside classes:
```python
class MyClass:
    @Hook
    def foo(self, *args)
```

When you register hooks, you just have to know that the first argument will be the object
```python
c = MyClass()

@c.foo.after:
def bar(o, *args):
    print('after foo')
    print('object: ' + str(o))
    print('args: ' + str(args))
```
