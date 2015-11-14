from __future__ import division

import collections
import re
import sys

if sys.version_info[0] == 2:
    range = xrange

ROMAN_RANGE = range(1, 4000)
ROMAN_REGEX = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', re.IGNORECASE)
ROMAN_CHARMAP = collections.OrderedDict([
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
])

BINARY_SUFFIX = collections.OrderedDict([
    (1125899906842624, 'PB'),
    (1099511627776, 'TB'),
    (1073741824, 'GB'),
    (1048576, 'MB'),
    (1024, 'kB'),
    (0, 'bytes')
])

METRIC_SUFFIX = collections.OrderedDict([
    (1000000000000000, 'P'),
    (1000000000000, 'T'),
    (1000000000, 'G'),
    (1000000, 'M'),
    (1000, 'k'),
    (0, '')
])

def ordinalize(number):
    number = int(number)
    return "{}{}".format(number, ordinal(number))

def ordinal(number):
    number = abs(int(number))

    if number % 100 in range(11, 14):
        return "th"

    number %= 10
    if number == 1:
        return "st"
    elif number == 2:
        return "nd"
    elif number == 3:
        return "rd"
    else:
        return "th"

def toRoman(number):
    number = int(number)

    if number not in ROMAN_RANGE:
        raise AttributeError

    roman = ""
    while number > 0:
        for key, val in ROMAN_CHARMAP.items():
            if number >= val:
                roman += key
                number -= val
                break
    return roman

def fromRoman(text):
    if not text or ROMAN_REGEX.match(text) is None:
        raise AttributeError

    total = 0
    strlen = len(text)

    while strlen > 0:
        strlen -= 1
        digit = ROMAN_CHARMAP[text[strlen]]
        if strlen > 0:
            prevDig = ROMAN_CHARMAP[text[strlen - 1]]
            if prevDig < digit:
                digit -= prevDig
                strlen -= 1
        total += digit
    return total

def binarySuffix(number):
    number = int(number)

    if number < 0:
        return str(number)

    for key, val in BINARY_SUFFIX.items():
        if key <= number:
            number = round(number / key, 2 if key > 1024 else 0) if key > 0 else number
            number = int(number) if int(number) == number else number
            return "{} {}".format(number, val)

    return str(number)

def preciseBinarySuffix(number, precision):
    number = int(number)

    if number < 0:
        return number

    for key, val in BINARY_SUFFIX.items():
        if key <= number:
            number = number / key if key > 0 else number
            return ("{:." + str(precision) + "f} {}").format(number, val)

    return number

def metricSuffix(number):
    number = int(number)

    for key, val in METRIC_SUFFIX.items():
        if key <= number:
            number = round(number / key, 2 if key > 1000 else 1) if key > 0 else number
            number = int(number) if int(number) == number else number
            return "{}{}".format(number, val)

    return str(number)
