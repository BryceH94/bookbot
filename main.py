def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path) 
    word_count = get_word_count(book_contents)
    print(f"{word_count} words found in book")
    return word_count

def get_book_contents(path):
    with open(path, "r") as f:
        contents = f.read()
    return contents

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

main()  
