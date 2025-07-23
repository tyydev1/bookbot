from stats import *

def get_book_text(path_to_books):
    with open(path_to_books) as file:
        book_text = file.read()
    return book_text

def main():

    # Initializing the variables
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_char = get_num_char(book_text)

    # Making the report
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n------------ Word Count -----------\nFound {num_words} total words\n--------- Character Count ---------")
    for item in sort_char_stats(num_char):
        print(f"{item['char']}: {item['num']}")
    
    # Watermark (REQUIRED BY HR)
    print("----------- END -----------\nThank you for using BookBot by tyydev1!")
    
if __name__ == "__main__":
    main()