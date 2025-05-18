def word_count(book_text):

    words_list = book_text.split()
    number_of_words = len(words_list)
    
    return number_of_words

def char_count(book_text):

    character_counts = {}

    for c in book_text:
        c = c.lower()
        if c not in character_counts:
            character_counts[c] = 1

        else:
            character_counts[c] +=1

    return character_counts

def sort_on(dict):
    return dict["num"]

def dict_sorter(character_counts):
    results = []

    for char, count in character_counts.items():
        results.append({"char": char, "num": count})

    results.sort(reverse=True, key=sort_on)
    

    return results