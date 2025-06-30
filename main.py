from stats import get_num_words, get_num_characters, sort_dict
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) > 1:
        param = sys.argv[1]
    book_text = get_book_text(param)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {param}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for k in sort_dict(get_num_characters(book_text)):
        print(f"{k['char']}: {k['num']}")
    print("============= END ===============")
    #print(f"{sort_dict(get_num_characters(book_text))}")

if __name__ == "__main__":
    main()