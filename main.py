def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    lowered_string = text.lower()
    char_count = get_num_chars(lowered_string)
    # print(char_count)
    unsorted_report = report(char_count)
    unsorted_report.sort(reverse=True, key=sort_on)
    for char_dict in unsorted_report:
        if char_dict['char'].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(lowered_string):
    lowered_dict = {}
    for char in lowered_string:
        if char in lowered_dict:
            lowered_dict[char] += 1
        else:
            lowered_dict[char] = 1
    return lowered_dict

def report(char_count):
    report_list = []
    for char, num in char_count.items():
        new_dict = {'char': char, 'num': num}
        report_list.append(new_dict)
    return report_list



main()

