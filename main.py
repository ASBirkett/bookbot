def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(string):
    content_array = string.split()
    print(len(content_array))

def get_distinct_character_count(string):
    character_count = len(string)
    character_count_dictionary = {}
    for i in range(0, character_count):
        lower_case_char = string[i].lower()
        if lower_case_char not in character_count_dictionary:
            character_count_dictionary[lower_case_char] = 1
        else:
            character_count_dictionary[lower_case_char] += 1

    return character_count_dictionary

def main():
    book_content = read_book('./books/frankenstein.txt')
    # word_count(book_content)
    distinct_character_count_result = get_distinct_character_count(book_content)

    print(distinct_character_count_result)


main()