import sys

from stats import word_counter, characters, descend, sort_on

def sys_check():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

sys_check()

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    content = get_book_text(sys.argv[1])
    count = word_counter(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    char_count = characters(content)
    ordered = descend(char_count)
    
    for entry in ordered:
        guess = entry["chars"]
        guess2 = entry["num"]

        if guess.isalpha() == True:
            print(f"{guess}: {guess2}")
    print("============= END ===============")
            

if __name__ == "__main__":
    main()
