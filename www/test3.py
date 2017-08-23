#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Foo(object):
    id = 'foo'
    @classmethod
    def func(cls):
        print(cls.id)

def main():
    Foo.func()
    f = Foo()

if __name__ == '__main__':
    main()