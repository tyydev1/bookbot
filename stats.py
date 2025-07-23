def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_char(book_text):
    text = book_text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sorter(items):
    return items["num"]

def sort_char_stats(dictionary):
    new_list = []
    for char, count in dictionary.items():
        if char.isalpha():
            new_dict = {'char': char, 'num': count}
            new_list.append(new_dict)
    new_list.sort(reverse=True, key=sorter)
    return new_list
