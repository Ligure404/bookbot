from stats import get_num_words , get_num_chars_per_letter

frankenstein_file_path = "../bookbot/books/frankenstein.txt"

def get_book_content(filepath: str) -> str: 
    """
    Reads the content of the book from the specified file path.
    
    Returns:
        str: The content of the book.
    """
    with open(filepath) as file:
        # Ensure the file is read correctly
        file_content = file.read()
        

    return file_content




def main():
    
    book = get_book_content(frankenstein_file_path)
    num_char = get_num_chars_per_letter(book)
    num_words = get_num_words(book)
    print(f"Number of characters per letter: {num_char}")
    print(f"{num_words} words found in the document") 
if __name__ == "__main__":
    main()


