#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Model(dict):

    # def __init__(self, **kw):
    #     super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

def main():
    m = Model(name='Stan', age=25, sex='man')
    print(m.getValue('name'))

if __name__ == '__main__':
    main()