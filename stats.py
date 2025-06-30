def get_num_words(text: str) -> int:
    return len(text.split())

def get_num_characters(text: str) -> int:
    count_characters = {}
    # loop through text
    for char in text.lower():
        if char in count_characters:
            count_characters[char] += 1
        else:
            count_characters[char] = 1

    return count_characters

def sort_dict(d: dict) -> dict:
    count_characters = [] # format: {"char": "b", "num": 4868}
    for k, v in d.items():
        if k.isalpha():
            count_characters.append({"char": k, "num": v})

    count_characters.sort(key=sort_on, reverse=True)
    return count_characters


def sort_on(items: dict) -> int:
    return items['num']