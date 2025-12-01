from stats import count_words, get_character_count, get_character_count_ls
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    w_count = count_words(text)
    c_count = get_character_count(text)
    char_count_ls = get_character_count_ls(c_count)
    print_report(book_path, w_count, char_count_ls)

def print_report(book_path, w_count, char_count_ls):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for item in char_count_ls:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
    
    return book_content

main()
