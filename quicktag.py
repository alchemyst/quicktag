#!/usr/bin/env python

""" Supplies some utilities for creating html documents manually

>>> print(h1('test'))
<h1>
test
</h1>

>>> print(table([tr([td('d1'), td('d2')]), tr()]))
<table>
<tr>
<td>
d1
</td>
<td>
d2
</td>
</tr>
<tr />
</table>
"""
from __future__ import print_function

class tag:
    """ represents an html tag - specifically used to create outputs for web pages

    Basic usage - create a "test" tag:

    >>> print(tag('test'))
    <test />

    Attributes can be specified as a dictionary

    >>> print(tag('test', attributes={'prop': 'value'}))
    <test prop='value' />

    The real benefit - tags can be nested, allowing the python interpreter to track closing tags:

    >>> print(tag('test', tag('inner')))
    <test>
    <inner />
    </test>
    """
    def __init__(self, name, contents=[], attributes={}):
        self.name = name
        self.contents = contents
        self.attributes = attributes
    def __str__(self):
        tagcontents = self.name
        if len(self.attributes) > 0:
            attrstring = " ".join("%s='%s'" % kv for kv in self.attributes.items())
            tagcontents += " " + attrstring

        if self.contents:
            if hasattr(self.contents, '__iter__') and not hasattr(self.contents, 'strip'):
                contentstring = "\n".join(str(i) for i in self.contents)
            else:
                contentstring = str(self.contents)
            return "<%s>\n%s\n</%s>" % (tagcontents, contentstring, self.name)
        else:
            return "<" + tagcontents + " />"
    def __repr__(self):
        return "tag(%s, contents=%s, attributes=%s)" % (self.name, self.contents, self.attributes)

def namedtag(t):
    """ create a named tag class - useful for standard html tags

    >>> mytag = namedtag('mytag')
    >>> print(mytag())
    <mytag />

    """
    from functools import partial
    return partial(tag, t)

h1, h2, p, table, td, th, tr, a = (namedtag(t) for t in ("h1", "h2", "p", "table", "td", "th", "tr", "a"))

def greystring(frac, best=90, worst=255):
    """ Generate a shade number for a fraction.

    >>> greystring(0)
    '#FFFFFF'
    >>> greystring(1)
    '#5A5A5A'
    >>> greystring(0.4)
    '#BDBDBD'
    """
    #TODO: Figure out how to handle exceptions properly in doctests

    assert 0 <= frac <= 1, ValueError

    colval = int(worst + frac*(best - worst))
    return "#%X%X%X" % (colval, colval, colval)


def shadedtd(numberformat, maxvalue, value):
    """ Generate a td item with background shaded a particular fraction """
    return  td(numberformat % value, {'bgcolor': greystring(value/maxvalue)})


def _test():
    import doctest
    doctest.testmod()

    
if __name__ == "__main__":
    _test()
