print("<-------analyse text------->")


def analyse_text(text):

    reversed_text(text)
    count_digits(text)
    count_vowels(text)
    count_word(text)




def reversed_text(text):
   return text[::-1]

def count_digits(text):
    digit_count = 0
    for digit in text:
        if digit in '0123456789':
             digit_count = digit_count + 1
             return digit_count
           

def count_vowels(text):
    vowel_count = 0
    for char in text.lower():
        if char in "aeiou" :
            # return {vowel,vowel.count(vowel)}
            vowel_count= vowel_count + 1
            return vowel_count
        

def count_word(text):
    return len(text.split())




text = "I will be learning python"

print(count_word(text))
print(count_word(text))
print(count_word(text))
print(count_word(text))
