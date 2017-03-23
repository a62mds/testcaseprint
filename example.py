#!/usr/bin/env python
import re
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    # From Raymond Hettinger's super() considered super talk
    """Counter that remembers the order elements are first seen"""
    def __repr__(self):
        return '{0:s}({1:s})'.format(self.__class__.__name__, OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
    @classmethod
    def get_classname(cls, fullname):
        rgx_pat = re.compile(r"<(class|type) '(.+\.)*(.*)'>")
        return re.match(rgx_pat, fullname).group(3)
    @classmethod
    def mro_names(cls):
        return [cls.get_classname(str(fullname)) for fullname in cls.mro()]
        #return list(map(cls.get_classname, map(str, cls.mro())))
    @classmethod
    def print_mro(cls):
        print('\n'.join(cls.mro_names()))


import unittest


class OrderedCounterTester(unittest.TestCase):

    def setUp(self):
        self.test_strs = ["<class '__main__.OrderedCounter'>",
                          "<class 'collections.Counter'>",
                          "<class 'collections.OrderedDict'>",
                          "<type 'dict'>",
                          "<type 'object'>"]
        self.classnames = ["OrderedCounter",
                           "Counter",
                           "OrderedDict",
                           "dict",
                           "object"]
        #print self.__class__.mro()

    def test_mro_names(self):
        self.assertEqual(self.classnames, OrderedCounter.mro_names())
    
    def test_print_mro(self):
        self.assertPrints(OrderedCounter.print_mro, '\n'.join(self.classnames))


if __name__ == '__main__':
    unittest.main()
