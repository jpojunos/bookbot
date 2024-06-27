def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_dict = char_count(file_contents)
        sorted_chars = sort_dict_val(char_dict)
        
        print("---------Report Begins----------",end="\n\n")
        print(f"There are {word_count(file_contents)} words in this book",end = "\n\n")
        for i in sorted_chars:
            print(f"The letter {i[0]} has {i[1]} occurances in this book")
        print("---------Report Ends----------")

def word_count(file_content):
    words = file_content.split()
    return len(words)

def char_count(file_content):
    chars = {}
    for char in file_content:
        lowered = char.lower()
        if lowered in chars:    
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict_val(dict):
    sorted_items = []
    for keys in sorted(dict.items(), key = sort_on, reverse=True):
        if keys[0].isalpha() == True:
            sorted_items.append([keys[0],keys[1]])
    return sorted_items


def sort_on(dict):
    return dict[1]


main() 