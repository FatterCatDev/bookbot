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

def sort_on(item):
    return item["num"]

def get_character_count_ls(char_count_dict):
    char_cnt_list = []
    for key, val in char_count_dict.items():
        tmp_char_dict = {
            "char":key,
            "num":val,
        }
        char_cnt_list.append(tmp_char_dict)
    char_cnt_list.sort(reverse=True, key=sort_on)
    return char_cnt_list
    