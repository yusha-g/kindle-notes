import pandas as pd

def extract_unique_titles():
    ...

def clean_titles(book, author):
    separators = ['-', '_', '[', '(']

    book=book.replace("\ufeff","").title()
    author = author[:-2].title()

    for char in separators:
        if char in book:
            if char == '[' or char == '(':
                book = book.split(char)[0]
            book = book.replace(char, " ")

    book=book.replace("By "+author,"")
    book=book.replace(author,"")
    if "," in author:
        author = author.split(",")
        author = " ".join(author[::-1])
    
    return book.strip(), author.strip()

if __name__ == "__main__":
    my_clippings = open("resources/My Clippings.txt", "r")
    book_dictionary = {}
    for line in my_clippings:
        try:
            """last character of every line is \n. So we take the second last character."""
            last_char = line[-2]
        except IndexError:
            # Skip empty line
            continue
        if last_char == ")":
            book, author = line.rsplit("(", 1)
            book, author = clean_titles(book, author)
            book_dictionary[book]={
                "Author": author
            }
    print(book_dictionary)