def sort_on(dict):
    return dict["count"]


def count_words(data):
    return len(data.split())


def count_letters(data):
    count = 0
    letters_dictionary = {}
    for letter in data:
        if letter in letters_dictionary:
            letters_dictionary[letter] += 1
        else:
            letters_dictionary[letter] = count + 1
    return letters_dictionary


def print_report(words_count, letters_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    letters_list = []
    for letter in letters_count:
        if letter.isalpha():
            letters_list.append({'name': letter, 'count': letters_count[letter]})
    letters_list.sort(reverse=True, key=sort_on)
    for item in letters_list:
        print(f"The '{item['name']}' character was found {item['count']} times")
    print("--- End report ---")


def main():
    with open('../books/frankenstein.txt') as f:
        file_contents = f.read()
        num_of_words = count_words(file_contents)
        letters_count = count_letters(file_contents.lower())
        print_report(num_of_words, letters_count)
    return num_of_words, letters_count


main()
