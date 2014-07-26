#!/usr/bin/python
import re

class BasicPreprocessor (object):
    def __init__ (self, process_value_func=None,
                        collapse_keys_regexps={}):
        self.process_value_func = process_value_func
        self.collapse_keys_regexps = collapse_keys_regexps
        for k, v in self.collapse_keys_regexps.iteritems():
            if isinstance(v, (str, unicode)):
                self.collapse_keys_regexps[k] = re.compile(v)

    def __call__ (self, *args, **kwargs):
        return self.preprocess(*args, **kwargs)

    def preprocess (self, struct, process_value_func=None):
        '''
Takes struct to analize and value processor function.
Returns dictionary, where keys are hash funcs of paths, and values are dicts with full (unhashed) path and list of values found by them'''
        self.result = {}
        if self.process_value_func is None:
            raise RuntimeError("Need to specify process_value_func to preprocess...")
        self.recur(struct, [])
        return self.result

    def recur (self, v, path):
        if isinstance(v, dict):
            self.parse_dict(v, path)
        elif isinstance(v, list):
            path.append("<list>")
            for el in v:
                self.recur(el, path)
            path.pop()
        else:
            pass

    def parse_dict (self, dct, path):
        for k, v in dct.iteritems():
            for re_name, re_object in self.collapse_keys_regexps.iteritems():
                if re_object.match(k):
                    k = re_name
                    break
            path.append(k)
            self.add_data(path, v) # add data about value v by path k
            self.recur(v, path) # going deeper
            path.pop()

    def add_data (self, path, v):
        hsh = hash(str(path)) # keys in result
        if not self.result.has_key(hsh):
            self.result[hsh] = {'path': path[:],
                           'values': []}
        self.result[hsh]['values'].append(self.process_value_func(v))


if __name__ == '__main__':
    from value_processors import *
    from representers import *

    represent = BasicRepresenter()
    process_value = BasicValueProcessor()
    data = {
        "a": {"aa": ["aaa", {"aab": "aaba"}],
              "ab": {"aba": "abaa",
                     "abb": {}}},
        "b": [],
        "c": 1
    }
    print represent(preprocess(data, process_value))
