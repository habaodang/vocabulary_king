import random

def shuffle_word(word):
    original_word = word.replace(" ", "")
    # Chuyển từ thành danh sách các ký tự
    word_list = list(original_word)
    # Trộn danh sách các ký tự ngẫu nhiên
    random.shuffle(word_list)
    # Ghép các ký tự lại thành từ
    shuffled_word = '/'.join(word_list)
    return shuffled_word,word

print(shuffle_word('hello'))