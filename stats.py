def word_counter(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def characters(text):
    words = str(text)
    words = words.lower()
    char_dict = {}
    for char in words:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict
    