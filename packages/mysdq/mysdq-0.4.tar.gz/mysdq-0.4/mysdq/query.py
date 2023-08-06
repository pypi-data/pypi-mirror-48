from collections import defaultdict
import itertools
import operator
import re


class Xoperator(object):

    def __init__(self):
        self.__dict__[''] = operator.eq
        self.__dict__['in'] = self._in
        self.__dict__.update({
            fname: func for fname, func in operator.__dict__.items() if callable(func) and not fname.startswith('_')
        })

    @staticmethod
    def isnum(val):
        try:
            int(val)
            return True
        except (ValueError,):
            pass
        return False

    def icontains(self, left, right):
        return operator.contains(left.lower(), right.lower())

    def _in(self, left, right):
        return left in right

    def not_in(self, left, right):
        return left not in right

    def startswith(self, left, right):
        return left.startswith(right)

    def endswith(self, left, right):
        return left.endswith(right)

    def regex(self, string, pattern):
        return re.search(pattern, string)

    def iregex(self, string, pattern):
        return self.regex(string.lower(), pattern)


class DictQuerer(object):

    DELIMITOR = '__'

    def __init__(self, dataset, **kwargs):
        self.dataset = dataset
        self._xoperator = Xoperator()

    def __getitem__(self, idx):
        return self.dataset[idx]

    def __len__(self):
        return len(self.dataset)

    def __str__(self):
        return '%s' % self.dataset

    def __repr__(self):
        return '<%s: %s >' % (self.__class__.__name__, str(self))

    def _lookup(self, datum, key, value, **kwargs):
        keyname, _, op = key.partition(self.DELIMITOR)
        if self.DELIMITOR in op:
            if self._xoperator.isnum(keyname):
                keyname = int(keyname)
            return self._lookup(datum[keyname], op, value, **kwargs)
        if not getattr(self._xoperator, op, None):
            # handle list with indexed element
            if isinstance(datum, (list,)) and self._xoperator.isnum(keyname):
                keyname = int(keyname)
            return self._lookup(datum[keyname], '%s__eq' % op, value, **kwargs)
        # handle list
        if getattr(self._xoperator, op, None) and isinstance(datum, (list,)):
            for item in datum:
                res = self._lookup(item, key, value, **kwargs)
                if res:
                    break
            return res
        if kwargs.get('get', False):
            return datum.get(keyname)
        return getattr(self._xoperator, op)(datum.get(keyname), value)

    def filter(self, *args, **kwargs):
        result = []
        for datum in self.dataset:
            tests = []
            for key, value in kwargs.items():
                tests.append(self._lookup(datum, key, value))
            if all(tests):
                result.append(datum)

        return DictQuerer(result)

    def values(self, *args):
        data = []
        for datum in self.dataset:
            cdata = {}
            for key in args:
                cdata[key] = self._lookup(datum, key, datum.get(key, None), get=True)
            data.append(cdata)
        return data

    def apply(self, func=lambda x: x, *args):
        for datum in self.dataset:
            for key in args:
                datum[key] = func(datum[key])
        return self

    def exists(self):
        return bool(len(self.dataset))

    def count(self):
        return len(self)

    def get(self, *args, **kwargs):
        result = self.filter(*args, **kwargs)
        if not result:
            return None
        if len(result) > 1:
            raise Exception('Multiple values returned')
        return result[0]

    def delete(self, *args, **kwargs):
        if kwargs:
            result = self.filter(*args, **kwargs)
            if result.exists():
                self.dataset = [datum for datum in self.dataset if datum not in result.dataset]
                return True
        else:
            self.dataset = []
            return True
        return False

    def order_by(self, *args, **kwargs):
        res = sorted(self.dataset, key=operator.itemgetter(*args))
        if not kwargs.get('asc', True):
            res = reversed(res)
        return DictQuerer(list(res))

    def group_by(self, *args):
        result = defaultdict(list)
        res = sorted(self.dataset, key=operator.itemgetter(*args))
        for key, group in itertools.groupby(res, operator.itemgetter(*args)):
            result[key].extend(list(group))
        return result

    def first(self):
        return self[0]

    def last(self):
        return self[-1]
