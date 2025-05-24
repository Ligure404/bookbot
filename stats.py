def get_num_words(book: str) -> int:
    
    book = book.split()
    count_words = len(book)

    return count_words

test = "This is a test book with some words."


def get_num_chars_per_letter(book):
    char_dict = {}
    for letter in book.lower():
        if letter in char_dict:
            char_dict[letter] = char_dict[letter] + 1
        else:
            char_dict[letter] = 1
    return char_dict

