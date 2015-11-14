#humanizepy

This package was inspired by [PHP Humanizer](https://github.com/coduo/php-humanizer) and a lot of the code is directly ported from that repo, as well as the README itself.
Apologies for the messy and undocumented code, this was made in 2 hours.

#Usage

## Text

**Humanize**

```python
>>> import humanizepy

>>> print humanizepy.string.humanize('field_name')
Field Name
>>> print humanizepy.string.humanize('user_id')
User
>>> print humanizepy.string.humanize('field_name', False)
field name
```

**Truncate**

Truncate string to word closest to a certain length

```python
>>> import humanizepy

>>> text = 'Lorem ipsum dolorem si amet, lorem ipsum. Dolorem sic et nunc.'
>>> print humanizepy.string.truncate(text, 8)
Lorem ipsum
>>> print humanizepy.string.truncate(text, 8, '...')
Lorem ipsum...
>>> print humanizepy.string.truncate(text, 2)
Lorem
>>> print humanizepy.string.truncate(text, len(text))
Lorem ipsum dolorem si amet, lorem ipsum. Dolorem sic et nunc.
```

## Number

**Ordinalize**

```python
>>> import humanizepy

>>> print humanizepy.number.ordinalize(0)
0th
>>> print humanizepy.number.ordinalize(1)
1st
>>> print humanizepy.number.ordinalize(2)
2nd
>>> print humanizepy.number.ordinalize(23)
23rd
>>> print humanizepy.number.ordinalize(1002)
1002nd
>>> print humanizepy.number.ordinalize(-111)
-111th
```

**Ordinal**

```python
>>> import humanizepy

>>> print humanizepy.number.ordinal(0)
th
>>> print humanizepy.number.ordinal(1)
st
>>> print humanizepy.number.ordinal(2)
nd
>>> print humanizepy.number.ordinal(23)
rd
>>> print humanizepy.number.ordinal(1002)
nd
>>> print humanizepy.number.ordinal(-111)
th
```

**Roman numbers**
```python
>>> import humanizepy

>>> print humanizepy.number.toRoman(1)
I
>>> print humanizepy.number.toRoman(5)
V
>>> print humanizepy.number.toRoman(1300)
MCCC

>>> print humanizepy.number.fromRoman("MMMCMXCIX")
3999
>>> print humanizepy.number.fromRoman("V")
5
>>> print humanizepy.number.fromRoman("CXXV")
125
```

**Binary Suffix**

Convert a number of bytes in to the highest applicable data unit

```python
>>> import humanizepy

>>> print humanizepy.number.binarySuffix(0)
0 bytes
>>> print humanizepy.number.binarySuffix(1)
1 bytes
>>> print humanizepy.number.binarySuffix(1024)
1 kB
>>> print humanizepy.number.binarySuffix(1025)
1 kB
>>> print humanizepy.number.binarySuffix(1536)
2 kB
>>> print humanizepy.number.binarySuffix(1048576 * 5)
5 MB
>>> print humanizepy.number.binarySuffix(1073741824 * 2)
2 GB
>>> print humanizepy.number.binarySuffix(1099511627776 * 3)
3 TB
>>> print humanizepy.number.binarySuffix(1325899906842624)
1.18 PB
```

Number can also be humanized with a specific number of decimal places with `preciseBinarySuffix(number, precision)`

```python
>>> import humanizepy

>>> print humanizepy.number.preciseBinarySuffix(1024, 2)
1.00 kB
>>> print humanizepy.number.preciseBinarySuffix(1325899906842624, 3)
1.178 PB
```

**Metric Suffix**

```python
>>> import humanizepy

>>> print humanizepy.number.metricSuffix(-1)
-1
>>> print humanizepy.number.metricSuffix(0)
0
>>> print humanizepy.number.metricSuffix(1)
1
>>> print humanizepy.number.metricSuffix(101)
101
>>> print humanizepy.number.metricSuffix(1000)
1k
>>> print humanizepy.number.metricSuffix(1240)
1.2k
>>> print humanizepy.number.metricSuffix(1240000)
1.24M
>>> print humanizepy.number.metricSuffix(3500000)
3.5M
```

## Collections

**Oxford**

```python
>>> import humanizepy

>>> print humanizepy.collection.oxford(['Michal', 'Norbert', 'Lukasz', 'Pawel'], 2)
Michal, Norbert, and 2 others
>>> print humanizepy.collection.oxford(['Michal', 'Norbert', 'Lukasz'], 2)
Michal, Norbert, and 1 other
>>> print humanizepy.collection.oxford(['Michal', 'Norbert'])
Michal and Norbert
```

## Date time

**Difference**

```python
>>> from datetime import datetime
>>> import humanizepy

>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=15, month=11))
'just now'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=15, month=11, second=5))
'5 seconds from now'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11, second=5), datetime(year=2015, day=15, month=11))
'5 seconds ago'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=15, month=11, minute=1))
'1 minute from now'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=19, month=11, minute=1))
'4 days from now'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=22, month=11))
'1 week from now'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2016, day=22, month=1))
'2 months from now'
>>> humanizepy.datetime.difference(datetime(year=2015, day=15, month=11), datetime(year=2018, day=5, month=1))
'2 years from now'
```

**Precise difference**

```python
>>> from datetime import datetime
>>> import humanizepy

>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=15, month=11))
'just now'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=15, month=11, second=5))
'5 seconds from now'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11, second=5), datetime(year=2015, day=15, month=11))
'5 seconds ago'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=15, month=11, minute=1))
'1 minute from now'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=19, month=11, minute=1))
'4 days, 1 minute from now'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2015, day=22, month=11))
'1 week from now'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2016, day=22, month=1))
'2 months, 1 week, 1 day from now'
>>> humanizepy.datetime.preciseDifference(datetime(year=2015, day=15, month=11), datetime(year=2018, day=5, month=1))
'2 years, 1 month, 3 weeks, 12 hours from now'
```
