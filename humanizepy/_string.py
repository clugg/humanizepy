def humanize(text, capitalize=True, separator='_', forbiddenWords=None):
    if forbiddenWords is None:
        forbiddenWords = ["id"]

    text = " ".join([x for x in text.lower().split(separator) if x not in forbiddenWords])
    return text.title() if capitalize else text

def truncate(text, length, append=""):
    length = int(length)
    strlen = len(text)
    i = 0
    while (i < strlen) and (i < length or text[i] != " "):
        i += 1
    return text[:i] + append
