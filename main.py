def get_book_text(filepath):

    with open(filepath) as f:

        text = f.read()

    return text

from stats import word_count
from stats import char_count


def main():
    
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    character_counts = char_count(book_text)
    print(f"{num_words} words found in the document")
    print (character_counts)



main()