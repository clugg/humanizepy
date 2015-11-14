def oxford(collection, limit=None):
    collen = len(collection)
    limit = limit if limit else collen

    if limit >= collen:
        return ", ".join(collection)[::-1].replace(" ,", " dna ")[::-1]
    else:
        others = collen - limit
        return ", ".join(collection[:limit]) + ", and {} other{}".format(others, "" if others == 1 else "s")
