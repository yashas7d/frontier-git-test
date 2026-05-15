def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))


def percentage(part, total):
    return round((part / total) * 100, 2) if total != 0 else 0


def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
