from __future__ import division

import collections
import importlib
from datetime import datetime
from time import mktime

DATE_SUFFIX = collections.OrderedDict([
    (31557600, "year"),
    (2592000, "month"),
    (604800, "week"),
    (86400, "day"),
    (3600, "hour"),
    (60, "minute"),
    (0, "second")
])

def difference(tfrom, tto):
    if type(tfrom) == datetime:
        tfrom = mktime(tfrom.timetuple())
    if type(tto) == datetime:
        tto = mktime(tto.timetuple())

    tfrom, tto = int(tfrom), int(tto)
    distance = tto - tfrom

    if distance == 0:
        return "just now"

    present = "from now" if distance > 0 else "ago"
    distance = abs(distance)

    for key, val in DATE_SUFFIX.items():
        if key <= distance:
            distance = int(distance / key) if key > 0 else distance
            return "{} {}{} {}".format(distance, val, "" if distance == 1 else "s", present)

def preciseDifference(tfrom, tto):
    if type(tfrom) == datetime:
        tfrom = mktime(tfrom.timetuple())
    if type(tto) == datetime:
        tto = mktime(tto.timetuple())

    tfrom, tto = int(tfrom), int(tto)
    distance = tto - tfrom

    if distance == 0:
        return "just now"

    present = "from now" if distance > 0 else "ago"
    distance = abs(distance)

    values = []
    for key, val in DATE_SUFFIX.items():
        if key <= distance:
            value = int(distance / key) if key > 0 else distance
            distance -= value * (key if key > 0 else 1)
            values.append("{} {}{}".format(value, val, "" if value == 1 else "s"))
            if distance <= 0:
                break
    return ", ".join(values) + " " + present
