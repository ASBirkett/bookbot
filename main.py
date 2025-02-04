def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(string):
    content_array = string.split()
    print(len(content_array))
        

def main():
    book_content = read_book('./books/frankenstein.txt')
    word_count(book_content)


main()