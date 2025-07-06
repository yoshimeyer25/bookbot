import sys
from stats import get_num_words, get_num_characters


def main():
    path_to_book = parse_inputs()
    frankenstein = get_book_text(path_to_book)
    num_words = get_num_words(frankenstein)
    num_characters = get_num_characters(frankenstein)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_in_order(num_characters)
    print("============= END ===============")

def parse_inputs():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_in_order(num_characters):
    for k in sorted(num_characters, key=num_characters.get, reverse=True):
        v = num_characters[k]
        print(f"{k}: {v}")


main()
