def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    sorted_dict_list = create_sorted_dict_list(chars_dict)

    print_report(book_path, num_words, sorted_dict_list)
 
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] =1
    return chars

def create_sorted_dict_list(chars_dict):
    def sort_on(dict):
        return dict["count"]

    sorted_dict_list = []

    for char in chars_dict:
        sorted_dict_list.append({"char" :char, "count":chars_dict[char]})
    
    sorted_dict_list.sort(reverse=True, key=sort_on)
    
    return sorted_dict_list

def print_report(book_path, num_words, dict_list):
    print(f"--- Begin report of {book_path} --- \n")
    print(f"{num_words} words found in the document \n")

    for item in dict_list:
        if item["char"].isalpha():
            print(f"The'{item['char']}' character was found {item['count']} times \n")

    print("--- End report ---")


main()
    

