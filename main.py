from stats import word_counter, characters, descend, sort_on

book = "books/frankenstein.txt"

def get_book_text():
    with open(book) as f:
        return f.read()

def main():
    content = get_book_text()
    count = word_counter(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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

