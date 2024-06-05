def main():
    file_contents = None
    with open("books/frankenstien.txt") as f:
        file_contents = f.read()

    words = count_words(file_contents)
    characters = sort_characters(count_characters(file_contents))
    
    
    print(characters)

def count_words(str):
    words = str.split()
    return len(words)

def count_characters(str):
    lowercase = str.lower()
    letters = {}

    for char in lowercase:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    
    return letters

def sort_characters(char_count):
    char_count_list = []
    for char in char_count:
        if char.isalpha():
            char_count_list.append({"char": char, "count": char_count[char]})
    
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list
    


def sort_on(dict):
    return dict["count"]

main()