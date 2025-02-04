def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
        

def main():
    book_content = read_book('./books/frankenstein.txt')
    print(book_content)


main()