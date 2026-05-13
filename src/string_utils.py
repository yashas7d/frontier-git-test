def truncate(text, max_len, suffix="..."):
    return text if len(text) <= max_len else text[:max_len - len(suffix)] + suffix


def slugify(text):
    return text.strip().lower().replace(" ", "-")


def camel_to_snake(name):
    result = []
    for i, ch in enumerate(name):
        if ch.isupper() and i > 0:
            result.append("_")
        result.append(ch.lower())
    return "".join(result)


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
