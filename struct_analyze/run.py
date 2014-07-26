#!/usr/bin/python

if __name__ == '__main__':
    from preprocessors import *
    from value_processors import *
    from representers import *

    process_value = BasicValueProcessor()
    preprocess = BasicPreprocessor(process_value_func=process_value,
                                   collapse_keys_regexps={"<ab-s>": "ab.+"})
    represent = BasicRepresenter()
    data = {
        "a": {"aa": ["aaa", {"aab": "aaba"}, {"aab": 1.0}],
              "ab": {"aba": "abaa",
                     "abb": {}}},
        "b": [],
        "c": 1
    }
    print represent(preprocess(data))
