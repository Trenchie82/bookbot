def get_book_text(i):
    with open(i) as f:
        contents = f.read()
        return contents

def main(i):
    content = get_book_text(i)
    print(content)

book = "books/frankenstein.txt"

main(book)

