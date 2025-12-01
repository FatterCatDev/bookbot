from stats import count_words, get_book_text, get_character_count
def main():
    print(get_character_count(get_book_text("books/frankenstein.txt")))

main()
