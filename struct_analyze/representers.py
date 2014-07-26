#!/usr/bin/python

class BasicRepresenter (object):
    '''Representer must fit value_processor'''
    def __call__ (self, *args, **kwargs):
        return self.represent(*args, **kwargs)


    def represent (self, preprocessed_struct):
        dicts = sorted(preprocessed_struct.values(),
                       self.cmp_paths,
                       lambda d: d['path'])
        def _represent_dict (d):
            return "Path: %s\nValues:\n  %s" % (
                self.represent_path(d["path"]),
                "\n  ".join(map(self.represent_value, d["values"])))
        return "REPORT...\n%s" % (
            ("\n%s\n" % ('-' * 10)).join(map(_represent_dict,
                                             dicts)))
    def cmp_paths (self, path1, path2):
        if len(path1) < len(path2):
            return -1
        elif len(path1) < len(path2):
            return 1
        else:
            return cmp(path1, path2)

    def represent_path (self, path):
        return "->".join(path)

    def represent_value (self, desc):
        if isinstance(desc, list):
            return self.represent_list(desc)
        elif isinstance(desc, dict):
            return self.represent_dict(desc)
        elif isinstance(desc, int):
            return self.represent_integer(desc)
        elif isinstance(desc, float):
            return self.represent_float(desc)
        elif isinstance(desc, str):
            return self.represent_string(desc)

    def represent_list (self, list_desc):
        '''Translates list description to human-readable text.
list_desc - a list with one element, that tells about number of elements in it'''
        el = list_desc.pop()
        assert not list_desc
        if el == 0:
            return "empty list"
        elif el == 1:
            return "list with one element"
        elif el == 2:
            return "list with many elements"
        assert 0

    def represent_dict (self, dict_desc):
        if not dict_desc:
            return "empty dict"
        else:
            return "dict with keys %s" % str(dict_desc.keys())
            
    def represent_integer (self, num_desc):
        if num_desc == 0:
            return "number 0"
        elif num_desc == 1:
            return "number 1"
        elif num_desc == 2:
            return "positive integer > 1"
        elif num_desc == -1:
            return "negative integer"
        assert 0

    def represent_float (self, num_desc):
        if float == 0:
            return "float 0"
        elif num_desc == 1:
            return "float 1"
        elif num_desc == 2:
            return "positive float > 1"
        elif num_desc == -1:
            return "negative float"
        assert 0

    def represent_string (self, string_desc):
        return "string %s" % string_desc


        
