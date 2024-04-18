def analyze_text_a(text: str) -> dict:
    words = text.split()
    details: dict = {
        "words": words,
        "amount": len(words),
        "chars": len(''.join(words)),
        "reversed": words[::-1],
    }
    return details


def analyze_text_b(text: str) -> dict:
    details: dict = {
        "words": (words := text.split()),
        "amount": len(words),
        "chars": len(''.join(words)),
        "reversed": words[::-1],
    }
    return details


# If many variables, this can be useful
def analyze_text_c(text: str) -> dict:
    return {
        "words": (words := text.split()),
        "amount": (amount := len(words)),
        "chars": (chars := len(''.join(words))),
        "reversed": (reversed_words := words[::-1]),
    }
    return details


# Example usage

print(analyze_text_a("Hello, World!"))
print(analyze_text_b("Hello, World!"))
print(analyze_text_c("Hello, World!"))
