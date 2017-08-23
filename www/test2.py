#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Foo(object):
    bar = True

def echo_bar(self):
    print(self.bar)
    return 1

def main():
    FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
    print(FooChild().echo_bar())

if __name__ == '__main__':
    main()