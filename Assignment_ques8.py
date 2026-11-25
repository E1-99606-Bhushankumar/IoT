def filter_long_words(words, min_length):
    result = []
    for word in words:
        
        char_count = 0
        for _ in word:
            char_count = char_count + 1
            
        if char_count > min_length:
            result = result + [word]
            
    return result

word_list = ["apple", "banana", "cat", "elephant", "dog"]
print(filter_long_words(word_list, 4))
