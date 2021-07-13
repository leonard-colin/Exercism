def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter in str(sentence).lower():
            pangram = True
        else:
            pangram = False
            break
    return pangram