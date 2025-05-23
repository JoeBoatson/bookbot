import sys
from stats import word_count
from stats import char_count
from stats import dict_sorter

['main.py', 'books/frankenstein.txt']
list_length = len(sys.argv)
if list_length != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):

    with open(filepath) as f:

        text = f.read()

    return text
#hi my love


def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = word_count(book_text)
    character_counts = char_count(book_text)
    sorted_list = dict_sorter(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    for item in sorted_list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
