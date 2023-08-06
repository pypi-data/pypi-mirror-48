# `@cls` - Class Made Aware to Decorator

![GitHub](https://img.shields.io/github/license/guoquan/acls.svg)
|
[![CircleCI](https://circleci.com/gh/guoquan/acls/tree/master.svg?style=svg)](https://circleci.com/gh/guoquan/acls/tree/master)
|
[![Build Status](https://travis-ci.org/guoquan/acls.svg?branch=master)](https://travis-ci.org/guoquan/acls)
|
[![codecov](https://codecov.io/gh/guoquan/acls/branch/master/graph/badge.svg)](https://codecov.io/gh/guoquan/acls)


The purpose of this library is to provide possibility to create decorators, especially in super classes, with current class `cls` as argument.
Everything are centered with our new `cls` module, keyword, magic, or what every you think it would be.

## Get Start

A typical snippet looks like:

```python
from functools import wraps
import cls


class Base(metaclass=cls.ClsMeta):
  @cls
  def decor(cls, decor_arg):
    def wrap(func):
      @wraps(func)
      def wrapper(self):
        # do something with `func`
        retval = func(self)
        # do something with `retval`
        return retval
      return wrapper
    return wrap

class Extended(Base):
  @cls.decor('some arg')
  def func(self):
    # do something
    pass
```

The magic is that you can use `@cls.decor` in `Extended` class, which is inheritance from `Base`.
What is more, with in the decorator `Base.decor`, argument `cls` will be assigned with the correct current class.
In this example, it would simply be a reference to `Extended`.
This would be helpful if you want to make use of some class property here in the decorator.

## Magic

Well, there is no magic. I created a delegator in class namespace to enable both class possible to use `@cls`.
So, it is not the module `cls` as we imported on the top.
I use this to make it more consistent looking, and fool some interpreters like `pylint`.
No offense, just want to make them less noisy.

## Limitations

Unfortunately, This work is based on [customizing python class creation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation).
I have to make use of [`__prepare__`](https://www.python.org/dev/peps/pep-3115/#id11), which is [introduced](https://www.python.org/dev/peps/pep-3115/) only to [python 3](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation).
That means there is no known possible backward compatibility with [python 2](https://docs.python.org/2/reference/datamodel.html#customizing-class-creation) now.
The code is tested against python 3.5+.

Please let me know if you come up with an idea how to manipulate class creation in python 2.

There are a couple of issues, with which I am talking. Contributions are welcome.

### Known issue

- [ ] relying on length of arguments and `callable()` to support optional arguments in decorator
- [ ] not compatible with `@classmethod`, or many other decorators
- [ ] make `pylint` really noisy
- [ ] no documents :see_no_evil:!
