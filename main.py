from stats import word_counter, characters

book = "books/frankenstein.txt"

def get_book_text():
    with open(book) as f:
        return f.read()

def main():
    content = get_book_text()
    count = word_counter(content)
    print(f"{count} words found in the document")
    char_count = characters(content)
    print(char_count)

if __name__ == "__main__":
    main()

