def word_count(text):
    # words = str.split()
    # return len(words)
    return len(text.split())

def character_count(str):
    lowered_str = str.lower()
    char_count = {}

    for char in lowered_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' was found {char_count[char]} times")

    return char_count

# def sort_characters(dictionary):




def sort_on(items):
    return items[int]