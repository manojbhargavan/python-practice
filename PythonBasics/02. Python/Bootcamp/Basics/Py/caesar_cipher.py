# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:55:58 2024

@author: manoj
"""
NO_OF_LETTERS = 26
ASCII_A = 65
ASCII_a = 97

def encrypt(text, number):
    
    number = number % NO_OF_LETTERS
    
    capitals = []
    for i in range(ASCII_A, ASCII_A + NO_OF_LETTERS):
        capitals.append(chr(i))
        
    small = []
    for i in range(ASCII_a, ASCII_a + NO_OF_LETTERS):
        small.append(chr(i))
        
    shifted_caps = capitals[number:]
    shifted_caps.extend(capitals[:number])
    
    shifted_small = small[number:]
    shifted_small.extend(small[:number])
    
    result = ""
    for c in text:
        if c.isalpha() and c.isupper():
            result += shifted_caps[ord(c) % ASCII_A]
        elif c.isalpha() and c.islower():
            result += shifted_small[ord(c) % ASCII_a]
        else:
            result += c
    
    return result
    
text_to_encrypt = 'The cat ran, a swift streak of fur in the garden!!'
number = 30
encrypted_text = encrypt(text_to_encrypt, number)
decrypted_text = encrypt(encrypted_text, -1 * number)
print(encrypted_text)
print(decrypted_text)

hound_of_baskervilles_excerpt = """
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he stayed up all night, was seated at the breakfast table. I stood upon the hearth-rug and picked up the stick which our visitor had left behind him the night before. It was a fine, thick piece of wood, bulbous-headed, of the sort which is known as a "Penang lawyer." Just under the head was a broad silver band, nearly an inch across. "To James Mortimer, M.R.C.S., from his friends of the C.C.H.," was engraved upon it, with the date "1884." It was just such a stick as the old-fashioned family practitioner used to carry—dignified, solid, and reassuring.
"""
print(encrypt(hound_of_baskervilles_excerpt, 10))
print(encrypt(encrypt(hound_of_baskervilles_excerpt, 10), -10))