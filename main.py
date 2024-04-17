def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path) 
    word_count = get_word_count(book_contents)
    print(f"{word_count} words found in book")
    letter_counts = get_letter_counts(book_contents)
    print("Printing massive letter count dict...")
    print(letter_counts)

def get_book_contents(path):
    with open(path, "r") as f:
        contents = f.read()
    return contents

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_letter_counts(text):
    letter_counts = {}
    for char in text:
        char = char.lower()
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

main()  
