from stats import count_words, get_character_count
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    c_count = get_character_count(text)

    print(c_count)

def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
    
    return book_content

main()
