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





def get_sorted_char_per_letter(book: str) -> dict:    
    """
    Counts the number of characters per letter in the book content.
    
    Args:
        book (str): The content of the book.
        
    Returns:
        dict: A dictionary with letters as keys and their counts as values.
    """
    char_dict = {}
    for letter in book.lower():
        if letter.isalpha():  # Count only alphabetic characters
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    sorted_char = {k: v for k ,v in sorted(char_dict.items(), key=lambda item: item[1],reverse=True)}
    return sorted_char