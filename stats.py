def get_book_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def get_char_count(file_contents):
    char_dict = {}
    for char in file_contents:
        lower_char = char.lower()
        char_dict[lower_char] = char_dict.get(lower_char,  0) + 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(file_contents):
    sorted_list = []
    char_dict = get_char_count(file_contents)
    for key, value in char_dict.items():
        dict_value = {"char": key, "num": value}
        sorted_list.append(dict_value)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list