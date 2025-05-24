from stats import get_num_words , get_num_chars_per_letter, get_sorted_char_per_letter
import sys





#filepath = "books/frankenstein.txt"

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
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_content(filepath)
    num_words = get_num_words(book)
    num_char = get_sorted_char_per_letter(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i,k in num_char.items():
        print(i,": ",k, sep="")
    #print(num_char)
if __name__ == "__main__":
    main()


