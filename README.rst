Quicktag 
========
.. image:: https://travis-ci.org/alchemyst/quicktag.png?branch=master   
   :target: https://travis-ci.org/alchemyst/quicktag
   :alt: Test status
   
.. image:: https://landscape.io/github/alchemyst/quicktag/master/landscape.svg
   :target: https://landscape.io/github/alchemyst/quicktag/master
   :alt: Code Health
   
.. image:: https://coveralls.io/repos/alchemyst/quicktag/badge.svg
  :target: https://coveralls.io/r/alchemyst/quicktag
  :alt: Coverage


Supplies some utilities for creating html documents manually

Simple usage for one tag::

    >>> print h1('test')
    <h1>
    test
    </h1>
    
A more elaborate example::

    >>> print table([tr([td('d1'), td('d2')]), tr()])
    <table>
    <tr>
    <td>
    d1
    </td>
    <td>
    d2
    </td>
    </tr>
    <tr></tr>
    </table>
