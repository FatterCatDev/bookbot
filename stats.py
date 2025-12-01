def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
    
    return book_content

def count_words(content):
    word_count = len(content.split())
    return word_count

def get_character_count(content_str):
    c_count_dict = {}
    content_str_lower = content_str.lower()
    for c in content_str_lower:
        if c in c_count_dict:
            c_count_dict[c] += 1
        else:
            c_count_dict[c] = 1
    return c_count_dict