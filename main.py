def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

        print(f"Word count: {word_count(file_contents)}")

        char_count = character_count(file_contents)
        print(f"Character count: {char_count}")



def word_count(str):
    words = str.split()
    return len(words)



def character_count(str):
    lowered_str = str.lower()

    char_count = {}

    for char in lowered_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count






main()