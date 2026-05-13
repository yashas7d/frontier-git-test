def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def unique(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


def safe_get(d, *keys, default=None):
    for key in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(key, default)
    return d
