def read_book(path):
    with open(path) as f:
        #read file
        file_contents = f.read()
        return file_contents

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for char in text:
        low_case = char.lower()
        if low_case in chars:
            chars[low_case] += 1
        else:
            chars[low_case] = 1
    return chars

def get_report(book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for char in char_count:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found '{char_count[char]}' times")
    print("--- End report ---")

def sort_dict(my_dict):
    return dict(sorted(my_dict.items()))


def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_dict = sort_dict(char_count)
    # print(word_count)
    # print(char_count)
    get_report(book_path, word_count, sorted_dict)

main()