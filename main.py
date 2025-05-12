from stats import *
import sys


def get_book_text(i):
    with open(i) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    num_times = num_of_times(book_text)
    sorted_chars = dict_words(num_times)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("---------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count --------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    

main()

