from stats import word_count, character_count

def main():
    book_text = get_book_text("books/frankenstein.txt")

    # print(f"Word count: {word_count(file_contents)}")
    print(f"Found {word_count(book_text)} total words")

    char_count = character_count(book_text)
    # print(f"Character count: {char_count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
        # file_contents = f.read()
        # print(file_contents)


main()