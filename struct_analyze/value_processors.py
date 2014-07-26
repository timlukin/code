#!/usr/bin/python

class BasicValueProcessor (object):
    def __call__ (self, *args, **kwargs):
        return self.process_value(*args, **kwargs)

    def process_value(self, v):
        if isinstance(v, list):
            return self.process_list_value(v)
        elif isinstance(v, dict):
            return self.process_dict_value(v)
        elif isinstance(v, int):
            return self.process_integer_value(v)
        elif isinstance(v, float):
            return self.process_float_value(v)
        elif isinstance(v, str):
            return self.process_string_value(v)
        else:
            raise TypeError("%s doesn't know, how process argument %s of type %s" % (
                self.__class__.__name__, v, type(v)))

    def process_list_value (self, v):
        if len(v) == 0:
            return [0]
        elif len(v) == 1:
            return [1]
        else:
            return [2]

    def process_dict_value (self, v):
        return {k: None for k in v.iterkeys()}

    def process_integer_value(self, v):
        if v in (0, 1):
            return v
        elif v > 0:
            return 2
        else:
            return -1

    def process_float_value(self, v):
        if v in (0, 1):
            return v
        elif v > 0:
            return 2.0
        else:
            return -1.0

    def process_string_value(self, v):
        return v
