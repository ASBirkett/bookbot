def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(book_content):
    content_array = book_content.split()
    return len(content_array)

def get_distinct_character_count(book_content):
    character_count = len(book_content)
    character_count_dictionary = {}
    for i in range(0, character_count):
        lower_case_char = book_content[i].lower()
        if lower_case_char not in character_count_dictionary:
            character_count_dictionary[lower_case_char] = 1
        else:
            character_count_dictionary[lower_case_char] += 1

    return character_count_dictionary

def print_book_report(word_count, character_count_dictionary):
    print(f'{word_count} words found in the document')
    print()
    for dic in character_count_dictionary:
        if(dic.isalpha()):
            print(f'The \'{dic}\' character was found {character_count_dictionary[dic]} times')


def main():
    book_content = read_book('./books/frankenstein.txt')
    book_word_count = get_word_count(book_content)
    distinct_character_count_result = get_distinct_character_count(book_content)
    print_book_report(book_word_count, distinct_character_count_result)
    


main()